webs = ["ph", "xv", "vlx", "gg"]
print("Current webs: ", end=" ")
print(*webs, sep =".com ",end="")
print(".com")
webs[0] = input("New first web: ")
webs[len(webs)-1] = input("New last web: ")
print("Current webs: ", end=" ")
print(*webs, sep='.com ', end="")
print(".com")
while 1:
    i = input("What is the index of the web u want to change? ")
    if not i.isdigit():
        print("There is no index " + i)
    elif int(i) >= len(webs):
        print("No web at index " + i)
    else:
        break
webs[int(i)] = input("New index "+ i + " web: ")
print("Current webs: ", end=" ")
print(*webs, sep='.com ', end="")
print(".com")

