# Week 6 Day 1

# What I did

Today I created a database using sqlite. Sqlite is a database that lives in a single file. 

I also defined the schema. A schema is the shape of the data: what tables exist, and what columns each table has. 

# My SELECT predictions

I guessed that the laneige description would come back empty since I stored it as `None` and my guess was correct.

# Schema in my words

The difference between `brands` and `pages` is that `brands` is tiny. One row per brand. Where as the `pages` section is doing most of the work like parsing the page and producing `status` and `error`. A `title` allows `NULL` because some pages don't have `titles` but every page has a `url`.

# What I don't fully understand

I still don't fully understand the schema part of this section. I get it that it is like `json` and `csv` but for those, I didn't have to write a seperate file of code, just one line at the bottom of my code, but for a schema, I have to write a whole seperate file?