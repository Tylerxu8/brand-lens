# Week 5 Day 2

# What I did

Today I added a couple more test functions.

- `extracts_meta_description`
- `none_when_description_missing`
- `extracts_og_title`
- `picks_first_h1`
- `extracts_canonical`

Without opening `parse.py` the list tells you what the function does and how it handles missing data. 

# What a fixture is

So a fixture is a reusable setup function that provides a consistent environment for tests and reduces repetitive code.

- `@pytest.fixture` is what is defining the fixture ex.(`full_page_html`)

- `conftest.py` is the file where the fixture lives in and this is the file pytest looks for in the `tests/` directory. 

# Tests as a spec

If `parse.py` were deleted tommorrow, I wouldn't be able to reconstruct with whats written in the test specs. The spec is missing a lot of information because the test is only there to prove that the code works and to see if there are any bugs or errors. 

# What I don't fully understand

For `picks_first_h1`, why is the assert expression "Welcome to Brand Lens"?

I don't really understand why it changed. Is it because of the fixture?

## Notes

The point of a fixture is so that you don't have to keep building and HTML string. 

It is a cleaner setup and without the fixture, when you eventually want to change the scaffolding, you have to remember to change it in every test. 

**Fixture** - A chunk of setup pytest builds for you, named, that you ask for by adding it as a function parameter. 

When pytest runs the test, it sees the parameter, looks up the fixture by name, calls the fixture function, and passes the returned value as the argument. You don't have to call the fixture yourself - pytest writes it up.

- `@pytest.fixture` is a decorator that says "this function produces a value that tests can ask for." The function name (`full_page_html`) is the fixture's name. 

- `conftest.py` is a special filename pytest looks for in the `test/` directory. Any fixture defined here is available to every test file in that directory automatically - no import needed. 