# Week 8 Day 3

# Mini Quiz

1. Define "separation of concerns" in one sentence, then give two examples form your own brand-lens code (not the ones spelled out above if you can avoid it)

So "separation of concerns" is when you break up one big file of code into separate files that do its own thing. For example, the `brief.md`is separate from `generate_brief.md`because `brief.md` is only the template.

2. A teammate proposes a function `fetch_parse_and_store(url)` that does all three. Using today's principle, what's the objection? Name on concreate thing that gets harder.

The objection is that we should be spliting those fuctions so that when we get an error, we will know where the error is coming from. 

If we keep it all in one function, later down the line, it can get harder and harder to find the bug.

3. Three of these belong in git and three don't: `parse.py`, `.env`, `brands.yaml`, `brand_lens.db`, `templates/brief.md`, `briefs/`. Sort them, and state the rule that decides.

Git: `brands.yaml`, `parse.py` `templates/brief.md`

.gitignore: `.env`, `brand_lens.db`, `briefs/`

`.env` has my api key in it so it has to be ignored.

`brand_lens.db` because it is a regenerable output like `briefs/`

4. You clone a friend's Python project and `python main.py` raises `ModuleNotFoundError`. What's almost certainly missing, what file should the project have included, and what command fixes it?

So the file that the project is missing is the `requirements.txt` file and the simple command that fixes this is `pip install -r requirements.txt`.

5. Why pin a version (`jinja2==3.1.4`) instead of leaving it open (`jinja2`)? Give the failure that pinning prevents.

So pining the version instead of leaving it open is better because when the project was made, that is the version that it was run on, and libraries always update so the behavior can be different a year from now. 

# What I don't fully understand

For today's lesson, I understood everything and I feel confident in being able to explain all of this to a person that doesn't know anything about this topic.

# What I'll do tomorrow

The dependencies that belong in `requirements.txt` are the libraries used for this project. 

I think testing `render_brief` will be easy becuase it doesn't have side effects? Im not too sure on my answer on this one.
