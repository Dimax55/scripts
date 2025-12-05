#функція - це підпрограма, зменшити код програми

#параметр який передається буде видний тільки в середиті функції

def test_func(word):
    print(word,end="")
    print("!")             #не повертає ні якого значення


test_func("dima")
test_func(True)
test_func(5.6)

#----------------

def summa(a,b):
    return a+b
                    #повертає певне значення

res=summa(6,7)
print(res)
print(summa("H","i!"))

#-----------------

def minimal(list):     #функція на знаходження мінімального елементу

    min_number = list[0]

    for i in list:
        if i < min_number:
            min_number=i
    print(min_number)


nums1 = [5,6,7,8,9]     
minimal(nums1)

nums2 = [1,2,3,4,-1]
minimal(nums2)


#----------------анонімна функція
function1=lambda x,y: x*y
print(function1(5,2))