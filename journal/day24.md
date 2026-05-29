# Week 5 Day 4

# What I did

Today we tested `fetch.py` by mocking the network. We used monkeypatch which is a fixture pytest provides for free. 

# What mocking solved

The problem that mocking sovled that I couldn't have by writing a "real" test is that the test is going to be slow and flaky.

If you have 50 tests in the suite it would take forever, the url could be down, the wifi could blip, the test could fail unrelated to your code so its best to mock up the network rather than writing a "real" test.

# The error-path test

This test is special because now it tells you if the `try/except` from `fetch.py` is working or not. After adding this test, it now simulates what a real network failure would look like. 

# What I don't fully understand

To be honest, I don't really understand this whole section of testing. I does make sense that it's to see if the code is working or not but, todays lesson, didn't really explain throughly on what I am doing and writing.