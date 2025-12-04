#Dictionary / словнник - можемо створити ключ до нашої зміної в списку

#country = dict(code="UA", name'"Ukraine")    #альтернатива написання
country = {"code":"UA", "name":"Ukraine", "population":43}
print(country)
print(country["name"])       #працюємо з інформацією через ключ


for key in country:      # виводимо ключі
    print(key)


for key, value in country.items():    #виводимо ключі та значення
    print(key, "-", value)

country.pop("name")   #видалити певний елемент по ключу
country.clear()    #почистити на словник
print(country)

#опис конкретного обєкту
person = {
    "user_1":{
        "first_name":"John",
        "last_name":"Marly",
        "age":45,
        "address":[192,168,0,1,True],
        "grades":{'first':1, "second":5}
    },
    "user_2": {

    }
}
print(person["user_1"]["address"])