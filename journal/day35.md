# Week 8 Day 1

# What I did

I started off by creating a template to use for the data I collect. The template that I created lives in the `templates` directory. I also created a `brief.md` file to produce a file that I can read and print.

I then rendered it with `render_brief` and tested it with `try_render.py`. I inserted data from a brand that I chose and ran the script. When run, it outputs the template with the inserted data from `try_render.py`. 

After I made sure the test worked, I wrote the produced data to a file.

When I run `subl briefs/(name.md)` the file opens up in a text version instead of it being shown in the terminal.

# My render prediction

I think when I run the script, it will print how the template would look like but without all the unnessecary things like `{% if %}`.

Edit: 

After printing, I was write. It filled in all the gaps and mapped out all the keys to its values. 

# Why a template instead of a f-string

A template is better than doing f-string because if you are doing a whole report with headings and a bunch of other data, it can make it unreadable. A template is a file that looks like the finished document, and the code just hands the data over to the template and fills in the gaps.

# render_brief vs write_brief

`write_brief` is the one with a side effect and it is that it touches the disk. `render_brief` is a pure function and is only building the string. 

This matters because if you only want to test without touching the disk, you can use `render_brief` instead of `write_brief`.

# What I don't fully understand

Today's lesson was pretty straight forward and I understand everything for the most part. I just don't remember what `import os` does. 

