from random import randint
from time import sleep
scores = []
for i in range(5):
    scores.append(randint(0,100))
scores.sort(reverse = True)
print("High scores:")
for i,v in enumerate(scores):
    print(str(i + 1) + ". " + str(v))
def a():
    sleep(1)
    scores.append(int(new))
    scores.sort(reverse = True)
    for i in range(5, len(scores)):
        scores.remove(scores[i])
    print("High scores:")
    for i,v in enumerate(scores):
        print(str(i + 1) + ". " + str(v))
while 1:
    god = True
    for i in scores:
        if i < 100:
            god = False
    if god:
        print("Thánh cmnr")
        break
    new = input("Nhập score mới vào đây thằng ngu này: ")
    if not new.isdigit():
        input("Score là số tự nhiên ngu à? ")
    elif int(new) > 100:
        print("Trên 100 điểm cc")
        sleep(1)
    elif int(new) == 100:
        print("Ăn may")
        a()
    else:
        print("Gà vl")
        a()
