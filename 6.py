"""
chunking_tools.py
A collection of utilities for chunking strings and iterables in Python.
"""
from itertools import zip_longest
from typing import Iterable, Generator, List, Any

def chunk_with_zip(iterable: Iterable, chunk_size: int, fillvalue: Any = None) -> Iterable:
    """
    Collect data into non-overlapping fixed-length chunks.
    Uses the highly optimized `zip_longest` iterator trick.
    """
    args = [iter(iterable)] * chunk_size
    return zip_longest(*args, fillvalue=fillvalue)

def chunk_string(text: str, chunk_size: int) -> List[str]:
    """
    Chunks a string into specific sizes. Leaves no trailing fill values.
    
    Example:
        >>> chunk_string("HelloWorld", 3)
        ['Hel', 'loW', 'orl', 'd']
    """
    chunks = chunk_with_zip(text, chunk_size, fillvalue='')
    return [''.join(chunk) for chunk in chunks]

def chunk_generator(iterable: Iterable, chunk_size: int) -> Generator[tuple, None, None]:
    """
    A readable, generator-based alternative for chunking.
    Does not pad the final chunk with fill values.
    """
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield tuple(chunk)
            chunk = []
    if chunk:
        yield tuple(chunk)

if __name__ == "__main__":
    # --- Example Usage ---
    sample_text = "This is for nothing for the reason of what we are doing"
    size = 23
    
    print("--- zip_longest Method ---")
    for i, chunk in enumerate(chunk_string(sample_text, size)):
        print(f"Chunk {i+1}: '{chunk}'")
        
    print("\n--- Generator Method (with list) ---")
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i, chunk in enumerate(chunk_generator(sample_list, 4)):
        print(f"Chunk {i+1}: {chunk}")