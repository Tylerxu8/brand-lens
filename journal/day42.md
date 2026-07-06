# Week 9 Day 3

# Mini Quiz

1. Yesterday `print(html)` showed raw `<h1>` tags but `open` showed a drawn page. Explain the difference in terms of who interprets the HTML.

- The browser is the program that interprets the HTML text into a drawn page.

2. Define "static site" in one sentence, then state plainly whether Brand Lens needs a backend and why - point to what the pipeline does and when it does it.

- A site where the files are already finished before anyone visits. Brand Lens doesn't need a backend because there is nothing that requires a desicion, lookup, or computation. 

3. Name the three languages a browser reads and the one job each does. Which one does Brand Lens use none of, and why is that the thing that makes it static?

- HTML- The content and structure.
- CSS- The appearance.
- JavaScript- Code that runs in the browser to make a page interactive.

- Brand Lens doesn't use JavaScript because it is a static site. It makes it static because the files are already finsihed so when someone visits the site, they get the file exactly as it was built until I rebuild it.

4. You open the site two ways: `open site/index.html` and `python -m http.server` then `localhost:8000`. What's different about the two - what's in the address bar each time, and which one is the rehersal for how AWS will serve it?

- When the site is opened by `open site/index.html`, the browser read the file straight off the disk but `python -m http.server` turns the file into a website that is running from "this machine" (localhost). 
So when you look up `http://localhost:8000` it shows the same thing as `open...`but the address bar shows localhost and not the disk. This is also the rehersal for how AWS will serve it.

5. Your brand page links to `index.html` (relative) rather than `/User/tyler/brand-lens/site/index.html` (absolute). Give the concrete failure the absolute version would cause once the site is copied to an S3 bucket.

- When you hardcode an absolute path the links break everywhere except your laptop. Relative links are what makes the site portable, build once, run anywhere.

# What I don't fully understand

I still don't fully understand the difference between relative and absolute links. When should I use absolute links and when should I be using relative links? I think I would be able to explain to someone else but not fully.