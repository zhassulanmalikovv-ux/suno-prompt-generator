# Suno AI Prompt Studio

Streamlit және Groq `openai/gpt-oss-20b` негізіндегі қосымша: өлең мәтінін немесе идеяны Suno AI үшін екі бөлек, көшіруге дайын нәтижеге айналдырады. Бұл ашық модель Groq-та орындалады; OpenAI API кілті қажет емес.

- **Style Prompt:** ағылшынша жанр, аспаптар, эмоция, дауыс және темпо; 120 символдан аспайды.
- **Structure Lyrics:** `[Verse 1]`, `[Chorus]`, `[Bridge]`, `[Outro]` және қажет болса `[Instrumental Drop]` тегтері бар өлең.
- **Translate lyrics to English:** мағынасын сақтайтын ағылшынша аударма.
- Әр нәтиже `st.code()` блогында стандартты Copy батырмасымен беріледі.
- Premium dark интерфейс: градиентті тақырып, PRO / AI Powered бейджі, glassmorphism карточкалар, неон батырма және мобильді экранға бейімделетін екі баған.
- 10 қазақша жанр: той, мұңды, лирика, халық әні, терме, дәстүрлі ән, эстрада, Q-Pop, рэп және этно-фьюжн; халықаралық жанрлар да сақталған.
- Телефонда бір баған, ықшам мәтін өрісі, 16 px қаріп, 44–48 px touch нысаналары және жеңілдетілген карточка эффектілері.

## Жергілікті іске қосу

Python 3.11 немесе 3.12 ұсынылады.

```bash
git clone https://github.com/zhassulanmalikovv-ux/suno-prompt-generator.git
cd suno-prompt-generator
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

`.streamlit/secrets.toml` файлын жасап, өз кілтіңізді қойыңыз:

```toml
GROQ_API_KEY = "your-groq-api-key"
```

```bash
streamlit run app.py
```

Кілтті [Groq Console](https://console.groq.com/keys) арқылы алыңыз. Ол тек `st.secrets["GROQ_API_KEY"]` арқылы оқылады. `.env` қолданылмайды; `python-dotenv` тәуелділігі бастапқы сұранысқа сай енгізілген. Құпия файлдар `.gitignore` ішінде.

## Streamlit Community Cloud-қа орналастыру

1. [Streamlit Community Cloud](https://share.streamlit.io/) жүйесіне GitHub аккаунтыңызбен кіріңіз.
2. **Create app** арқылы `zhassulanmalikovv-ux/suno-prompt-generator` репозиторийін, `main` тармағын және `app.py` файлын таңдаңыз.
3. **Advanced settings → Secrets** ішіне жоғарыдағы TOML форматымен нақты `GROQ_API_KEY` енгізіңіз. Python нұсқасын 3.11 немесе 3.12 таңдаңыз.
4. **Deploy** басыңыз. Тәуелділіктер `requirements.txt` арқылы орнатылады.

Нұсқаулық: [Streamlit deployment docs](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).

## Қолдану

Өлең не идея енгізіп, жанрды, көңіл-күйді, дауыс түрін және аударма опциясын таңдаңыз. **Generate Suno Prompt** басып, екі нәтижені Suno-ның **Style of Music** және **Lyrics** өрістеріне көшіріңіз. Аударма өшірілсе, өлеңнің бастапқы тілі сақталады; идеядан сол тілде жаңа өлең жазылады.

Нәтиже [Groq JSON Object Mode](https://console.groq.com/docs/structured-outputs#json-object-mode) арқылы алынады. Қосымша екі мәтіндік өрісті, 120 символ шегін және өлең тегтерін тексереді, сәйкес болмаса бір рет түзетуді сұрайды. API қатесі немесе толық емес нәтиже пайдаланушыға түсінікті хабарлама береді.

Генерация Groq аккаунтының API лимиттерін пайдаланады. Пайдаланушы енгізген мәтін Groq-қа жіберіледі. Нәтижелер тек ағымдағы Streamlit сессиясында сақталады.

## OpenAI-дан Groq-қа ауысу

Streamlit Cloud-та Secrets ішіндегі кілт атауын `GROQ_API_KEY` деп ауыстырып, нақты Groq кілтін енгізіңіз. `requirements.txt` енді `groq` SDK орнатады. Ескі `OPENAI_API_KEY` бұл қосымшаға қажет емес.
