# Week 2 Day 5

# What I did this week

**Day 1** 
I worked on my fetch.py file and learned how to parse a specific website using BeautifulSoup 4. I then used claude to get explanation on certain lines of code

**Day 2** 
I learned how to convert my long for loop into a function so its cleaner and dictionarys into fetch_many.py.

**Day 3**
I didn't do any new coding this day, I learned the layers of a web, status codes, and what `response` is.

**Day 4**
For day 4 we got into richer parsing. I extracted the description, og:title, canonical URl, and the h1 tag for the URLs in my urls.txt file.

**Day 5**
Today I learned how to get a CVS output. CVS is great for looking at data through a speadsheet and not python. I also learned how to sort the list using `results.sort` and `lambda`.

# How is my work different now than at the end of Week 1?

I feel that I improved a lot in being able to actually read the code and know what each line means. I still struggle with actually writing code from scratch but I am a little more confident than Week 1 in reading the code. 

# What I don't fully understand

```python
results.sort(key=lambda r: (r["error"] is not None, (r["title"] or "").lower()))
```

I don't fully understand the `r["error"] is not None, (r["title"] or "").lower()`

I looked up what a tuple is but I still don't fully understand what it means.

# How I used Claude this week

**Rule 1**
Yes, I followed rule 1 and I didn't ask claude to write any of my code and I wrote everything myself.

**Rule 2**
Yes, I made sure my code actually worked in my terminal and I didn't ask claude to run any of my code, only to check errors.

Claude was very helpful in figuring out mistakes and when asking about certain python words like `href`. Claude it also very helpful when asking what certain lines of code do.

# How fetch_many.py connects to Brand Lens

`fetch_many.py` is very helpul and connects to brand research because with this script, I am pooling a bunch of websites from different places and countrys to research more about the brand, their description, and if the website is actually real or not.