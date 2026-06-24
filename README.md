# Brand Lens

Brand Lens evaluates how a Korean brand presents itself to the US market.
It fetches a brand's US web pages, extracts the fields that signal positioning
(title, meta description, og:title, h1, canonical URL), stores them in a SQLite
database, asks Claude to turn them into a structured brief, and renders one
markdown brief per brand.

## Setup

    git clone <your repo url>
    cd brand-lens
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    cp .env.example .env          # then add your ANTHROPIC_API_KEY

## Usage

    python3 runner.py             # fetch + parse + store pages in the database
    python3 summarize_all.py      # generate a brief per brand (calls the LLM)
    python3 generate_briefs.py    # render briefs/<brand>.md from the database

Briefs are written to briefs/ (gitignored — regenerate any time).

## Layout

- runner.py      — orchestrates fetch → parse → store
- fetch.py       — fetch a page (network)
- parse.py       — HTML → fields
- db.py          — all SQLite access
- brief.py       — LLM summarization
- render.py      — context → markdown
- generate_briefs.py — db → rendered briefs/
- templates/     — jinja2 templates
- tests/         — pytest suite