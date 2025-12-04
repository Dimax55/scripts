
# список / list - це місце де ми можемо зберігати зразу набор з декількох зміних
# в списку кожен елемент має всій індекс, починаючи з нуля
# в списку мажуть бути елемкнти з різними типати даних
# в списку можу бути інший список

nums = [5, 14, 4.6 , True, "hello", 7, 100]
print (nums)

nums[0] = 50  #змінити перший елемент списку по індексу
print('\n',nums) 

print('\n',nums[4])  #вивести окремий 

nums = [5, 14, 4.6 , True, "hello", 7, 100,[111,222]]
print ('\n',nums)

print('\n',nums[-1][-1])  #вивести останній елемент списку


nums.append("yoy")   #додати новий елемент
print('\n',nums)

nums.insert(1, "141")   #змінити значення другого елементу
print('\n',nums)

B = [5,6,7]
nums.extend(B) # додати декілька елементів
print('\n',nums)

#nums.sort()    #сортувати елементи від більшого до меншого 
                # але без типу даних string!!

nums.reverse()   #перевертає список задом на перед
print(nums)

nums.pop(-5)   #видалети n-ний елемент з списку по інднксу
print(nums)

nums.remove('hello')  #видалити елемент з списку по його значенню
print(nums)

nums

nums.clear()      #видалиити весь список
print(nums)

nums = [111,222,333,444,"five",True]

for i in nums:
    print(i)


##application for user to create a list
n = int(input("Enter lenght: "))
user_list =[]
i=0
while i < n:
    string = "enter element #" + str(i+1) + ":"
    user_list.append(input(string))
    i+=1
print(user_list)




##################
### HOME  TASK ###
##################

#Вивести мінімальну оцінку.

#Вивести максимальну оцінку.

#Вивести середнє значення оцінок.

#Додати нову оцінку в список.

#Видалити оцінку 6 зі списку.

#Вивести оновлений список.


#grades = [12,8,6,11,9,10,7]
#print(grades)
#print('min value is: ', min(grades))
#print('max value is: ', max(grades))
#num_of_values= (len(grades))
#print(sum(grades)/num_of_values)
#grades.append("111")
#print(grades)
#grades.remove(6)
#print(grades)