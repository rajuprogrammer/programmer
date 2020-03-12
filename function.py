# def test():
#     print('hello functio')

# test()

# def test(x,y):
#     print(x,y)

# test(10,20)

# def test(x,y):
#     print('hello function')

# test(10,20)


# def user(name, age):
#     get_name = f'your name is{name}'
#     get_name = f'age{}'
#     return [get_name, get_name]

# data = users('ram', 20)
#     print(data[0])
#     print(data[1])


# def students(name, roll=None):
#     print(name)
#     if not roll == None:
#         print(roll)

# students('ram',20)

# def students(name,age):
#     print(name)
#     print(age)

# students('ram','30')


print('------function_practice-------')
# def user():
#     print('hello function')

# user()

# def user(x,y):
#     print(x,y)

# user(10,30)

# def test():
#     print('hello function')

# print(test)

# def user(*names,):
#     print(names)

# user('ram','shyam','hari')

# def user(*names,**data):
#     print(names)
#     print(data)

# user('ram','shyam','hari','ktm', age=24, phone=9813548604)

# x = 40

# def user():
#     global x
#     x = x + 20
#     print(x)

# user()

 
# def users(name, age):
#     return[name, age]

# user = users('ram','25')
# print(user[0])


# def take_valu():
#     x = int(input('Enter p: '))
#     y = int(input('Enter t: '))
#     z = int(input('Enter r: '))

#     return [x,y,z] 
# def calculate():
#     data = take_value()
#     p = data[0]
#     t = data[1]
#     r = data[2]
#     return p * t * r / 100

# def display():
#     print(calculate())

# display()





# def users():
#     def names(name):
#         return f'your name is {name}'

#     return names

# data = users()
# print(data('ram'))

# x = 10

# def test():
#     global x
#     x = x + 20
#     print(x)

# test()


# data = lambda x, y: x + y

# print(data(10,20))

# def users(x):
#     return lambda y: x + y

# a = users(10)
# print(a(20))



# def get_doc(anyfunction):
#     def inner():
#         return f'{anyfunction.__doc__}'

#     return inner


# @get_doc
# def test():
#     """this is test function"""

#     pass

# @get_doc
# def user():
#     """hello ussers function"""

#     pass

# def get_doc(number):
#     def innerfunction():
#         return f'{number.__doc__}'

#     return innerfunction



# @get_doc
# def test(x):
#     """this is number"""
#     pass



def zero_check(anyfunction):
    def inner(x,y):
        if y == 0:
            return f"y is zero"
        return anyfunction(x,y)

    return inner


@zero_check
def add(x,y):
    
    return x + y

print(add(10, 10))