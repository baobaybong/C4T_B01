subjects = ["biology", "chemistry", "wryyy"]
new_sub = input("wdyw? ")
subjects.append(new_sub)
print("Current subjects: ", end=" ")
print(*subjects, sep=' | ')
print("First subject: " + subjects[0].upper())
ec = len(subjects)
print("Best subject: " + subjects[ec-1].upper())
print("Before last subject: " + subjects[ec-2].upper())