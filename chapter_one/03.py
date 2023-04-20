s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

# 不要な文字を削除
words = s.replace(",","").replace(".","")
# 単語に分解

print([len(line) for line in words.split()])
