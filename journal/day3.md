# Day 3

# What I did today
We first set up a Virtual Environment

- 'cd ~/dev/brand-lens'
- 'python3 -m venv venv'
- 'ls'

This created a 'vevn/' folder which is the sandbox within dev/brand-lens

To use the sandbox you have to activate it:

- 'dev/brand-lens'
- 'source venv/bin/activate'

Now the prompt should start with (venv). To leave the sandbox, type deactivate.

Always activate this before working on a project. 

To no have git track the venv/ folder, we created a .gitignore file

## In Ghostty

- 'touch .gitignore'
- 'open -a "Sublime Text" .gitignore'

## In Sublime

- 'venv/'
- '__pychace__/'
- '*.pyc'
- '.DS_Store'

## Back in Ghostty

Commit "Add gitignore"

## Installing 


## What does a virtrual environment do and why does it exist?
A virtual environment exists because installing a bunch of libraries onto your computer takes up a lot of space and is a mess so creating a virtual environment helps manage your projects.

## What happens when you run 'requests.get(url)'?
To my knowledge, this is what shows as the response when it retrives the URL.

## What's the difference between 'response.text' and 'soup.title.string'?
'response.text' shows the actual title

and 

'soup.title.string' is a defense code because some pages don't have titles so without the guard, the script will crash.