# Week 3 Day 5

# What I shipped this week

1. I refactored my `fetch_many.py` to read from `brands.yaml` and shipped both files.

2. Then I spilt up my `fetch_many.py` file into seperate modules - `fetch.py`, `parse.py`, `runner.py`

3. I added argparse to `runner.py` just as a parameter just in case I need specific data in the future. I also cleaned up the csv part.

# Where I struggled in the review



# What I don't fully understand

I still don't fully understand the argparse parameter and when I would be using them in the future. 

# How I used claude this week

- Yes I never asked claude to write the code for me, whenever I was having trouble understanding something, I aasked claude to explain it in details. 

- I ran everything myself and if an error popped up, I tried to fix the issue my self before asking claude what was wrong with the code.

- Claude has been very helpful in explaing step by step on what each line of code is doing and what it means. 

# What I want to learn next week

I am still a little fuzzy on the argparse section so I want to learn a little bit more on that and situations where I would need to use it.


# Prep checklist

1. **Cold Start**

To get `runner.py --limit 1` to run, you need to add a `parse.add_argument` with `"--limit"`, `type=int`, `default=None`. When you run `runner.py --limit 1` in the terminal it should limit the search to the first brand on the list. 

2. **The Shape**

- `fetch.py` is getting the HTTP 

- `parse.py` is parsing the html so that it is readable

- `runner.py` is importing from those two and orchestrating everything to get the parsed html and url into a clean csv list and .json file. 

3. **The Data Flow**



4. **The Argparse Choices**

These flags exist as a parameter so that incase you want a different result, you can ask for different results instead of hard coding it into the script. Without these parameters, you would have to go into the script and hard code what ever command you would like to run. 

5. **The Hardest Line**

```python
if __name__ == "__main__":
	main()
```
Claude explained it well for me to understand. So sum it all up, the code is there just incase I were to import from `runner.py`, `from runner import fetch_one`, if I didn't have that line of code, it would run both `fetch_one` and `main()` instead of just `fetch_one`. 