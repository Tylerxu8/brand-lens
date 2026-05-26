# Week 5 Day 1

# What I did

Today, I installed pytest, which is a third party library, to see if my test codes work in my terminal.

In my test file, I imported from `parse.py` to test if the `parse_page` part of my code had any errors or not.

I first tried `pytest` without implementing bugs into my code and my test results came back positive.

Once I implemeneted a bug into my `parse.py` code, my test result came back negative. 

# The green-red-green cycle

In the failure message, it shows that somewhere in the code, the assertion didn't pass so there was an error. The test is asserting from `record["title"]`, so I can check in my `parse.py` for that line.

# The AAA shape

**Arrange**

Builds the input. In my test file, I wrote the html string so I know what is in it.

**Act**

This is what is actually doing the work. This is calling from `parse_page` in my test file from the import `parse.py`.

**Assert**

This is where the test is happeneing to see if my output matches what I am expecting.

# What I don't fully understand

I still don't fully understand the AAA shape. I understand the `Assert` and `Act` part but not the `arrange` part. 

I would love if there were a lesson just for the AAA shape.

