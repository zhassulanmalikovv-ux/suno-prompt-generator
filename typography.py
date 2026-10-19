"""Self-hosted user-supplied display and handwriting fonts."""
import base64
from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=1)
def font_faces() -> str:
    root = Path(__file__).resolve().parent / "assets" / "fonts"
    rules = []
    for name, filename, weight in [("Smooz", "Smooz-Regular.woff2", 400)]:
        data = base64.b64encode((root / filename).read_bytes()).decode("ascii")
        rules.append(f"@font-face{{font-family:'{name}';src:url(data:font/woff2;base64,{data}) format('woff2');font-weight:{weight};font-style:normal;font-display:swap;}}")
    return "\n".join(rules)


def studio_font_css() -> str:
    return "<style>" + font_faces() + """
.stApp h1, .stApp h2, .stApp h3, .studio-title, .studio-brand, .studio-heading {
    font-family:'Smooz','Segoe UI',sans-serif!important; font-weight:400!important;
    font-style:normal!important; letter-spacing:0!important; line-height:1.25!important;
}
.studio-title {font-size:clamp(1.8rem,2.7vw,2.7rem)!important;padding:.05em 0!important;margin:.2rem 0 .35rem!important;overflow:visible;}
.studio-brand {font-size:1.35rem!important;}
.studio-heading {font-size:1.35rem!important;}
.st-key-preset_library h3 {font-size:1.7rem!important;}
@media(max-width:768px) {
 .studio-title {font-size:clamp(1.7rem,6vw,2.2rem)!important;overflow-wrap:anywhere;}
 .studio-brand {font-size:1.15rem!important;}
 .studio-topline {flex-wrap:wrap;}
 [role="tab"] {font-size:.85rem!important;}
}
</style>"""
