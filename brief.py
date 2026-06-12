import json

from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

SYSTEM = (
    "You are a brand analyst evaluating how a Korean brand presents itself "
    "to the US market, based only on data scraped from its US website. "
    "Respond with ONLY a JSON object — no markdown fences, no prose before "
    "or after."
)


def build_prompt(brand_name, pages):
    lines = [f"Brand: {brand_name}", "", "Scraped pages:"]
    for p in pages:
        lines.append(f"- url: {p['url']}")
        lines.append(f"  title: {p['title']}")
        lines.append(f"  meta description: {p['description']}")
        lines.append(f"  og:title: {p['og_title']}")
        lines.append(f"  h1: {p['h1']}")
        lines.append(f"  canonical: {p['canonical']}")
    lines.append("")
    lines.append(
        "Return a JSON object with these keys:\n"
        '  "value_proposition": one sentence, the brand\'s pitch as the data '
        "suggests it (use the meta description and h1).\n"
        '  "messaging_consistency": one sentence on whether title, og:title, '
        "and h1 tell a consistent story.\n"
        '  "us_presence_signal": one sentence on what the canonical URLs '
        "suggest about US-market commitment.\n"
        '  "confidence": one of "low", "medium", "high" — how much the scraped '
        "data actually supports your read."
    )
    return "\n".join(lines)


def summarize_brand(brand_name, pages):
    prompt = build_prompt(brand_name, pages)
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=500,
        system=SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = message.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(raw)