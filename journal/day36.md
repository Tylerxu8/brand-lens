# Week 8 Day 2

# What I did

I started by building some context from the database to implement into a brief. I then added more context to my brief template so that it can hold information from the context I built earlier.

Now each brand has its own brief. The brand with a brief shows the full summary and without, shows "No brief has been generated for this brand yet." instead of crashing. 

I also updated my template to show the page description in the brief.

# My prediction

I expected to see all brands but I didn't know what was going to happen after that. For some reason, none of my brands got a stored in `json.dumps` so every brand hit the `{% else %}` branch.

# The json round trip



# Pretty vs true

It makes the grounding question more important because the brief can be generated looking the best and prettiest but the information that is stored in the brief has to be true. If the brief isn't true, the looks won't matter because the information on it, is useless.

# What I don't fully understand

I don't fully understand the json round trip. I don't know if I did something wrong in the earlier lessons but my brands didn't get stored into json for some reason. So during the lesson today, all the brief files showed "No brief has been generated for this brand yet.".

That is also why I didn't answer question #3.

