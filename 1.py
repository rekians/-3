name = input("имя:")
surname = input("фамилия:")
year = int(input("год рождения:"))
print(name,"_",surname,"_",year)
name, surname = surname, name
year += 60
print(name,"_",surname,"_",year)