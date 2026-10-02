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
from ui_kz import kz


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
        app.selectbox(key='artist_preset').set_value('Трэвис Скотт').run()
        self.assertFalse(app.exception)
        self.assertEqual(app.selectbox(key='genre_family').value, 'Trap')
        self.assertEqual(app.slider(key='tempo').value, 140)
        self.assertEqual(app.selectbox(key='autotune').value, 'Fast-retune trap autotune')
        app.selectbox(key='artist_preset').set_value('Адель').run()
        self.assertFalse(app.exception)
        self.assertEqual(app.selectbox(key='voice_type').value, 'Әйел дауысы')
        self.assertEqual(app.selectbox(key='voice_range_Әйел дауысы').value, 'Меццо-сопрано')
        self.assertEqual(app.selectbox(key='autotune').value, 'Off / natural uncorrected vocal')
        self.assertEqual(app.text_area[0].value, 'Менің өз өлеңім')
        app.selectbox(key='mood').set_value('Peaceful').run()
        self.assertEqual(app.selectbox(key='mood').value, 'Peaceful')
        self.assertEqual(len(app.code), 0)

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
        app.selectbox(key='genre_family').set_value('Trap').run()
        self.assertIn(kz('Melodic trap'), app.selectbox(key='genre_Trap').options)
        self.assertTrue(any('Лос Анджелес' in x for x in app.selectbox(key='region_Trap').options))
        self.assertFalse(app.error)
        app.selectbox(key='genre_Trap').set_value('Melodic trap')
        app.selectbox(key='region_Trap').select_index(2)
        app.selectbox(key='output_language').set_value('Өзбекше')
        app.selectbox(key='voice_range_Еркек дауысы').set_value('Баритон')
        app.multiselect(key='voice_timbres').set_value(['Мұрындық', 'Жарқын'])
        app.selectbox(key='autotune').set_value('Fast-retune trap autotune')
        app.selectbox(key='reverb').set_value('Plate reverb')
        app.selectbox(key='delay').set_value('Tape echo')
        app.multiselect(key='instruments').set_value(['Dombra', '808 bass'])
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
            app.button[0].click().run()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.code), 2)
        spec = json.loads(captured[0]['messages'][1]['content'])
        self.assertEqual(spec['genre'], 'Melodic trap')
        self.assertIn('baritone', spec['voice_direction'])
        self.assertIn('nasal', spec['voice_direction'])
        self.assertIn('bright', spec['voice_direction'])
        app.selectbox(key='voice_type').set_value('Әйел дауысы').run()
        self.assertNotIn('Баритон', app.selectbox(key='voice_range_Әйел дауысы').options)
        self.assertIn('Сопрано', app.selectbox(key='voice_range_Әйел дауысы').options)
        controls = spec['studio_controls']
        self.assertEqual(controls['output_language'], 'Uzbek')
        self.assertIn('Los Angeles', controls['regional_style'])
        self.assertEqual(controls['tempo_bpm'], 140)
        self.assertEqual(controls['autotune'], 'Fast-retune trap autotune')
        self.assertEqual(controls['instruments'], ['Dombra', '808 bass'])
        app.selectbox(key='genre_family').set_value('Jazz').run()
        self.assertIn(kz('Bebop'), app.selectbox(key='genre_Jazz').options)
        self.assertEqual(len(app.code), 2)
        self.assertTrue(app.info)
        # A failed request clears stale output and produces actionable diagnostics.
        def unavailable(request):
            return httpx.Response(403, json={'error': {'code': 'model_not_found'}})
        with patch('groq.Groq', side_effect=lambda **kwargs: Groq(**kwargs,
                http_client=httpx.Client(transport=httpx.MockTransport(unavailable)))):
            app.button[0].click().run()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.code), 0)
        self.assertIn('HTTP 403', app.error[0].value)


if __name__ == '__main__':
    unittest.main()
