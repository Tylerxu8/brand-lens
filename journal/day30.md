# Week 7 Day 1

# What I did

Today we used claude through writing code and not a regular chat prompt. What I mean is that we asked claude a question through writing code and using an API key to get a response back in my terminal. 

An API key is a way for one program to ask another program over the internet to do something.

My program sends an HTTP request containing my question to anthropics servers and they send back a response. It is the same as `request/response` but this time I am talking to claudes servers instead of a website.

# My prediction vs to real runs

I predicted that I would just get a normal response as if I were asking the regular prompt and it was true. This shows that function calls are always going to give the same answer but LLM calls are always going get you a different response. 

# Why the key lives in .env

Your API key has to live in the `.env` file and not direclty on the `first_call.py` file because `load_dotenv()` and `client = Anthropic()` is fetching that key for you from your `.env` file. Also your API key is like any other password you want to keep safe which is why it is stored in `.gitignore` so that it can never be exposed and traced back.

# What I don't fully understand

I don't fully understand `message.content[0].text`. I understand that it is using the message dict to print but I don't understand the `.content[0].text` part of that line.