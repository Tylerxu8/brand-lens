# Week 3 Day 1

# What I did

I started by installing pyyaml into my terminal so I can use `yaml`. I then created a dict in a `brands.yaml` file to pull data from for my script. After that, I refactored my script so that the outer loop is over brands, and each brand's pages.

This grabs data from `brands.yaml` now instaed of `urls.txt`. 

# What I learned

- I learned what YAML is and what why it is used. 

- How to parse the YAML file into a Python dict. `yaml.safe_load(f)` 

- You have to always use `safe_load` for files you didn't write yourself and not just `load` beacause if you run the unsafe version, it can execute code hidden within the yaml file. 

# What I fully don't understand

```python
brand_results = {}
for slug, brand in config["brands"].items():
    print(f"\n=== {brand['name']} ===")
```

I didn't understand this at first but I asked claude to explain it to me and I understand better now. 

# Claude check-in

I asked claude to explain this because I didn't understand what `slug` was doing. 

```python
brand_results = {}
for slug, brand in config["brands"].items():
    print(f"\n=== {brand['name']} ===")
```
`brand_results = {}` - creates an empty dict called `brand_results`.

`config["brands"]` grabs the data from the `brands` section in the `brands.yaml` file.

`.items()` is what gives you both the key and the value as you loop.

`slug, brand` slug is getting the key and brand is getting the value.

# If `brands.yaml` had 100 brands and one of them had a typo making it invalid YAML, what would happen, and at what line of your script would the error appear(Don't run anything to check - predict.)

I think at which every brand the typo is in, will print an error because the key wouldn't match the value. 

For example:

`brand.yaml`: 
```python
brands:
  inisfree:
    name: Innisfree
    country: South Korea
    pages:
      - https://www.innisfree.com
      - https://us.innisfree.com
```
`inisfree` is the key and doesn't match the value `Innisfree`

So it would fail at:

```python
brand_results = {}
for slug, brand in config["brands"].items():
    print(f"\n=== {brand['name']} ===")
```

### Edit

I put my answer into claude along with the question and it said that it was good think but `inisfree` and `innisfree` woulnd't acutally be considered a typo but instead missing a `:` or not indenting is the actual typo. From this, it said that it would crash:

```python
with open("brands.yaml") as f:
	config = yaml.safe_load(f) # it would crash here
```

Becuase `yaml.safe_load()` reads and parses the entire file all at once and not line by line so if brand 50 of 100 had the typo, it wouldn't print brands 1-50, it would try to parse the whole thing and crash immediately once it hits the broken part. 

## Notes

YAML is a readable format for structured data. It is easier to edit, supports comments, and has fewer brackets and quotes than JSON.

For Yaml syntax, 

- indentation matters - two spaces, no tabs 
- `-` stats a list item

