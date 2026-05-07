# Week 2 day 4

# What I did

I looked up a website and viewed the page source to take a peek at the whole HTML. 

I then worked on my `fetch_many.py` file to extract certain data from my URLs like the description, og title and, the canonical URL. 

I didn't really understand what I was doing in the beginning but after seeing the results in `results.json` it became more clear as to why I was retriving specific information.

# What I learned

I learned how retrieve the meta description, og title, canonical URL, and the h1 tag. 

All these information can be seen by viewing the page source on a website and I learned how to extract each piece of information to better understand that data.

# What I fully don't understand

I sitll don't really under what the canonical URL and h1 tag is for. Also, I still don't really understand what `href` is.

```python
canonical_tag = soup.find("link", attrs={"rel": "canonical"})
record["canonical"] = canonical_tag["href"] if canonical_tag else None
```
```python
h1_tag = soup.find("h1")
record["h1"] = h1_tag.get_text(strip=True) if h1_tag else None
```

# Claude Check-in

I asked claude whaat `href` stands for and what is it. `href` is the attribute that holds the destination URL.

The simple version is if there is a door, `href` is the address written on the door. So `href` is where you end up.

# Of the four new fields you extracted today, which would you trust most as a signal of how a brand presents itself, and why?

I would look for the description field because the description field tells you what that brand is doing and gives you the description for it.