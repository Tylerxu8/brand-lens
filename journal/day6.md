# Week 2 Day 6


## What I did today

These are functions:

 `print(...)`, `len(brands)`, `requests.get(url)`, or `int(number)`

 A function is a named, reausable piece of code that takes inputs and returns outputs.

 I practied on functions and learned why functions exist. 

 There are 2 reasons as to why they exist.

 1. Reuse. If the same code is running in two places, you can change it once instead of twice.

 2. Clarity. A well named function can turn a 12 line block into a single line.

 I then I refactored my `fetch_many.py` file so that the `for` loop is now 4 lines of intent/readable.


 ## What I learned

 I learned what Dictionarys are and what they do. A dict maps keys to values. 

 For example:

 ```python
 brand = {
 	"name" : "Nike",
 	"founded": 1972,
 	"country" : "USA"
 }
```
The dictionary is created using `{}` and `""`, the key in the second line is `"name"` and the value is `"Nike"`. For integers you do not need `""` because if you put an integer in `""` it is telling python to treat whatevers inside those quotes as a text instead of actual numbers. 


## What I fully don't understand

```python
 successes = sum(1 for r in results if not r["error"])
failure = len(results) - successes
print(f"\ndone. {successes} succeeded, {failure} failed.")
```

```python
def fetch_one(url):
    record = {
        "url": url,
        "fetched_at": datetime.now().isoformat(),
        "status": None,
        "title": None,
        "error": None,
    }
```


### Claude Check-in

I asked Claude to see if my explanation to "what a dicationary was" correct or not. It explained it very well and I also learned something from it. Dictionarys are created not with just `{}` but also using `""` for the keys and values.

I did ask a follow up question "why don't integers require quotes?"

It explained by saying that if you were to put integers into quotes it will tell python to treat whatevers inside those quotes as a text instead of actual numbers. 

For example:

`"1972" + 1`  # will give an error saying you can't add numbers to a string

`1972 + 1`  # works and gives you 1973


I also asked claude what it means to refactor something and it means to rewrite the code to be cleaner or better organized without changing what that code actually does.


## If a friend asked you "what's the difference between a list and a dict? - answer in 2 sentences, no AI."

The difference between a list and a dict is that a list is a collection of itmes that can be different types of data like names and numbers. A dict is what maps a key to values. So a list is made by using `[]` and a dict is made by using `{}` and `"key" : "value"`.