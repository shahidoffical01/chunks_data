import random

def generate_company_names():
    # Base syllables extracted from "shahid", "hasnain", and "luqman"
    syllables = [
        "sha", "hid", "ah",   # From shahid
        "has", "nain", "in",  # From hasnain
        "luq", "man", "an"    # From luqman
    ]
    
    valid_names = set()
    
    # Combine the syllables to create new words
    for first in syllables:
        for second in syllables:
            if first != second:
                combined = first + second
                # Enforce the 5 to 6 letter constraint
                if 5 <= len(combined) <= 6:
                    valid_names.add(combined.capitalize())
                    
    # Convert to a list and shuffle for variety
    results = list(valid_names)
    random.shuffle(results)
    
    return results

# Execute the function and print a sample of 15 names
suggested_names = generate_company_names()

print("Here are some 5 to 6 letter combinations:")
print("-" * 40)
for name in suggested_names[:15]:
    print(name)