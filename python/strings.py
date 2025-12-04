#строка це той ж самий список це кожен елемент це певний символ строкі 

word = "hello_world_yoy_"
print(word[1])

for i in word:
    print(i)

print(len(word))    #підрахунок кількості елементів в рядку
print(word.count("!"))

print(word.upper()) #вивести рядок у верхньому регістрі
print(word.lower())  #вивести рядок в нижньому регістрі
print(word.isupper()) #перевірка чи рядок є у верхньому регістрі
print(word.islower())
print(word.capitalize())  #привести перший символ у верхній регістр


print(word.find("d"))  #шукаємо симвіл і виводить індекс символу

print(word.split("_"))  #створити список з рядка

hobby= word.split("_")
print(hobby)

#привести до верхнього регістру перший елемент з списку
for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()
print(hobby)

 #перевести список в звичанний рядок
result = ", ".join(hobby)
print(result)

# ІНДЕКСИ І СРЕЗИ #

print(word[0:5])
print(word[0:-1:2])   #виводити символ з рялка з кроком в 2
print(word[::])

list = [6,2,"stroka",True,5.5]
print(list[2:5:1])      #вивести елемент з списку з кроком в 1
print(list[::])