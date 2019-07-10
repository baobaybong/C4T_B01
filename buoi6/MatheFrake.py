import random
point = 0
while 1:
    print("Point: " + str(point))
    n1 = str(random.randint(1, 30))
    n2 = str(random.randint(1, 30))
    ops = [" + ", " - "]
    op = random.choice(ops)
    option = n1 + op + n2
    ans = eval(option)
    n3 = random.randint(ans - 5, ans + 5)
    sol = random.randint(0, 1)
    if sol or n3 == ans:
        sol = "y"
        print(option + " = " + str(ans))
    else:
        sol = "n"
        print(option + " = " + str(n3))
    allowed_inp = ["Y", "N", "y", "n"]
    inp = 0
    question_marks = 1
    while inp not in allowed_inp:
        inp = input("Y/N"+ "?" * question_marks + " ")
        question_marks += 1
    if inp.lower() == sol:
        point += 1
    else:
        print("Game over!")
        print("Point: " + str(point))
        break