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

## Notes

**Two things to notice**

1. `tests/` lives next to your code, not inside it. `fetch.py`, `parse.py`, `runner.py`, `brands.yaml` stay at the root; tests get their own folder. The convention is so universal that pytest finds the directory automatically.

2. `__init__.py` is an empty file that marks `tests/` as a Python package. It lets your test files import from your project without import shenanigans.

**The AAA Pattern**

1. **Arrange.** Build the inputs. The `html` string is hand written so you know exactly what's in it.

2. **Act.** Call the function under test. (ex.`parse_page(html, url)`) is the only line that does real work. 

3. **Assert.** Check the output matches your expectation. One assertion is fine; many are fine. The point is to compare actual against expected. 



- A test does not `print` and then have you eyeball the output. The `assert` does the checking.

- A test does not `return` a value. pytest ignores return values - only assertions count.

- A test does not call your function with live network input. The `html` string was hand-crafted so you know what's in it.

- A test file is not run with `python test/test_parse.py`. You run `pytest` from the project root, and pytest does the discorvery and reporting.

