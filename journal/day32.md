# Week 7 Day 3

# Mini Quiz

1. In your own words, how is `client.messages.create(...)` the same as the `requests.get(url)` you used is Week 2? Name what's added that a public web request didn't need.

`client.messages.create(...)` is the same as `requests.get(url)` because they are doing the same thing. They are both asking the server for data and reciving back that data in a structured form. 

The thing that was added that a public web request didn't need is the API key. Every request must carry the API key and the server checks before doing anything and that check is proving you're you.

2. Why does the API key go in `.env` and not in the code, stated in terms of what the key authorizes (not just "it's a secret")? If a key leaks, what's the fix, and why isn't "log out" the fix?

The API key has to go into `.env` because the key is a password which can be used by other people to use your money. So the `.env` file lives in `.gitignore` which git doesn't track so your key can't be leaked.

If your key leaks, the fix is to delete that key and create a new one. `Log out` isn't a fix because whoever has the key, has to go into their console and revoke it. 

3. You set `max_tokens=300`. What does that limit, exactly - input, output, or both? Name one reason a cap is useful even when you trust the prompt.

When you set `max_tokens=...` it limits the output. A cap is useful even when you trust your prompt because claude is a text predictor predicting plausible next text, token by token, so if you don't put a limit, sometimes it can ramble on forever, extending you token usage.

4. Define "hallucinate" for and LLM. Why  does a text-predicting model do this, and what did D2's prompt do to push against it?

"hallucinate" for an LLM is when something that the scraped data never supported, a fact about something that isn't true. This happens because the LLM doesn't know it's wrong because it isn't checking against truth, it is only predicting text. 

5. You wrote `test_parse_page_extracts_title` in Week 5 with a hard-coded `assert`. Explain why you cannot write an equivalent `assert results["value_proposition"] == "..."` for a real `summarize_brand` call, and what you'll do instead(one word, plus a sentence)

Mocking. In the test, you replace it with a fake that returns a canned response, instantly offline for free. 

# What I don't fully understand

I don't fully understand the temperature setting part. What is that doing for the response. "A pure function (`parse_page`) has no such knob; an LLM alway does" I don't understand what this means.

# What I'll watch for tomorrow

I am expecting that I will always get a different response each time I run the prompt and I am going to do a lot of mocking. 

