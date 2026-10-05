"""Run with: python -m unittest discover -s tests -v (no live API calls)."""
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

import httpx
from groq import Groq
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from catalog import GENRE_GROUPS, GENRE_COUNT, VOICE_PRESETS, LANGUAGES
from app import validate_result
from app import normalize_lyrics, validate_random_concept

def select(app, key):
    return app.selectbox(key="_locale_" + app.session_state["ui_language"] + "_" + key)

def multi(app, key):
    return app.multiselect(key="_locale_" + app.session_state["ui_language"] + "_" + key)


class StudioTests(unittest.TestCase):
    def test_artist_presets(self):
        from presets import PRESETS, preset_settings
        from ui_kz import VOICE_RANGES, TIMBRES
        from catalog import INSTRUMENTS
        self.assertGreaterEqual(len(PRESETS), 100)
        for name in PRESETS:
            settings = preset_settings(name)
            family = settings['genre_family']
            self.assertIn(settings['genre_' + family], GENRE_GROUPS[family], name)
            voice = settings['voice_type']
            if voice != 'Дауыссыз':
                self.assertIn(settings['voice_range_' + voice], VOICE_RANGES[voice], name)
            self.assertTrue(set(settings['instruments']) <= set(INSTRUMENTS))
            self.assertTrue(set(settings['voice_timbres']) <= set(TIMBRES))
            self.assertNotIn(name, settings['custom_notes'])
        app = AppTest.from_file(str(ROOT / 'app.py'), default_timeout=30).run()
        app.text_area[0].set_value('Менің өз өлеңім').run()
        select(app, 'artist_preset').set_value('Трэвис Скотт').run()
        self.assertFalse(app.exception)
        self.assertEqual(select(app, 'genre_family').value, 'Trap')
        self.assertEqual(app.slider(key='tempo').value, 140)
        self.assertEqual(select(app, 'autotune').value, 'Fast-retune trap autotune')
        select(app, 'artist_preset').set_value('Адель').run()
        self.assertFalse(app.exception)
        self.assertEqual(select(app, 'voice_type').value, 'Әйел дауысы')
        self.assertEqual(select(app, 'voice_range_Әйел дауысы').value, 'Меццо-сопрано')
        self.assertEqual(select(app, 'autotune').value, 'Off / natural uncorrected vocal')
        self.assertEqual(app.text_area[0].value, 'Менің өз өлеңім')
        select(app, 'mood').set_value('Peaceful').run()
        self.assertEqual(select(app, 'mood').value, 'Peaceful')
        self.assertNotIn('suno_result', app.session_state)

    def test_language_switch_preserves_controls(self):
        app = AppTest.from_file(str(ROOT / 'app.py'), default_timeout=30).run()
        select(app, 'artist_preset').set_value('Адель').run()
        app.text_area(key='lyrics_source').set_value('Менің өз өлеңім').run()
        multi(app, 'voice_timbres').set_value(['Мұрындық', 'Жарқын']).run()
        for lang in ['en', 'ru', 'kk', 'en', 'kk']:
            app.selectbox(key='ui_language').set_value(lang).run()
            self.assertFalse(app.exception)
            self.assertEqual(app.session_state['artist_preset'], 'Адель')
            self.assertEqual(app.session_state['voice_type'], 'Әйел дауысы')
            self.assertEqual(app.session_state['voice_timbres'], ['Мұрындық', 'Жарқын'])
            self.assertEqual(app.text_area(key='lyrics_source').value, 'Менің өз өлеңім')
            self.assertEqual(app.session_state['autotune'], 'Off / natural uncorrected vocal')
        select(app, 'artist_preset').set_value('Трэвис Скотт').run()
        self.assertEqual(app.session_state['genre_family'], 'Trap')

    def test_escaped_lyrics(self):
        self.assertEqual(normalize_lyrics(r'[Verse]\nҚазақша\r\n[Chorus]\nЖол'),
                         '[Verse]\nҚазақша\n[Chorus]\nЖол')
        concept = {'title':'Идея','concept':'Бағыт','style_prompt':'A new sound',
                   'lyrics':r'[Verse]\nӘн'}
        self.assertEqual(validate_random_concept(json.dumps(concept))['lyrics'], '[Verse]\nӘн')

    def test_catalog_and_limits(self):
        self.assertGreaterEqual(GENRE_COUNT, 300)
        self.assertGreaterEqual(len(VOICE_PRESETS), 100)
        self.assertIn('Қазақша', LANGUAGES)
        self.assertIn('Өзбекше', LANGUAGES)
        self.assertIn('Қырғызша', LANGUAGES)
        self.assertIn('Trap', GENRE_GROUPS['Trap'])
        result = {'style_prompt': 'x' * 900, 'structure_lyrics': '[Verse 1]\nTest'}
        self.assertEqual(len(validate_result(json.dumps(result))['style_prompt']), 900)
        result['style_prompt'] += 'x'
        with self.assertRaises(ValueError):
            validate_result(json.dumps(result))

    def test_reactive_studio_and_groq_payload(self):
        app = AppTest.from_file(str(ROOT / 'app.py'), default_timeout=30).run()
        self.assertFalse(app.exception)
        select(app, 'genre_family').set_value('Trap').run()
        self.assertIn('Melodic trap', GENRE_GROUPS[app.session_state['genre_family']])
        self.assertGreater(len(select(app, 'region_Trap').options), 2)
        self.assertFalse(app.error)
        select(app, 'genre_Trap').set_value('Melodic trap')
        select(app, 'region_Trap').select_index(2)
        select(app, 'output_language').set_value('Өзбекше')
        select(app, 'voice_range_Еркек дауысы').set_value('Баритон')
        multi(app, 'voice_timbres').set_value(['Мұрындық', 'Жарқын'])
        select(app, 'autotune').set_value('Fast-retune trap autotune')
        select(app, 'reverb').set_value('Plate reverb')
        select(app, 'delay').set_value('Tape echo')
        multi(app, 'instruments').set_value(['Dombra', '808 bass'])
        app.checkbox(key='auto_tempo').uncheck().run()
        app.slider(key='tempo').set_value(140)
        app.text_area[0].set_value('Достық туралы ән')
        app.secrets['GROQ_API_KEY'] = 'test-key'
        captured = []
        output = {'style_prompt': 'Melodic trap, Los Angeles groove, warm baritone, dombra, 808 bass, 140 BPM, tape echo.',
                  'structure_lyrics': '[Verse 1]\nDo‘stlik bizni birlashtirar\n[Chorus]\nBirga kuylaymiz'}

        def handler(request):
            self.assertEqual(request.url.host, 'api.groq.com')
            captured.append(json.loads(request.content))
            return httpx.Response(200, json={'id': 'test', 'object': 'chat.completion', 'created': 1,
                'model': 'openai/gpt-oss-20b', 'choices': [{'index': 0, 'finish_reason': 'stop',
                'message': {'role': 'assistant', 'content': json.dumps(output)}}]})

        with patch('groq.Groq', side_effect=lambda **kwargs: Groq(**kwargs,
                http_client=httpx.Client(transport=httpx.MockTransport(handler)))):
            app.button(key='generate_prompt').click().run()
        self.assertFalse(app.exception)
        self.assertEqual(app.session_state['suno_result'], output)
        spec = json.loads(captured[0]['messages'][1]['content'])
        self.assertEqual(spec['genre'], 'Melodic trap')
        self.assertIn('baritone', spec['voice_direction'])
        self.assertIn('nasal', spec['voice_direction'])
        self.assertIn('bright', spec['voice_direction'])
        select(app, 'voice_type').set_value('Әйел дауысы').run()
        self.assertNotIn('Баритон', select(app, 'voice_range_Әйел дауысы').options)
        self.assertIn('Сопрано', select(app, 'voice_range_Әйел дауысы').options)
        controls = spec['studio_controls']
        self.assertEqual(controls['output_language'], 'Uzbek')
        self.assertIn('Los Angeles', controls['regional_style'])
        self.assertEqual(controls['tempo_bpm'], 140)
        self.assertEqual(controls['autotune'], 'Fast-retune trap autotune')
        self.assertEqual(controls['instruments'], ['Dombra', '808 bass'])
        select(app, 'genre_family').set_value('Jazz').run()
        self.assertIn('Bebop', GENRE_GROUPS[app.session_state['genre_family']])
        self.assertEqual(app.session_state['suno_result'], output)
        self.assertTrue(app.info)
        # A failed request clears stale output and produces actionable diagnostics.
        def unavailable(request):
            return httpx.Response(403, json={'error': {'code': 'model_not_found'}})
        with patch('groq.Groq', side_effect=lambda **kwargs: Groq(**kwargs,
                http_client=httpx.Client(transport=httpx.MockTransport(unavailable)))):
            app.button(key='generate_prompt').click().run()
        self.assertFalse(app.exception)
        self.assertNotIn('suno_result', app.session_state)
        self.assertIn('HTTP 403', app.error[0].value)


if __name__ == '__main__':
    unittest.main()
