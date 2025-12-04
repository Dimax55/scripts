#Кортеж / tuple - це ті ж самі списки але дані яких не можна змінити(константа)
#Кортеж вfжить менше за список

#data = 4,5,6,True, "Hello"    #створення кортежу
#data = (4,)
data  = (4,5,6,True, "Hello")
print(data[1])


print(data.count(6)) # підрахунок скільки подібних елементів є в кортежі
print(len(data))  #довжина

for i in data:
    print(i)

nums =[3,4,5]
new_data = tuple(nums)   #перетворити список в кортеж
print(new_data)


word = "hello world" 
word = tuple("hello world")   #перетворити рядок в кортеж
print(word)