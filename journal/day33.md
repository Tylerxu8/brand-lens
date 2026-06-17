# Week 7 Day 4

# What I did

I started by making `summarize_brand` in `brief.py` more robust so that it handles failure better. Since the brief is data, I had to teach the schema about it in `db.py`. 

Then, I added a helper `set_brief` in `db.py`. This is doing two things. 

First, is it changing the existing row instead of inserting a new one which is the brand row. It is filling in its brief. Second, it is turing dict into a JSON string to store.

After all that, I created a script that runs the full loop. Read brand data from the db, summarize, and store the brief back.

To test the script, I tested it by mocking claude. 

# The (summary, error) contract

`summarize_brand` never raises because of the try/except block. When it fails, the summary is set to `None` and it will explain why it failed.

# Mocking Claude

I would say that the two are the same because they are both passing in real information but only getting out a fake response. 

# The two error-path test

Mocking is the only way to test these paths because these instances can't really happen all the time. So that is why we are testing to see how the code will handle the situation when it does accure.

# What I don't fully understand

I still don't fully understand `def fake_create(**kwargs)`. I don't really understand how `**kwargs` is working. 

