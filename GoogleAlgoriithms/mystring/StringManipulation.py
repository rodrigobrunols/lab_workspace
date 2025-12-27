from bisect import bisect, bisect_left

s = "banana bread"

print(s.startswith("banana"))
print(s.endswith("bread"))

s = "hello world, world is big"

# Remove all 'world'
print(s.replace("world", ""))  # 'hello ,  is big'
print(s.replace("world", "", 1))

s = [1,2]
a = bisect_left(s,3 )
print(a)

l = len("python")
s = "python is awesome"
a = len("awesome")
idx = s.index("python")
print(s.index('python'))  # 10
print(s.find('y'))  # -1
if idx != -1:
    n = s[idx + l:].strip()
    m = s[:-a]
    print(n)
    print(m)

print()


s = "I love Buiú"
#    012345678910

print(s[2:6])   # 'love'

# This means: start from index 4 → go until the end
print(s[4:])  # 've Buiú'

# This means: start from 4th char from the end → go until the end
print(s[-4:])  # 'Buiú'

# This means: start from beginning → stop right before index 4
print(s[:4])  # 'I lo'

# Start from the beginning (default) and stop 4 characters from the end (exclusive).
print(s[:-4])  # Output: 'I love '
