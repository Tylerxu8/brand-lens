# Week 10 Day 4

# What I did

Today I set up a CI, continues integration, for github to run my pytest suite automatically every push and PR instead of manually testing it.

I created a new directory called `.github` and created a `ci.yml` file on a new branch called `add-ci`. This YAML file contains everything it needs to create a CI in GitHub. 

I then made sure it worked on github and merged the branch to the main branch.  

# Why a secretless robot can run my tests

The CI can still run `fetch_one` and `summarize_brand` even though it is not connected to the internet because in the previous weeks, I created mock tests for the files so that it will be able to run without an API key or the internet.

# Reading ci.yml

The difference between `on:` and `runs-on:` is `on:` is telling when to run and `runs-on:` is creating a VM using `ubuntu-latest`.

The difference between `uses:` step and a `run:` step is `uses:` is telling what to use and `run:` is telling what to do.

# Green I'd never seen red

Deliberately watching CI fail is worth doing because it shows what it failed on and from there you can choose to merge the branch or not. 

# What I don't fully understand

I still don't fully understand the github PR workflow. I had trouble doing the `break-on-purpose` test because github was being buggy. That lead me to rethinking if I am doing this correctly or not so it made it more confusing.
