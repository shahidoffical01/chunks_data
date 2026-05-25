text="The website is warning you:We will not display it again. This means once you close this browser tab, you cannot come back to copy this exact key."

chunks=[]

chunk_size= 25

for i in range(0, len(text), chunk_size):
    chunk= text[i:i + chunk_size]
    chunks.append(chunk)
print(chunks)