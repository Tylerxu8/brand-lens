# Week 6 Day 4

# What I did

The first thing I did today was fix a previous problem that occured from last week. The problem was that when I would run the test again on a new day, it didn't rewrite the test so it would fail since it was trying to duplicate the information.

The fix was changing `insert_page` to `upsert_page` and changing the execution line to `INSERT OR REPLACE`.

I then used Claude Code to add a new flag to my `runner.py` file. 

That flag is added to connect those two pipelines so that the data is being written to a database.

# The re-run problem

This showed that the Integrity key was working. Since I already assigned `x` to an `id` it couldn't be rewritten so I had to use `upsert_pages` and `INSERT OR REPLACE` to fix the error.

# The in-memory database

We tested against `:memory:` instead of `brands_lens.db` because that creates a database that lives only in memory. Since side-effectful code is harder to test, this substitues a fake for the real thing. 

# Yield vs return in a fixture

The `yield` code is there as a fixture version of `open/close`. It is doing two things, everything above the `yield` is a setup and the yielded value is what the test recives. After, is the teardown which pytest runs automatically pass or fail. 

# What I don't fully understand

I don't fully understand the connection life cycle in `main()`. It doesn't really make sense to me on how it is working and why I am using the `--limit` flag instead of the `--db` flag even though that is the new flag I added.

