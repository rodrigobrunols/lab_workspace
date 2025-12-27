import re
match = re.search(r'\d+', 'abc123def')
if match:
    print("Found:", match.group())  # Found: 123


match = re.match(r'\d+', '123abc')
if match:
    print("Starts with digits:", match.group())  # Starts with digits: 123

# replace

result = re.sub(r'\d+', '#', 'a1b22c333d')
print(result)  # a#b#c#d

text = "Hello, 123 World! 456"
cleaned = re.sub(r'[^a-zA-Z]', '', text)  # Remove everything except letters

print(cleaned)  # Output: HelloWorldtext = "Hello, 123 World! 456"
cleaned = re.sub(r'[^a-zA-Z]', '', text)  # Remove everything except letters
print(cleaned)  # Output: HelloWorld

text = "Hello, 123 World! 456"
cleaned = re.sub(r'[^a-zA-Z ]', '', text)  # Keep letters and spaces
print(cleaned)  # Output: "Hello  World"

# findall
numbers = re.findall(r'\d+', '1a22b333c')
print(numbers)  # ['1', '22', '333']

# split
parts = re.split(r'\d+', 'a1b22c333d')
print(parts)  # ['a', 'b', 'c', 'd']

# compiling
pattern = re.compile(r'\d+')
match = pattern.search('abc123')
if match:
    print(match.group())  # 123


