# Day 4

# What I did

First I started by creating a scratch file to mess around in
- 'touch scratch.py'
- open -a "Sublime Text" scratch.py

Then in Sublime:

- brands = ["Innisfree", "Laneige", "COSRX", "Sulwhasoo"]

- print(brands)
- print(len(brands))
- print(brands[0])
- print(brands[-1])

- for brand in brands:
    - print("checking:", brand)

This prints the brands at the top, len() shows how many items are in the list, brands[0] starts the count from 0 and brands[-1] stops it at the last listed item

# Experiment

## To add something to the list use:
- 'brands.append("example")'
- print(brands)

## To numerate the list use:

- 'for i, brand in enumerate(brands):'
- 	'print(i, brand)'

## To give a list of the short names use:

- 'short_names = [b for b in brands if len(b) < #]'
- 'print(short_names)'

This means the list of b for each b is brands, where the length of b is less than #.

# Planing the code before writing the code

You can create a .py file and write in a plan before writing in code to plan out what is going to happen.

- touch fetch_many.py
- oepn -a "Sublime Text" fetch_many.py

In this file I put the plan in before the real code:

```python
# fetch_many.py
# Read a list of URLs from urls.txt (one URL per line)
# For each URL:
#   - fetch it
#   - extract the title
#   - record the result (URL, title, status, timestamp)
#   - if anything goes wrong, record the error instead of crashing
# Write all results to results.json (one JSON object per line)
# Print a short summary at the end: how many succeeded, how many failed
```
Then I built the input file that stores where the data can be fetched from.

- touch urls.txt
- open -a "Sublime Text" urls.txt

I put about 7 urls and one that didn't work.

To view the file, you can run 'cat urls.txt' which will list everything in that file

# Now building the script

When writing the script, write it in increments to get one part working before adding more parts to the code.

In 'fetch_many.py' below the plan,

- 'with open("urls.txt") as f:'
- 	'urls = [line.strip() for line in f if line.strip()]'

- 'print(f"loaded {len(urls)} urls")'
- 'for url in urls:'
- 	'print(" -", url)'

When you run this script a count and the URLs are listed.

The:

- 'line.strip()' removes the trailing newlines and spaces.

- 'if line.strip()' skips blank lines.

- 'f"..."' is an f string - pythons way of inserting variables into text


