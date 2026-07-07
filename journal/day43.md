# Week 9 Day 4

# What I did

I started off by writing the file that will create the index site for all my brands. I then made sure it worked by removing the `site/` directory and running my code to see if it will build the directory and show me the index for all my brands.

After that, I tested the renderers in my `tests` directory with pytest to see if everything is working properly without errors. I had a little trouble because `templates/brief.html` had a bug but I used claude and everything works perfectly and all tests are green.

# The four build steps

`build_site.py` is rebuilding the entire static site from the database into `site/`. 

The one thing reused from week 8 I believe is the main guard. The main guard lets `build_site.py` be both a script and a module tests can import without it triggering a full rebuild.

# Pure again

I skipped using `monkeypatch`. Since the renderers are pure, you hand it data and get a string, we didn't need to use `monekypatch` or fake anything.

# The href test

The exact link is worth a test of its own because the link is load bearing. If the slug-to-filename glue is wrong, every page on the site will 404.

# What I don't fully understand

I still don't fully understand what `shutil` is for and what it is doing. It breifly explained that it is a "shell utilites" module for file operations; `copy` does what `cp` did by hand yesterday. But I don't understand what that means.

