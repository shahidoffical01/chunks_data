from itertools import zip_longest

text = "This is the main data from where I type this for nothing to do with us to do this for the reason of what we are doing"
chunk_size = 32

# The "magic" zip_longest trick
# [iter(text)] * chunk_size creates a list of 32 references to the SAME iterator
# zip_longest then pulls from that same iterator 32 times per loop
chunks = [''.join(chunk) for chunk in zip_longest(*[iter(text)] * chunk_size, fillvalue='')]

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: '{chunk}'")