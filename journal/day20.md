# Week 4 Day 5 (Week 4 retospective)

# What I shipped this week

I didn't really ship much this week. I mainly focused on setting up Claude Code and getting used to using Claude..

On day 4 is when I actually used Claude to implement a change into my `runner.py` file which was to add the `--brand` flag.

# How my relationship to Claude changed

In my experince with Claude on the browser and Claude code is so different. 

Claude on the browser can only make suggestions and doesn't really work well unless you screen shot, or give it your whole code, but Claude code can take over your computer and make any changes you want it to.

This can be scary but once you get used to reading its outputs and asking the right questions, Claude can be a very helpful tool.

# A specific moment I broke a rule

I didn't break any rules because at first, I was very confused on how to use Claude so I read everything that it was outputing and didn't accept anything until I understood everyhting it was changing.

# Where the diff review reflex felt strongest

The diff review felt the strongest when I asked Claude to make its first changes to my `runner.py` file and I instantly knew where to look for the changes.

# Where the diff review reflex felt weakest

I still struggled a bit on the hunk header part but I asked Claude to explain that part and resovled my issue right away.

# My top 3 questions from W4D5_questions.md

1. At the end of my code in `runner.py`, there is a line:

```python
if __name__ == "__main__":
	main()
```

I kind of understand it. I don't know if this is correct but if you are importing from `runner.py`, to only run the main function from `runner.py`?

2. What is the difference between using `git diff --cached` and `git diff --staged` because in the explanation from that lesson, it says it does the same thing.

3. `results.sort(key=lambda r: (r["error"] is not None, (r["title"] or "").lower()))` in this line, I don't know what the `lambda` part is for.

