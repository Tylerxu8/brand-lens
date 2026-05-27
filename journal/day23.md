# Week 5 Day 3

# Mini-quiz

1. In your own words, what makes `parse_page` easier to test than `fetch_one`? Use the words "pure" and "side effect" in your answer.

- `parse_page` is easier to test than `fetch_one` because `parse_page` is pure and `fetch_one` has side effects. `parse_page` gives the same output as the input and `fetch_one` sends an HTTP request which is a side effect.

2. Look at `process_url(url)` in `runner.py`. Is it a unit test target, an integration test target, or an end to end test target? Why?

- I think that `process_url(url)` is an integration test target because it is importing from `fetch_one` and `parse_page` so its testing different places to see if the pieces fit together.

3. You wrote `test_parse_page_returns_none_when_description_missing` on D2. Suppose tomorrow you change `parse.py` so that a missing description returns the empty string `""` instead of `None`. Does that mean (a) the code is wrong, (b) the test is wrong, or (c) you can't tell yet? Explain.

- I think this means that (a) the code is wrong. The test assertion is testing if the description returns `None` not an empty string `""`.

4. Why is a test suite shaped like a pyramid (many unit, few, e2e) and not a rectangle (equal numbers of each)?

- A test suite is shaped like a pyramid becasue the unit test at the bottom gives you the fastest feedback and is the lowest cost. 

5. You wrote a test yesterday that passes. Today you run it and it passes again. Tomorrow you run it and it fails. You run it again immediately and it passes. What kind of test is this, and why is it especially bad?

- This is considered a flaky test. This is bad becasue you can start to ignore the reds and then a real failure can get ignored. This can happen if the test is comparing against the time and the clock changes.


# What I fully don't understand

I still don't fully understand why the shape is a pyramid. It didn't really explain well execpt the fact that unit tests are faster and cost less than e2e testing.

# What I'll watch for tomorrow

I will look out for mocking. Because in todays lesson, it said that side effectful functions are harder to test becasue the test has to fake the side effect. So mocking is when you substitute a fake version during the test.



## Notes

**What a unit is**

- A unit test tests a unit. A unit is the smallest piece of your code that does one thing you can describe in a sentence.

**What is not a unit**

- The whole `runner.py main()` - Too many things in one place to verify in isolation.

- "The pipeline" - that's the system, not a unit.

- A single line of code - too small. You can't say in a sentence what one line does without context.

When writing a function, ask what would a test for this look like? If the answer is hard, the function probably does too much. Splitting it makes both testable and cleaner.

**A function is pure if:**

1. Given the same input, it always returns the same output.

2. It doesn't change anything outside itself - no writing files, no sending network requests, no modifying global state.

**A function has a side effect if it does anything outside returning a value:**

- `fetch_one("https://example.com")` - sends an HTTP request. Side effect.

- A function that writes to `results.json` - file I/O. Side effect.

- A function that prints to the terminal - also a side effect, though a mild one.

- A function that reads the current time - depends on outside state. Hard to test becasue the time keeps changing.

The takeaway: pure functions are easy to test, side-effectful functions are hard.

