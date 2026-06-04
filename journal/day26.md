# Week 6 Day 2

# My query predictions

`SELECT url, title FROM pages;`

- I think this will get the url and titles from the brands in pages.

- EDIT: This pulled all the urls in pages.

`SELECT url, title FROM pages WHERE brand_slug = 'innisfree;`

- I think this will pull the url and title from `innisfree`

`SELECT url FROM pages WHERE status = 200;`

- This will pull the urls with only a status of 200 and exclude everything else

`SELECT url FROM pages WHERE status != 200;`

- Im not really sure what `!=` does.

- EDIT: `!=` is excluding everything with a status code of `200` so only the urls with a different status code is pulled.

`SELECT url FROM pages WHERE error IS NOT NULL;`

- This will pull the urls with no errors

- EDIT: I think this pulls the urls with errors, but since my pages didn't have any errors, nothing was pulled.

# NULL

Im not sure if I fully understand this correctly but it is because `NULL` means `unkown` so `IS` is asking to match all the ones that are `None` but `=` is `unkown = unkown`?

# WHERE vs GROUP BY

`WHERE` is filtering individual rows and `GROUP BY` is summaraizing groups of them.

# What I don't fully understand

I still don't fully understand the difference between `WHERE` and `GROUP BY`, also why I can't use `WHERE description = NULL`.