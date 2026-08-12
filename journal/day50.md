# Week 11 Day 1

# What I did

Today I created an AWS root account and also created an IAM User.

The root account is the master key and the IAM User is a seperate user with a narrow set of permissions with a "master key".

After creating everything, I installed the AWS CLI to my terminal and configured the account so that it is pointed to my laptop and that it is authenticated as the locked down user not root.

# Why not root

I created a locked down user instead of using the root account for deploys following the least privilege principle. This means a credential should be able to do only what the job needs nothing else.

In Week 7, I hid my anthorpic key in a `.env` file so that my key won't get leaked and creating a locked down user is the same concept.  

# Where the keys live

Putting your key somewhere else instead of the project folder is safer because if the key lives in the project folder, the key can get leaked and your account can get hacked. 

# What I don't fully understand

I understood everything today, from creating my root account and a seperate locked down user. 

