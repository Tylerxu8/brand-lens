# Week 10 Day 2

# What I did

Today I turned yesterdays branch into a pull request.

A pull request is a request to pull the commits from your branch into another branch, `main`. It is a proposal step, the straight to `main` workflow never had.

**Base** should be `main`, **compare** should be `(name of branch)`, this case, `add-site-footer`.

This is read as "merge compare into base". If it were backwards, you'd propose merging `main` into the branch.

After merging the pull request, I deleted the branch on GitHub since it did its one job. I did the same in my terminal so that my laptop can match the data from GitHub.

# PR as a review checkpoint

So reviewing the steps instead of commiting straight to `main` offers a lot of things but the main thing that I think is really useful is being able to make changes and add code without fully commiting to `main`. 

This is very useful when the change you are making is risky and don't know if the change will work or not.

# Base vs compare

So "base" should be the `main` branch and the "compare" should be the new branch you are trying to merge to `main`. If you were to swap this order, you would be merging `main` into the new branch you were working on. 

# Reviewing my own diff

Im not too sure what this question is asking for but maybe an extra file that you didn't intend you touch?

I am not 100% sure with this answer because this is my first time merging a branch and seeing the diff that way.

# What I don't fully understand

I don't understand why local main didn't update until git pull even though I had already merged and deleted from Github. 

Do I have to do git pull every time I merge a branch to `main`?
