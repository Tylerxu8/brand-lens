# Week 6 Day 3

# Mini Quiz

1. In your own words, map a database table onto a python list of dicts. What plays the role of the list, the dict, and the dict's keys? What does the schema add that the Python list doesn't have?

- The list is the table which is the `pages`.

- Each dict is a row.

- Each key is a column.

- If the data is wrong, the schema will refuse to store it.

2. `pages` uses an auto-number `id` as its primary key, but `brands` uses `slug`. Why the different choices? What would go wrong if `pages` tried to use `title` as its primary key?

- They use different primay keys becasue `brands` refers to exaclty that one brand forever but `pages` can change in the future. 

3. Your seed data has the same brand name potentially relevant to many pages. Explain, using the words "foreign key" and "duplication", why the brand name lives in the `brands` table and not in each `pages` row.



4. A page has `description = ''`(empty string) and another has `description IS NULL`. What real-world difference does that capture? Which one would `WHERE description IS NULL` return?




5. Give one question about your data that is genuinely easier to asnwer with two SQL tables than with the old nested `results.json`, and say why it's easier.



