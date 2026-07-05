from chunking_tools import chunk_string, chunk_generator

# Chunking Strings
text = "Supercalifragilisticexpialidocious"
print(chunk_string(text, 19))
# Output: ['Supercalif', 'ragilistic', 'expialidoc', 'ious']

# Chunking standard iterables without padding
numbers = [1, 2, 3, 4, 5, 6, 7]
print(list(chunk_generator(numbers, 3)))
# Output: [(1, 2, 3), (4, 5, 6), (7,)]