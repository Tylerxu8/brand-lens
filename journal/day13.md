# Week 3 Day 4

# What I did

Today, I used argparse which is a built in library in python that lets your script accept inputs directly from the terminal when the script is ran. 

I added command-line arguments in `runner.py` so the input, output, brand limit path can be passed in. 

# What I learned

Today, I learned what argparse is and what its for. Argparse lets you pass values in at runtime from the terminal making your script flexible and reusable without touching the code itself.

# What I fully don't understand

I still don't fully understand this section. I understand what I can do with argparse and I kind of understand the structure but I am still fuzy on why it is being used and when I will use it.

# Claude check-in 

I asked claude to break this down for me and explain bit by bit:

```python
parser = argparse.ArgumentParser(description="Greet someone.")
parser.add_argument("--name", "-n", default="world")
parser.add_argument("--loud", "-l", action="store_true")
args = parser.parse_args()
```

Just to understand more on what I am typing and doing. Claude was very helpful in breaking it down line by line and acutally explaining what it being done.

# If you only got to keep one of these flags - `--input`, `--output`, `--limit`, `--csv` - which would you keep, and why? (Think about which one you acutally reached for during testing.)

If I could keep one of these flags, it would be `--limit` because if I am researching 100 brands and I need to see the first 50, `--limit` is the best tool for that task. 