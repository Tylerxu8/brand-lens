# Week 1 day 3

# What I did today

First I set up a Virtual environment which is a "per project" sandbox for python packages. Then , I created a `.gitignore` file to contain the `/vnev` file so git doesn't track it. After, I installed my first package which was `requests` using `pip`.

I also fetched my first webpage and learned how to extract the title using `BeautifulSoup` which was pretty cool.

# What I don't fully understand

```python
soup = BeautifulSoup(response.text, "html.parser")
```

## What does a virtrual environment do and why does it exist?

A virtual environment exists because installing a bunch of libraries onto your computer takes up a lot of space and is a mess so creating a virtual environment helps manage your projects.

## What happens when you run 'requests.get(url)'?

To my knowledge, this is asking to get the url from the request library 

## What's the difference between 'response.text' and 'soup.title.string'?

`response.text` shows the actual title

and 

`soup.title.string` is a defense code because some pages don't have titles so without the guard, the script will crash.

## Name the line from 'fetch.py' and what part you can't explain

```python
with open("result.json", "a") as f:
	f.write(json.dumps(result) + "\n")
```

This is what I couldn't write from scratch and I don't really understand what the second line.