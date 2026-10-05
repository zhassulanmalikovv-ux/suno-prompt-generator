"""Curated daily inspiration; deterministic across visitors in Kazakhstan (UTC+5)."""
from datetime import datetime, timedelta, timezone
import random

KAZAKHSTAN = timezone(timedelta(hours=5))
DIRECTIONS = [
    ("Домбыра және заманауи поп", "Kazakh folk pop, crisp dombra arpeggios, warm electric bass, organic percussion, memorable melodic chorus", 104),
    ("Қазақша той", "Kazakh wedding dance pop, sparkling dombra riffs, festive hand percussion, punchy kick, joyful call-and-response chorus", 126),
    ("Түнгі Лос-Анджелес", "West Coast melodic trap, rolling sub bass, restrained 808 slides, syncopated hi-hats, hazy electric piano, spacious half-time groove", 140),
    ("Сағыныш балладасы", "Intimate Kazakh piano ballad, felt piano, delicate kobyz textures, restrained strings, emotional rising chorus", 72),
    ("Неонды синтвейв", "Cinematic synthwave, analog pads, pulsing arpeggiators, gated snare, rounded synth bass, nostalgic night-drive atmosphere", 108),
    ("Жылы лоу-фай", "Warm lo-fi soul, dusty Rhodes chords, soft vinyl texture, brushed drums, mellow upright bass, relaxed swung pocket", 82),
    ("Эпикалық оркестр", "Epic orchestral pop, soaring strings, brass swells, cinematic toms, delicate opening piano, expansive final chorus", 92),
    ("Өзбекше би попы", "Uzbek dance pop, bright dutar phrases, doira rhythms, modern synth bass, lively percussion and playful melodic hooks", 118),
    ("Қырғызша фолк", "Kyrgyz contemporary folk, intricate komuz picking, airy acoustic textures, subtle frame drums, open mountain atmosphere", 96),
    ("Қараңғы альтернатив рок", "Dark alternative rock, textured guitars, driving live drums, deep bass, intimate verses and cathartic powerful chorus", 124),
    ("Жұмсақ афро-поп", "Melodic Afro-pop, interlocking clean guitars, warm bass, shakers, syncopated percussion, sunlit danceable groove", 110),
    ("Кеңістікті электроника", "Atmospheric melodic house, layered analog synths, deep four-on-the-floor kick, shimmering plucks, gradual uplifting build", 122),
    ("Джаз және нео-соул", "Jazz neo-soul, extended Rhodes chords, expressive muted trumpet, elastic electric bass, laid-back live drums", 88),
    ("Қазақша терме эксперименті", "Contemporary Kazakh terme fusion, rhythmic dombra ostinato, declamatory melodic phrasing, subtle electronic low end, sparse percussion", 100),
    ("Акустикалық инди", "Acoustic indie folk, fingerpicked guitar, soft mandolin, intimate room ambience, gentle bass, understated live percussion", 94),
    ("Драмалық R&B", "Modern alternative R&B, lush electric piano, deep sub bass, minimal trap percussion, spacious pads, emotionally rich harmonies", 76),
]
VOICES = [
    "Warm male baritone, velvety chest resonance, clear diction, gentle vibrato, restrained soulful phrasing",
    "Bright female mezzo-soprano, rounded low notes, airy verse delivery, confident sustained chorus, natural vibrato",
    "Expressive male tenor, clear upper register, smooth legato, controlled falsetto accents, dynamic emotional phrasing",
    "Rich female alto, smoky warm timbre, intimate articulation, subtle breath texture, powerful grounded chorus",
    "Male-female duet, complementary registers, alternating verses, close harmony in the chorus, distinct natural timbres",
    "Intimate androgynous vocal, soft breathy tone, precise diction, understated melodic phrasing and layered harmonies",
]
FINISHES = [
    "Natural pitch correction, short warm plate reverb, subtle quarter-note delay, transparent compression",
    "Expressive audible autotune, spacious hall reverb, filtered ping-pong delay, controlled low-end compression",
    "No audible autotune, intimate room reverb, gentle tape saturation, minimal delay, organic dynamics",
    "Light pitch correction, lush plate reverb, dotted-eighth delay, polished vocal layering and clean transients",
]


def daily_collection(day=None):
    day = day or datetime.now(KAZAKHSTAN).date()
    rng = random.Random(day.isoformat())
    rows = []
    for title, direction, bpm in rng.sample(DIRECTIONS, 8):
        prompt = (f"{direction}. {bpm} BPM. {rng.choice(VOICES)}. "
                  f"{rng.choice(FINISHES)}. Original melody; verse, pre-chorus, hook-driven chorus, "
                  "contrasting bridge, final chorus and clean outro. Wide instrumental stereo image, "
                  "focused centered lead vocal, professional balanced studio mix, no clipping.")
        rows.append({"title": title, "style_prompt": prompt})
    return day, rows
