"""Musical presets: real genres, regional directions, and composable studio controls."""

_GROUPS = {
    "Қазақша / Turkic": "Қазақша той|Қазақша мұңды|Қазақша лирика|Қазақша халық әні|Қазақша терме|Қазақша дәстүрлі ән|Қазақша эстрада|Қазақша Q-Pop|Қазақша рэп|Қазақша этно-фьюжн|Kazakh Folk|Kyrgyz folk|Uzbek pop|Uzbek maqom|Uyghur muqam|Turkish folk|Anatolian rock|Azerbaijani mugham|Turkmen folk|Tatar pop|Bashkir folk|Sakha folk",
    "Trap": "Trap|Melodic trap|Southern trap|Atlanta trap|West Coast trap|Latin trap|Cloud trap|Emo trap|Dark trap|Hard trap|Orchestral trap|Ambient trap|Electronic trap|Trap soul|Rage rap|Plugg|Pluggnb|Detroit trap|Memphis trap|Experimental trap",
    "Hip-Hop / Rap": "Hip-Hop|Boom bap|West Coast hip-hop|East Coast hip-hop|G-funk|Gangsta rap|Conscious hip-hop|Jazz rap|Alternative hip-hop|Abstract hip-hop|Underground hip-hop|Hardcore hip-hop|Political hip-hop|Chopper rap|Crunk|Snap music|Hyphy|Horrorcore|Cloud rap|Emo rap|Pop rap|Country rap|Industrial hip-hop|Instrumental hip-hop|Lo-fi hip-hop",
    "Drill / Phonk": "Chicago drill|UK drill|Brooklyn drill|New York drill|Melodic drill|Sample drill|Jersey drill|Latin drill|French drill|Phonk|Drift phonk|House phonk|Brazilian phonk|Memphis phonk|Wave phonk|Raw phonk",
    "Pop": "Pop|Dance-pop|Synth-pop|Electropop|Indie pop|Art pop|Dream pop|Chamber pop|Baroque pop|Power pop|Teen pop|Bubblegum pop|Sophisti-pop|Hyperpop|Bedroom pop|Ambient pop|Orchestral pop|Acoustic pop|J-pop|K-pop|C-pop|City pop|Europop|Latin pop",
    "R&B / Soul": "R&B|Contemporary R&B|Alternative R&B|Neo-soul|Soul|Southern soul|Northern soul|Blue-eyed soul|Psychedelic soul|Soul blues|Quiet storm|New jack swing|PBR&B|Gospel soul|Funk soul|Motown|Smooth soul|Future soul",
    "Rock": "Rock|Classic rock|Hard rock|Soft rock|Blues rock|Folk rock|Progressive rock|Psychedelic rock|Garage rock|Glam rock|Art rock|Arena rock|Southern rock|Country rock|Roots rock|Surf rock|Instrumental rock|Space rock|Math rock|Post-rock|Experimental rock|Stoner rock",
    "Alternative / Indie": "Alternative rock|Indie rock|Britpop|Grunge|Post-grunge|Shoegaze|Noise rock|Dream rock|Slowcore|Sadcore|College rock|Madchester|Baggy|Jangle pop|Gothic rock|Darkwave|New wave|No wave",
    "Punk": "Punk rock|Pop punk|Hardcore punk|Post-hardcore|Post-punk|Anarcho-punk|Street punk|Skate punk|Ska punk|Celtic punk|Horror punk|Garage punk|Crust punk|D-beat|Emo|Screamo|Emocore|Folk punk",
    "Metal": "Heavy metal|Thrash metal|Death metal|Black metal|Doom metal|Power metal|Symphonic metal|Progressive metal|Folk metal|Industrial metal|Nu metal|Alternative metal|Groove metal|Gothic metal|Metalcore|Deathcore|Djent|Sludge metal|Stoner metal|Post-metal|Melodic death metal|Technical death metal|Atmospheric black metal|Blackgaze",
    "House": "House|Deep house|Tech house|Progressive house|Future house|Bass house|Electro house|Acid house|Chicago house|French house|Disco house|Soulful house|Afro house|Amapiano|Organic house|Melodic house|Tropical house|Minimal house|Tribal house|Garage house|Lo-fi house|Ghetto house",
    "Techno": "Techno|Detroit techno|Minimal techno|Dub techno|Acid techno|Industrial techno|Hard techno|Melodic techno|Hypnotic techno|Peak-time techno|Schranz|Ambient techno|Raw techno|Hardgroove techno|Bleep techno",
    "Trance": "Trance|Progressive trance|Uplifting trance|Vocal trance|Psytrance|Goa trance|Full-on psytrance|Dark psytrance|Forest psytrance|Tech trance|Hard trance|Acid trance|Balearic trance|Eurotrance",
    "Bass / EDM": "EDM|Dubstep|Brostep|Riddim dubstep|Melodic dubstep|Future bass|Color bass|Bass music|Midtempo bass|Glitch hop|Moombahton|Moombahcore|Big room|Festival electro|Complextro|Hardstyle|Rawstyle|Hardcore techno|Gabber|Happy hardcore|Frenchcore|Speedcore",
    "Drum & Bass": "Drum and bass|Liquid drum and bass|Neurofunk|Jump-up|Techstep|Darkstep|Atmospheric drum and bass|Intelligent drum and bass|Jungle|Ragga jungle|Darkside jungle|Drumfunk|Sambass|Dancefloor drum and bass|Half-time drum and bass",
    "UK Garage / Breaks": "UK garage|2-step garage|Speed garage|Future garage|Bassline|UK funky|Grime|Breakbeat|Big beat|Nu skool breaks|Electro breaks|Progressive breaks|Breakcore|Baltimore club|Jersey club|Footwork|Juke",
    "Synth / Retro": "Synthwave|Retrowave|Darksynth|Outrun|Dreamwave|Chillwave|Vaporwave|Future funk|Mallsoft|Synth-funk|Minimal wave|Cold wave|Electroclash|Italo disco|Hi-NRG|EBM|New beat|Chiptune",
    "Ambient / Downtempo": "Ambient|Dark ambient|Space ambient|Drone|Ambient dub|Downtempo|Chillout|Lounge|Trip-hop|Illbient|Psydub|Psybient|Balearic beat|Lo-Fi|Chillhop|New age|Meditation music|Soundscape|Lowercase",
    "Experimental": "IDM|Glitch|Experimental electronic|Musique concrete|Electroacoustic|Acousmatic|Noise|Harsh noise|Power electronics|Industrial|Sound collage|Deconstructed club|Microsound|Plunderphonics",
    "Jazz": "Jazz|Swing|Bebop|Hard bop|Cool jazz|Modal jazz|Free jazz|Avant-garde jazz|Jazz fusion|Smooth jazz|Soul jazz|Jazz-funk|Latin jazz|Afro-Cuban jazz|Bossa nova jazz|Gypsy jazz|Dixieland|Traditional jazz|Chamber jazz|Nu jazz|Acid jazz|Vocal jazz",
    "Blues / Funk": "Blues|Delta blues|Chicago blues|Texas blues|Piedmont blues|Country blues|Electric blues|Acoustic blues|Jump blues|Swamp blues|Hill country blues|Funk|P-funk|Electro-funk|Go-go|Boogie|Disco|Nu-disco",
    "Country / Americana": "Country|Traditional country|Contemporary country|Country pop|Outlaw country|Honky-tonk|Bluegrass|Progressive bluegrass|Western swing|Alt-country|Americana|Rockabilly|Psychobilly|Country soul|Red dirt|Bakersfield sound|Country folk",
    "Folk / Acoustic": "Folk|Acoustic|Contemporary folk|Indie folk|Traditional folk|Chamber folk|Anti-folk|Psychedelic folk|Neofolk|Celtic folk|Nordic folk|Balkan folk|Flamenco|Fado|Singer-songwriter|Acoustic instrumental|Folk blues",
    "Latin": "Salsa|Salsa romantica|Son cubano|Bachata|Merengue|Reggaeton|Dembow|Cumbia|Cumbia villera|Tango|Nuevo tango|Samba|Bossa nova|MPB|Baile funk|Brega funk|Forro|Norteno|Banda|Mariachi|Corridos tumbados|Ranchera|Bolero|Mambo|Cha-cha-cha",
    "Reggae / Caribbean": "Reggae|Roots reggae|Dub|Dancehall|Lovers rock|Rocksteady|Ska|Two-tone ska|Reggae fusion|Ragga|Soca|Calypso|Zouk|Kompa|Rockers reggae|Dub poetry",
    "Africa / Global": "Afrobeats|Afrobeat|Afropop|Highlife|Hiplife|Afro-swing|Gqom|Kwaito|Soukous|Ndombolo|Makossa|Mbalax|Afro-fusion|Gnawa|Desert blues|Ethiopian jazz|Bongo flava|Kizomba|Semba|Kuduro",
    "Asia / Middle East": "Arabic pop|Dabke|Rai|Chaabi|Shaabi|Khaliji|Persian pop|Persian classical|Indian classical|Hindustani classical|Carnatic classical|Qawwali|Ghazal|Bhangra|Bollywood|Filmi|Dangdut|Gamelan|Enka|Trot|Chinese traditional|Japanese traditional|Korean traditional",
    "Classical / Cinematic": "Orchestral|Classical|Baroque|Classical period|Romantic classical|Contemporary classical|Minimalism|Neo-classical|Chamber music|String quartet|Solo piano|Piano and strings|Opera|Operetta|Choral|Sacred choral|Symphonic|Epic cinematic|Cinematic ambient|Film score|Trailer music|Orchestral hybrid|Fantasy soundtrack|Video game soundtrack|Musical theatre",
    "Gospel / Vocal": "Gospel|Traditional gospel|Contemporary gospel|Urban gospel|Spiritual|A cappella|Barbershop|Doo-wop|Vocal harmony|Gregorian chant|Sacred vocal|Nasheed|Devotional music|Vocal jazz ensemble",
}
GENRE_GROUPS = {group: names.split("|") for group, names in _GROUPS.items()}
GENRE_COUNT = len({genre for names in GENRE_GROUPS.values() for genre in names})

REGIONAL_STYLES = {
    "Trap": ["California / West Coast: laid-back bounce, warm synths", "Los Angeles: spacious low-end, melodic West Coast leads", "Atlanta: rolling 808s, triplet hi-hats", "Memphis: dark bells, gritty bass", "Detroit: offbeat pocket, punchy piano", "Houston: slow chopped-and-screwed feel", "Miami: bass-heavy club bounce", "New York: gritty drums and samples", "London: UK rhythm and dark atmosphere", "Latin America: syncopated percussion and melodic hooks"],
    "Hip-Hop / Rap": ["California: sunny West Coast groove", "Los Angeles: G-funk synth leads and relaxed swing", "Bay Area: hyphy bounce", "New York: boom-bap grit", "Atlanta: Southern bounce", "Houston: slow deep groove", "Detroit: offbeat flow", "Memphis: eerie samples", "Chicago: soulful sampling", "London: UK urban rhythm", "Paris: melodic French rap production"],
    "Drill / Phonk": ["Chicago: sparse sinister drill", "London: sliding 808s and syncopated drill", "Brooklyn: energetic drill bounce", "Memphis: lo-fi phonk samples", "Brazil: distorted baile-funk pulse", "Tokyo: night-drive drift atmosphere"],
    "Қазақша / Turkic": ["Алматы: modern Kazakh pop with dombra", "Астана: polished cinematic Kazakh pop", "Шымкент: festive toy dance arrangement", "Қырғыз: komuz-led folk arrangement", "Өзбек: doira and dutar ornamentation", "Ұйғыр: muqam-inspired rhythmic ornamentation", "Түрік: baglama and darbuka arrangement", "Әзербайжан: tar and kamancha ornamentation", "Татар: accordion and folk dance pulse"],
    "House": ["Chicago: classic house swing", "Detroit: soulful electronic depth", "Paris: filtered French groove", "Ibiza: Balearic sunset atmosphere", "Berlin: minimal underground club", "South Africa: log-drum and Afro rhythm"],
    "Techno": ["Detroit: futuristic soulful machines", "Berlin: hypnotic industrial club", "Rotterdam: hard driving energy", "London: broken electronic rhythm"],
    "Jazz": ["New Orleans: traditional collective swing", "New York: modern bebop club", "Paris: intimate acoustic jazz", "Brazil: bossa nova sway", "Havana: Afro-Cuban percussion"],
    "Rock": ["California: sunlit guitar tone", "Los Angeles: polished arena sound", "Seattle: gritty grunge atmosphere", "London: British guitar sound", "Nashville: roots-oriented live band"],
    "Country / Americana": ["Nashville: polished country production", "Texas: raw outlaw band", "Bakersfield: bright twang", "Appalachia: acoustic bluegrass ensemble"],
    "Pop": ["Los Angeles: polished radio pop", "Stockholm: melodic Scandinavian pop", "Seoul: layered K-pop production", "Tokyo: bright city-pop color", "London: alternative art-pop texture", "Almaty: contemporary Kazakh pop"],
    "R&B / Soul": ["Detroit: Motown ensemble feel", "Memphis: warm Southern soul", "Philadelphia: lush orchestral soul", "Los Angeles: spacious contemporary R&B", "London: alternative R&B"],
    "Classical / Cinematic": ["Vienna: acoustic classical concert hall", "Hollywood: cinematic scoring stage", "London: orchestral studio clarity", "Paris: intimate chamber ensemble"],
    "Folk / Acoustic": ["Anatolia: baglama-led folk color", "Ireland: Celtic acoustic ensemble", "Nordic: sparse bowed-string folk", "Appalachia: string-band folk", "Almaty: dombra-led acoustic storytelling"],
    "Ambient / Downtempo": ["Bristol: moody trip-hop space", "Berlin: minimalist ambient electronics", "Tokyo: delicate environmental ambience", "Ibiza: Balearic sunset texture"],
    "Latin": ["Puerto Rico: reggaeton bounce", "Dominican Republic: bachata guitar", "Cuba: son and salsa percussion", "Colombia: cumbia pulse", "Brazil: samba and baile-funk textures", "Argentina: tango phrasing", "Mexico: regional brass and strings"],
}
DEFAULT_REGIONS = ["California: warm spacious production", "Los Angeles: polished contemporary studio sound", "London: textured alternative production", "Berlin: minimal electronic production", "Tokyo: precise bright electronic detail", "Istanbul: Anatolian instrumentation", "Almaty: modern Kazakh musical color"]

REGISTERS = {
    "Contralto / әйелдің төмен дауысы": "female contralto with a low chest register",
    "Mezzo-soprano / әйелдің орта дауысы": "female mezzo-soprano with a rich middle register",
    "Soprano / әйелдің жоғары дауысы": "female soprano with a bright high register",
    "Tenor / тенор": "male tenor with a clear upper register",
    "Baritone / баритон": "male baritone with rounded chest resonance",
    "Bass / бас": "male bass with a deep low register",
    "Countertenor / контртенор": "adult male countertenor with a light upper register",
    "Female alto / альт": "adult female alto with a grounded middle-low register",
    "Male midrange / орта ер дауысы": "adult male lead with a comfortable middle register",
    "Female midrange / орта әйел дауысы": "adult female lead with a comfortable middle register",
    "Duet / дуэт": "adult male-female duet with complementary registers",
    "Choir / хор": "blended adult choir with layered vocal registers",
}
TEXTURES = {
    "Қоңыр / Warm dark": "warm dark rounded timbre", "Барқыт / Velvety": "smooth velvety timbre",
    "Ауадай / Airy": "airy breathy timbre", "Қарлығыңқы / Husky": "husky textured timbre",
    "Таза / Clear": "clear clean focused timbre", "Жарқын / Bright": "bright forward timbre",
    "Нәзік / Delicate": "delicate soft timbre", "Резонансты / Resonant": "full resonant timbre",
    "Түтінді / Smoky": "smoky intimate timbre", "Мұрындық / Nasal": "light nasal cutting timbre",
    "Металл / Metallic": "metallic penetrating timbre", "Жібектей / Silky": "silky fluid timbre",
}
VOICE_PRESETS = {f"{register} · {texture}": f"{direction}, {TEXTURES[texture]}"
                 for register, direction in REGISTERS.items() for texture in TEXTURES}
VOICE_PRESETS["Instrumental / Дауыссыз"] = "instrumental only, no vocals"
DELIVERY = ["Legato / flowing phrases", "Staccato / short articulation", "Melisma / ornamented syllables", "Straight tone / no vibrato", "Gentle vibrato", "Wide expressive vibrato", "Whispered delivery", "Spoken word", "Fast rap flow", "Melodic rap", "Double-time flow", "Breathy intimate delivery", "Powerful belting", "Soft crooning", "Call and response", "Throat singing", "Yodeling", "Falsetto", "Vocal fry", "Growl", "Scream", "Traditional ornamentation"]

LANGUAGES = {
    "Бастапқы тілін сақтау": "preserve the source language",
    "Қазақша": "Kazakh", "Өзбекше": "Uzbek", "Қырғызша": "Kyrgyz", "Түрікше": "Turkish",
    "Әзербайжанша": "Azerbaijani", "Түрікменше": "Turkmen", "Ұйғырша": "Uyghur",
    "Татарша": "Tatar", "Башқұртша": "Bashkir", "Қарақалпақша": "Karakalpak",
    "Қырым татарша": "Crimean Tatar", "Ноғайша": "Nogai", "Құмықша": "Kumyk",
    "Қарашай-балқарша": "Karachay-Balkar", "Қарайымша": "Karaim", "Қырымшақша": "Krymchak",
    "Гагаузша": "Gagauz", "Хорасан түркіше": "Khorasani Turkic", "Қашқайша": "Qashqai",
    "Халажша": "Khalaj", "Саларша": "Salar", "Сары ұйғырша": "Western Yugur",
    "Чувашша": "Chuvash", "Саха / Якутша": "Sakha (Yakut)", "Долғанша": "Dolgan",
    "Тываша": "Tuvan", "Тофаларша": "Tofa", "Хакасша": "Khakas", "Шорша": "Shor",
    "Алтайша (оңтүстік)": "Southern Altai", "Алтайша (солтүстік)": "Northern Altai",
    "Чұлымша": "Chulym", "Телеутше": "Teleut", "Кумандинше": "Kumandin",
    "Тубаларша": "Tubalar", "Челканша": "Chelkan", "Фую қырғызша": "Fuyu Kyrgyz",
    "Іле түркіше": "Ili Turki", "Оңтүстік өзбекше": "Southern Uzbek",
    "Оңтүстік әзербайжанша": "South Azerbaijani", "Сібір татарша": "Siberian Tatar",
    "Ескі түркіше (тарихи)": "Old Turkic (historical)", "Шағатайша (тарихи)": "Chagatai (historical)",
    "Осман түрікше (тарихи)": "Ottoman Turkish (historical)",
    "English": "English", "Русский": "Russian", "العربية": "Arabic",
}
INSTRUMENTS = ["Dombra", "Kobyz", "Komuz", "Dutar", "Doira", "Baglama", "Tar", "Kamancha", "Darbuka", "Saz", "Qanun", "Ney", "Oud", "Accordion", "Jaw harp", "Morin khuur", "Acoustic guitar", "Electric guitar", "Nylon guitar", "Distorted guitar", "Bass guitar", "Upright bass", "808 bass", "Sub bass", "Analog synth", "FM synth", "Synth arpeggio", "Synth pad", "Piano", "Rhodes", "Wurlitzer", "Hammond organ", "Church organ", "Strings", "Solo violin", "Cello", "Harp", "Brass", "Trumpet", "Trombone", "French horn", "Saxophone", "Clarinet", "Flute", "Oboe", "Bassoon", "Drum kit", "Drum machine", "TR-808 drums", "TR-909 drums", "Trap hi-hats", "Claps", "Hand percussion", "Congas", "Bongos", "Shaker", "Tambourine", "Timpani", "Taiko", "Tabla", "Sitar", "Santur", "Marimba", "Vibraphone", "Kalimba", "Steel drum", "Glockenspiel", "Choir pad", "Sample chops", "Vinyl texture", "Field recording"]
AUTOTUNE = ["Auto / жанрға сай", "Off / natural uncorrected vocal", "Transparent pitch correction", "Light melodic autotune", "Strong robotic autotune", "Fast-retune trap autotune", "Formant-shifted vocal", "Vocoder", "Talkbox"]
REVERB = ["Auto / жанрға сай", "Dry / no reverb", "Small room reverb", "Studio room reverb", "Plate reverb", "Large hall reverb", "Cathedral reverb", "Spring reverb", "Shimmer reverb", "Gated reverb", "Dark short reverb"]
DELAY = ["Auto / жанрға сай", "Off / no delay", "Slapback echo", "Quarter-note delay", "Eighth-note delay", "Dotted-eighth delay", "Ping-pong stereo delay", "Tape echo", "Dub feedback echo", "Subtle vocal throw delay"]
PRODUCTION = ["Auto / жанрға сай", "Professional studio / polished radio-ready mix", "Clean modern digital studio", "Warm analog studio", "Vintage tape studio", "Intimate home studio", "Live concert recording", "Raw underground recording", "Lo-fi cassette recording", "Cinematic wide studio", "Acoustic live room", "Minimal dry close-mic studio"]
MIX_OPTIONS = {
    "Компрессия": ["Auto", "Natural dynamics", "Gentle glue compression", "Punchy parallel compression", "Heavy pumping compression", "Sidechain ducking"],
    "EQ / тон": ["Auto", "Warm low-mid body", "Bright airy top end", "Dark soft treble", "Clean balanced spectrum", "Mid-forward vocal presence", "Deep bass emphasis"],
    "Сатурация": ["Auto", "Clean / no saturation", "Subtle tape warmth", "Tube saturation", "Gritty distortion", "Bitcrushed texture"],
    "Стерео": ["Auto", "Intimate narrow stereo", "Wide stereo image", "Mono vintage image", "Centered lead with wide backing", "Immersive spacious image"],
    "Вокалдың микстегі орны": ["Auto", "Upfront close-mic vocal", "Vocal blended into instruments", "Dreamy distant vocal", "Dry centered lead", "Layered doubled lead"],
    "Бэк-вокал": ["Auto", "No backing vocals", "Subtle doubles", "Thirds and fifths harmony", "Wide choir backing", "Call-and-response backing", "Octave doubles", "Ad-libs and vocal chops"],
    "Динамика": ["Auto", "Steady energy", "Intimate verse / explosive chorus", "Gradual cinematic build", "Sparse verse / dense chorus", "Drop-focused contrast"],
}
STRUCTURES = ["Auto", "Verse–Chorus–Verse–Chorus–Bridge–Chorus–Outro", "Intro–Verse–Pre-Chorus–Chorus–Verse–Chorus–Outro", "Intro–Build–Drop–Breakdown–Build–Drop–Outro", "Verse–Hook–Verse–Hook–Bridge–Hook", "Through-composed / no repeated chorus", "Short intro–Verse–Chorus–Outro"]
