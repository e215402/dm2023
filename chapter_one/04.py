s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
indexes = [1, 5, 6, 7, 8, 9, 15, 16, 19]
result = {}

words = s.replace(",","").replace(".","").split()

for i, word in enumerate(words):
    index = i + 1
    if index in indexes:
        key = word[0]
    else:
        key = word[:2]
    result[key] = index

print(result)















