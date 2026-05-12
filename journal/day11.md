# Week 3 Day 2

# What I did

I split my `fetch_many.py` into three sperate files because in the future, the script is just going to get longer and longer, so I split them into seperate modules to make it more scannable.

The three split files are `fetch.py`, `parse.py`, and `runner.py`.

- `fetch.py` is for network calling 

- `parse.py` is for parsing the body of the URL

- `runner.py` is executing the code with `fetch.py` and `parse.py` imported.
 
# What I learned

I learned how to create split files and import those files into one main file that reads from `brands.yaml`, drives the loop, and writes the `reults.json`. 

Doing this is important because when you are writing a script that is really long, it is easier to structure everything seperatly rather than piling all the code into one main file. 

# What I fully don't understand

I still don't full understand `__name__ == "__main__"`

# Claude check-in

I didn't really use claude today because everything that I wrote was pretty straight forward and it followed the structure from week 2. 

# Why does `parse.py` not import requests, and why does `fetch.py` not import BeautifulSoup? What would go wrong if both files imported both libraries?

- `parse.py` doesn't require `requests` because `requests` is a tool that goes out to the internet and fetches webpages for you. `parse.py` is only there to parse the the bodys of the url in the `runner.py` script. 

- `fetch.py` doesn't require `BeautifulSoup` because `BeautifulSoup` is a parsing tool and `fetch.py` is only there for network calling and getting the status of the webpage.

- I don't think anything would happen because even if I were to import, I am not calling anything from the import in those scripts. 
