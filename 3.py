def chunk_string(text, chunk_size):
    """Splits a string into chunks of a specific size."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

text = "The website is warning you:We will not display it again. This means once you close this browser tab, you cannot come back to copy this exact key."

# Now you can easily call the function whenever you need it
chunks = chunk_string(text, 22)
print(chunks)