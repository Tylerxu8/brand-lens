from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader("templates"))


def render_brief(context):
	"""Turn a context dict into the rendered markdown string."""
	template = env.get_template("brief.md")
	return template.render(**context)

def write_brief(slug, markdown):
	os.makedirs("briefs", exist_ok=True)
	path = os.path.join("briefs", f"{slug}.md")
	with open(path, "w", encoding="utf-8") as f:
		f.write(markdown)
	return path