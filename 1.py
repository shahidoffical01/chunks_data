text="This is the main data from where i tyoe this fro nothing do to us to do this fro the resaon of what we are doing"

chunks=[]

chunk_size= 25

for i in range(0, len(text), chunk_size):
    chunk= text[i:i + chunk_size]
    chunks.append(chunk)
print(chunks)