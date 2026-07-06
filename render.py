from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

env = Environment(
	loader=FileSystemLoader("templates"),
	autoescape=select_autoescape(["html"]),
)

def write_page(slug, html):
	os.makedirs("site", exist_ok=True)
	path = os.path.join("site", f"{slug}.html")
	with open(path, "w", encoding="utf-8") as f:
		f.write(html)
	return path

def render_brief(context):
	"""Turn a context dict into the rendered markdown string."""
	template = env.get_template("brief.md")
	return template.render(**context)

def render_brief_html(context):
	"""Turn a context dict into the rendered HTML string. Pure - no I/O."""
	template = env.get_template("brief.html")
	return template.render(**context)

def write_brief(slug, markdown):
	os.makedirs("briefs", exist_ok=True)
	path = os.path.join("briefs", f"{slug}.md")
	with open(path, "w", encoding="utf-8") as f:
		f.write(markdown)
	return path

def render_index(brands, generated_at):
	"""Render the index page listing all brands. Pure - no I/O"""
	template = env.get_template("index.html")
	return template.render(brands=brands, generated_at=generated_at)