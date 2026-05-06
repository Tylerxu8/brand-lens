# Week 2 day 7

# Mini Quiz

1. In one sentence each, what does DNS, TCP, and TLS do?

- DNS is asking the server what the IP address is for that specific website.

- TCP is opening a connection for the IP address.

- TLS is negotiating the encryption.

2. If `repsonse.text` is the full HTML body, what's the difference between `response.text` and `response.text[500]`

- I believe `response.text[500]` is asking to limit the body to 500 characters.

3. You hit a URL and get back `status_code = 403`. Whose fault is that - yours or the server's? What might be happeneing?

- So in the 4xx range that would be my fault and it is telling me to slow down. (Correction - I went back up and it is still my fault but it is saying that the site is blocked because I seem like a bot)

4. Predict the output:

```python
x = "5"
y = 3

print(x * y)
```
What does this print? Why? 

- I think this will print an error becuase if you put an int into quotes, python will read that as a text so when you ask it to `print(x * y)` you can't do math with int and str. `*` is asking to multiply.

- Edit: When I ran the code I was wrong, I thought it would return an error but what happened was the it told python to multiple [5] three times giving the answer (555) since `x = "5"` is a string, it is telling python to print 5 three times. I was right on the multiplication part so I tried making `x = 2` and the answer was (6).

5. Why does `soup.title.string` crash on some pages but not others, and how did you guard against it on W1D3?

- `soup,title.string` crashes on some pages becasue you are asking to extract the title but some pages do not have titles so to defened that I used `soup.title.string if soup.title else "(no title)"`.

## What I fully don't understand

I understand the layers for the web but I am still fuzzy on the TLS part. It says that this is where the encryption get negotiated but I don't fully understand what that means.


## How my mental model changed

At first I was confused and felt like I was falling behind a little bit because I didn't fully understand `BeautifulSoup` but after today, I feel like I have caught up a bit and feel more comfortable reading what I wrote last week in `fetch_many.py`. I know I still have a long ways to go but I've learned a lot in the last two weeks and I can see in real time of my progression.

## Notes

**DNS** Is asking the server what is the IP address for a certain website.

**TCP** Is a protocol that is guaranteeing that data arrives in order wihtout erros and is opening a connection to that IP address on port 443 (which is the standard port for HTTPS).

**TLS** Is where the encryption gets negotiated and the server proves its identity with a certificate.


`response = requests.get(url)`, the `response` object has three things worth knowing: 

```python
response.status_code # an integer like 200, 404, 500
response.headers     # a dictionary of metadata about the response
response.text        # the body - usually HTML for webpages
```

When using `response.text`, this is the body of the HTTP response. For webpages, the body is the whole HTML. To extract the title you would use:

```python
soup = BeautifulSoup(response.text, "httml.parser")  # this is telling BeautifulSoup to parse the body
title = soup.title.string                            # which is telling string to extract just the title tag
```
