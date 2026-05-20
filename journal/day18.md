# Week 4 Day 3

# Mini Quiz

1. In a `git diff` output, what's the difference between a line starting with `-`, a line starting with `+`, and a line with no prefix?

- A line starting with `-` shows what is being removed, `+` shows what is being added, and a line with no prefix is not being changed at all.

2. The hunk header `@@ -10,5 +10,7 @@` - what do the four numbers mean?

- The four numbers are showing starting at the old file at line 10 at line 5 and starting at the new file at line 10 at line 7.

3. You've made changes to two files: `runner.py` (saved on disk, not staged) and `parse.py` (staged with git add). Which command shows you `runner.py`'s changes? Which shows you `parses.py`'s? Which shows both?

- To show `runner.py` do `git diff runner.py` and for `parse.py` do `git diff parse.py`. To show both do `git diff`.

4. You ask Claude Code to add a `--verbose` flag. The proposed diff is 80 lines, touches three files, and includes deletions in a function unrelated to logging. Name two specific things you'd ask before reviewing futher.

- First I would ask to explain the diff and why it did that, then I would telll Claude to just focus on the original change.

5. Why is a `-` line in a diff the highest-risk part to review?

- The `-` line in a diff is the highest risk part to review because if you are using claude code and it just makes a bunch of changes without reviewing, it can create bugs and break the code.

# What I don't fully understand

I undesrstand most of everything that I learned today and I am confiedent that I can explain what I learned today to someone that doesn't know what a diff is.

# What I'll watch for tommorrow

I'll check what diffs claude has made and if claude changed any files that I didn't mention. 

## Notes

`git diff`

shows working tree vs. staging area - what you've changed but haven't staged. 

`git diff --cached` or `git diff --staged`

shows staging area vs. last commit - what you've staged but haven't commited.

`git diff HEAD`

shows working tree vs. last commit - everything that's changed since the last commit, staged or not. 

**Dif** 

Shows the difference between two versions of a file: what was there before, what's there now, what changed. 

- The `-` line is the old version (deleted).

- The `+` line is the new version (added).

- Lines with neither prefix are context - unchanged lines around the change, shown so you can see where the change sits. 

A diff isn't just for git but any tools way of saying whats changed. Claude code shows diffs the same way before applying edits.

When you type git diff after changing something you will see the changes before pushing your code. 

- `a/` is the old version

- `b/` is the new version

- `@@ -40,7 +40,7 @@ def ,main()` is a hunk header, "starting at line 40 of the old file, 7 lines; starting at line 40 of the new file, 7 lines." 

Lines starting with `-` are removed, `+` are added.

`git checkout runner.py` throws away unstaged changes to that file.

The general rule is if you can't say why a `+` or `-` line is there, don't accept it.