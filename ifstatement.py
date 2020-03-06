# x = 10
# y = 20
# z = 50

# if x > y: 
#     if x > z:
#         print('x')
#     else: 
#         print('z')
# else: 
#     if y > z:
#         print('y')
#     else: 
#         print('z')

# p = 150000
# t = 2.5
# r = 2.5

# i = p*t*r/100
        
# print(f'simple intrest is {i}')

# x = i*100/t*r
# print(f'principle is {x}')
        
# math = 96
# science = 84
# english = 80
# nepali = 77
# account = 88
# tp = math+science+english+nepali+account/500*100
# t = math+science+english+nepali+account 

# print(f'total percentage is {tp}')
# print(f'sum of total subject is {t}')



# print("please enter the following info to know your result")
# name = input('Enter your name: ')
# count = 0
# english = float(input("Enter your marks in english(0-100): "))
# if english > 100:
#     print('your marks cannot be grater than 100')
#     english = float(input("Enter your marks in english(0-100): "))

    
# science = float(input("Enter your marks in science(0-100): "))
# if science > 100:
#     print('your marks cannot be grater than 100')
#     science = float(input("Enter your marks in science(0-100): "))

# math = float(input("Enter your marks in math(0-100): "))
# if math > 100:
#     print('your marks cannot be grater than 100')
#     math = float(input("Enter your marks in math(0-100): "))

# else:
#     total = english + science + math
#     average = total/3
#     print(f"your total secured marks is:{total}")
#     print(f"your average marks is:{average}")
    
#     if english > 40 or science > 40 or math > 40:
#         print(f"congratulation! you have pass in all subject")

#        if average >= 32 and average < 45:
#             print("Your have secured third division.")
#         elif average>=45 and average<60:
#             print("Your have secured second division.")
#         elif average>=60 and average<75:
#             print("You have sucured first division.")
#         else:
#             print("You have secured distinction.")
#     else:

#         print("Sorry! You have failed in following subjects:")
#         if english<32:
#             print("English")
#             count=count+1
#         if math<32:
#             print("Math")
#             count=count+1
#         if science<32:
#             print("Science")
#             count=count+1
 

# users = ["ram","shyam","hari"]
# for user in users:
#     print(user)

# users = [['ram','shyam','hari'],['1','2','3'],['a','n','m']]
# for us in users:
#     print(us)

# num = int(input('Enter num of std: '))
# x = 0
# students = [ ]
# while x < num:
#     name = input('Enter name')
#     students.append(name)
#     x+=1

# for student in students:
#     print(student)


# x = 0
# while x < 10:
#     if x == 5:
#         break
#     print(x)
#     x+=1


x = 0 
while x < 10:
    x+=1
    if x == 5:
        continue
    print(x)