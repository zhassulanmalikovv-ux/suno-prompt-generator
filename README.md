# Suno AI Prompt Generator

Streamlit және OpenAI `gpt-4o-mini` негізіндегі қосымша: өлең мәтінін немесе идеяны Suno AI үшін екі бөлек, көшіруге дайын нәтижеге айналдырады.

- **Style Prompt:** ағылшынша жанр, аспаптар, эмоция, дауыс және темпо; 120 символдан аспайды.
- **Structure Lyrics:** `[Verse 1]`, `[Chorus]`, `[Bridge]`, `[Outro]` және қажет болса `[Instrumental Drop]` тегтері бар өлең.
- **Translate lyrics to English:** мағынасын сақтайтын ағылшынша аударма.
- Әр нәтиже `st.code()` блогында стандартты Copy батырмасымен беріледі.

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
OPENAI_API_KEY = "your-openai-api-key"
```

```bash
streamlit run app.py
```

Кілт тек `st.secrets["OPENAI_API_KEY"]` арқылы оқылады. `.env` қолданылмайды; `python-dotenv` тәуелділігі сұранысқа сай енгізілген. Құпия файлдар `.gitignore` ішінде.

## Streamlit Community Cloud-қа орналастыру

1. [Streamlit Community Cloud](https://share.streamlit.io/) жүйесіне GitHub аккаунтыңызбен кіріңіз.
2. **Create app** арқылы `zhassulanmalikovv-ux/suno-prompt-generator` репозиторийін, `main` тармағын және `app.py` файлын таңдаңыз.
3. **Advanced settings → Secrets** ішіне жоғарыдағы TOML форматымен нақты `OPENAI_API_KEY` енгізіңіз. Python нұсқасын 3.11 немесе 3.12 таңдаңыз.
4. **Deploy** басыңыз. Тәуелділіктер `requirements.txt` арқылы орнатылады.

Нұсқаулық: [Streamlit deployment docs](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).

## Қолдану

Өлең не идея енгізіп, жанрды, көңіл-күйді, дауыс түрін және аударма опциясын таңдаңыз. **Generate Suno Prompt** басып, екі нәтижені Suno-ның **Style of Music** және **Lyrics** өрістеріне көшіріңіз. Аударма өшірілсе, өлеңнің бастапқы тілі сақталады; идеядан сол тілде жаңа өлең жазылады.

Нәтиженің форматы [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) арқылы беріледі. Қосымша 120 символ шегін және өлең тегтерін тексереді, сәйкес болмаса бір рет түзетуді сұрайды. API қатесі немесе толық емес нәтиже пайдаланушыға түсінікті хабарлама береді.

Генерация OpenAI API балансын пайдаланады. Пайдаланушы енгізген мәтін OpenAI-ға жіберіледі. Нәтижелер тек ағымдағы Streamlit сессиясында сақталады.
