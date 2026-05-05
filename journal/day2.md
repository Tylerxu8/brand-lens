# Week 1 Day 2

## What I did today
First I installed this tool called Homebrew.

- Homebrew is a Package manager and it installs developer tools for you.

When I fisnished downloading Homebrew, I installed the newest version of python using Homebrew.

- "brew install python@3.12"
- "python3 --version"

To check which python version I am currently running.

Next, I learned how to create a command that made it easier for me to open sublime files.

Instead of using 

- "open -a "Sublime Text" hello.py"

We created an alias in my shell config so the terminal knows what "subl" means.

So now when I run "subl hello.py" it opens that file on Sublime.

Next, we installed git into our terminal.

- "brew install git"
- "git --version"
	
Which shows us which version we are running

Then, I told git who I am and connected it using my GitHub account.

- "git config --global user.name "Username""
- "git config --global user.email "your-githubemail@example.com""
- "git config --global init.defaultBranch main"

- "--global" means use this for every project on this machine which you only do once per laptop.

## Connecting my laptop to Github
We used an SSH key which is a cryptographic handshake that is more secure and less annoying than passwords.

- "ssh-keygen -t ed25519 -C "you-github-email@example.com"

Which generates the key.

Then,

- "cat ~/.ssh/id_ed25519.pub"

This prints your public key.

Now when I run "ssh -T git@github.com" it shows my username and that I have authenticated.

## Making my first Repository
A Repository or repo is a folder that git is tracking.

- "cd ~dev/brand-lens"
- "git init"
- "git status"

"git status" is a command that tells you what git is seeing right now.

Now my work is backed up onto Github and shareable.

## Python with shape
I learned how to create an interactive input.

- "name = input("what's your name? ")"
- "print("hello,", name)"

This will run a command that will ask what my name is and then print "Hello, (name)"

Then I tried it on my own and came up with this.

- name = input("What's your name ? ")
- number = input("What's your favorite number? ")
- print("Hello,", name)
- print("Favorite number,", number)
- if int(number) > 100: 
	- print("That's a BIG one. ")
- else: 
	- print("Modest choice. ")

In the beginning, I tried running the code without puting int() in front of "number" so it kept giving me an error stating that ">" is not a valid syntax. 

Then I was told that I have to put a colon ":" next to the integers.

After that, it worked so I commited my work onto Github.

- "git status"
- "git add ." 
- "git commit -m "interactive hello with name and number""
- "git push"

Once published, I can see my line of codes directly on Github.

## What does "git init" actually do
To my understanding, "git init" creates a ".git" file and also creates a Repository
## What is the difference between "add" and "commit"?
When you "add" it changes the status from untracked to staged and when you "commit" it creates a snapshot of the current code.
## Why did Github need an SSH key?
The SSH key is more secure and connects my laptop directly to Github.