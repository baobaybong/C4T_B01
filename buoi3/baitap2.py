invalid_name = True
while invalid_name:
    invalid_name = False
    name = input("Hay nhap ten cua ban vao: ")
    for i in name:
        if i.isdigit():
            print("Ten khong hop le vi co chu so")
            invalid_name = True
            break
invalid_password = True
while invalid_password:
    invalid_password = False
    password = input("Hay nhap mat khau cua ban vao: ")
    for i in password:
        invalid_password = True
        if i.isdigit():
            invalid_password = False
            break
    if invalid_password == True:
        print("Mat khau can chua so")
    if len(password)<=8:
        print("Mat khau can it nhat 8 ky tu")
        invalid_password = True
