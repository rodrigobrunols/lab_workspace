

def commonCharacters(strings):
    list = []
    for c in strings[0]:
        list.append(c)

    list = [c for c in list if all(c in str for str in strings[1:])]
    return list



strings = ["abc", "bcd", "cbaccd"]

print(commonCharacters(strings))  # Output: ['c', 'c']
