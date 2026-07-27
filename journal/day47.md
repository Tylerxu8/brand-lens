# Mini Quiz

1. "A branch is a pointer, not a copy." Explain what it points at, and what happens to that pointer when you make a new commit while on the branch.

A branch is a tiny label that points at one commit and when you make a new commit, the label slides forward to the new commit.

2. After `git switch -c feature` and one commit on `feature`, `main` "doesn't have" that commit. Using the lables-and-parents model, explain precisely what that means - where does `main` point, where does `feature` point?

So after swtiching branches and commiting on the `feature` branch, `main` remains pointing at C, the parent, and the new label `feature` slides to D.

3. What's the difference between a fast-forward merge and a merge commit? Name a situation that forces a merge commit.

A fast-forward merge is when you are working solo and a merge commit is created when you are working with a teammate or when you create a new branch after.

Merge commits is forced when a second branch is created while working on a current branch by you or a teammate.

4. What is a merge conflict, and why is git stopping to ask you a good thing rather than a bug?

A merge conflict is when the same file was edited in conflicting ways and git can't guess which to commit so it will ask you to choose.

Git stopping to ask is a good thing when you and a teammate are working on the same project, both lines of the same file were edited in conflicting ways, thats when merge conflict happens and git will ask you to choose.

5. Give the three properties of the branch/PR workflow (isolation, review-before-merge, parallel work) and, for each, the one concrete bad outcome it prevents.

**Isolation**. A branch is a separate pointer, so work-in-progress lives off main. main stays trustworthy because broken or half-done commits aren't reachable from it until merged.

**Review before merge**. The PR is a gate in front of the merge. The change is a proposal (commits on a branch) until someone approves it. Nothing lands on main unseen.

**Parallel work without collisions**. Many people branch off main at once, each on their own pointer, and merge back. Git reconciles the lines; conflicts surface explicitly instead of one person silently clobbering another.

# What I don't fully understand

I still don't fully understand what the difference is between merge commit and merge conflict. To my understanding, they basically mean the same thing.

# What I'll do tomorrow

Tommorrow, I will set up a CI which is a robot that runs pytest automactically on every push and PR. It matters that my tests don't need the network or a real API key because we are only mocking those tests and to see if the mock tests are working correctly or not. 
