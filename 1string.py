data = "   hello world   "

# Remove leading and trailing whitespace
print(data.strip())  # Output: "hello world"

# Split the string into a list of substrings
print(data.split())  # Output: ["hello", "world"]

# Join a list of strings into a single string
fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits))  # Output: "apple, banana, cherry"

# Replace occurrences of a substring
data = "hello world"
print(data.replace("world", "python"))  # Output: "hello python"

# Find the index of the first occurrence of a substring
print(data.find("world"))  # Output: 6

# Check if the string starts or ends with a specific substring
print(data.startswith("hello"))  # Output: True
print(data.endswith("world"))  # Output: True

data = "hello,world,python"
split_data = data.split(",")
print(split_data)  # Output: ["hello", "world", "python"]