print("Day la chuong trinh CRUD")
print("De them gia tri, bam C")
print("De hien thi list hien tai, bam R")
print("De thay doi gia tri co san, bam U")
print("De xoa gia tri co san, bam D")
print("De dung chuong trinh, bam X")
abusive_list = []
while 1:
    action = input("Ban muon lam clg? ")
    if action.upper() == "C":
        new_value = input("Nhap gia tri ban muon them: ")
        abusive_list.append(new_value)
        print("Da them gia tri " + new_value)
    elif action.upper() == "R":
        if len(abusive_list) == 0:
            print("List trong")
        else:
            print("Cac gia tri trong list: ", end="")
            print(*abusive_list, sep=', ')
    elif action.upper() =="U":
        i = input("Ban muon doi gia tri o index nao? ")
        if not i.isdigit():
            print("Khong co index " + i)
        elif int(i) >= len(abusive_list):
            print("Khong co gia tri tai index " + i)
        else:
            new_value = input("Nhap gia tri moi: ")
            print("Gia tri tai index " + i + " la " + abusive_list[int(i)] + " da duoc thay bang " + new_value)
            abusive_list[int(i)] = new_value
    elif action.upper() == "D":
        del_act = input("Ban muon xoa gia tri theo ten gia tri (dien v) hay theo index (dien i)? ")
        if del_act.lower() == "v":
            v = input("Gia tri ban muon xoa: ")
            if v in abusive_list:
                for value in abusive_list:
                    if value == v:
                        abusive_list.remove(value)
                print("Da xoa gia tri " + v)
            else:
                print("Khong co gia tri " + v + " trong list")
        elif del_act.lower() == "i":
            i = input("Index cua gia tri ban muon xoa: ")
            if not i.isdigit():
                print("Khong co index " + i)
            elif int(i) >= len(abusive_list):
                ("Khong co gia tri tai index " + i)
            else:
                print("Gia tri tai index " + i + " la " + abusive_list[int(i)] + " da bi xoa")
                abusive_list.pop(int(i))
        else: 
            print("Deo hieu ban muon lam gi")
    elif action.upper() == "X":
        print("Bai bít ch")
        break
    else:
        print("Deo hieu ban muon lam gi")


