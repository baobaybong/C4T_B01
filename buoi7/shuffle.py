import random
list1 = ["chicken", "crocodile", "elephant", "leopard"]
word = random.choice(list1)
char = list(word)
random.shuffle(char)
print("Day la con gi? ", end="")
print(*char, sep='')
ans = input()
if ans.lower() == word:
    print("Khon vl")
else:
    print("Sai me roi con ga nay")
