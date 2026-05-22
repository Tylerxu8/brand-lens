# 10 Questions I couldn't answer right now wihout looking something up or asking someone

1. This is from Week 2 day 1, I still wouldn't be able to explain what a list comprehension is and what its doing. **(Vincent)**

2. This is for the layers of a website, I still don't understand what the TLS is. **(Claude)**

3. When fetching the urls I don't understand why we need to get the canonical tag and the h1 tag.

```python
record["canonical"] = canonical_tag["href"] if canonical_tag else None
```

And I don't understand the `href` part.
**(Claude)**

4. `results.sort(key=lambda r: (r["error"] is not None, (r["title"] or "").lower()))` in this line, I don't know what the `lambda` part is for.**(Claude)**

5. At the end of my code in `runner.py`, there is a line:

```python
if __name__ == "__main__":
	main()
```

I kind of understand it. I don't know if this is correct but if you are importing from `runner.py`, to only run the main function from `runner.py`?**(Vincent)**

6. What is the difference between using `git diff --cached` and `git diff --staged` because in the explanation from that lesson, it says it does the same thing. **(Claude)**

7. I don't understand the difference between `git diff --staged` and `git diff HEAD`. Isn't it showing the same thing bascially? **(Claude)**

8. Where does the conversation store when I am using Claude code? And if my computer were to reset while I'm using Claude code, will it mess up my code that Claude is running, and how can I retrieve the converstaion? **(Claude)**

9. `index 1a2b3c4..5d6e7f8 100644` this is git's internal hashes for the old and new content, I don't know what it says or what I am looking at. **(Vincent)**