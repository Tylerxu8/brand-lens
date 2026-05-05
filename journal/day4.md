# Week 1 day 4

# What I did

I started off by learning how to create list and loops. A list is an ordered collection of things written with square brackets. I also learned how to `.append` items onto an existing list, `enumerate`, and also how to filter the list and create a new filtered list.

Then I got into building the script that fetches from many pages. I tried out try/except but didn't really understand how it works exepct the fact that it is a defense code to handle errors.

# What's the difference between a list and a string? Give an example

So a list is a collection of items that can be different types of data like names and numbers.

A string is a sequence of characters to store textual data. 

## Example:

- String: 
```python
name = "hello world" 
```
- List: 
```python
my_list = [1, "hello", 4.20, false]
```

# What's one thing you wrote today that you don't fully understand?

```python
try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "(no title)"
        record["status"] = response.status_code
        record["title"] = title.strip()
        record["error"] = None
        successes += 1
        print(f"  -> {title.strip()}")
    except Exception as e:
        record["status"] = None
        record["title"] = None
        record["error"] = str(e)
        failure += 1
        print(f"  -> FAILED: {e}")
    results.append(record)
```

# What does try/except do and why did my script need it

So try/except is a defense code to handle errors if there are any. My script needed it because I had a URL in my .txt file that didn't exist. So without it, my whole script would crash, but with it, it will just log it as an error.

# How does today's script relate to the eventual capstone (a brand research tool)?

Today's script is very important in brand research because it is the first step into fetching data for brand research.
