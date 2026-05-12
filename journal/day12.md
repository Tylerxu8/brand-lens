# Week 3 day 3

# Mini Quiz

1. What's the difference between `open(f, "w")` and `open(f, "a")`? Which one would silently destroy your results file?

- `open(f, "w")` open's the file 'f' and rewrites the entire file with new data. 

- `open(f, "a")` open's the file 'f' and appends new data when you rerun the script.

2. You run `python3 runner.py` from `~/dev/brand-lens`. The script reads `"brand.yaml`. Predict what happens if you `cd ~` and run `python3 dev/brand-lens/runner.py`. Where does Python look for `brands.yaml`?

- If you were to run that, the script would crash because python looks for `brands.yaml` in whatever directory it was ran from and since `~` is the home directory, and `brands.yaml` isn't in the home directory it would crash. 

3. Why is the `with` form of file handling preferred over manual `open()` and `close()`?

- `with` is prederred over `open()` and `close()` because the `with` function automatically closes the file after it is done being used and if you were to manually open the file and forget to close it, the file will stay open in the background. 

4. WHat is `UTF-8`, in plain english?

- `UTF-8` is a character encoder for different almost every language. Python already has it embeded into the system and it is used to turn bytes into text. 

5. If `runner.py` uses `from fetch import fetch_one`, where does python look for `fetch.py`?

- Python looks for `fetch.py` in the directory it lives in and if it isn't in the same directory as `runner.py`, the script would fail. 


# What I don't fully understand

I don't quite understand the paths part yet. I understand that it depends on what directory you are running the script from but not the `pathlib` part.


# How my mental model changed

Before today, I didn't really understand how file I/O was working but after today and studying on my own, I now know how import it is to use `with` instead of manually opening and closing each file. Especailly later in the future. If I were to open a file for my script and forget to close it after, it would waste resources. But the `with` string automatically opens and closes for me wihtout worrying about wasting resoruces and having too many files open in the background. 
