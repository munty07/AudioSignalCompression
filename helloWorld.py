# ex1
# name = 'John Smith'
# age = 20
# is_new = True

####################################################

# ex2
# name = input('What is your name? ')
# color = input('What\' is your favorite color? ')
# print(name + ' likes ' + color)

####################################################

#ex3
# mail = '''
# Hello Anda

# Thanks for your e-mail. nmsbjkcbjsnj

# Bye
# '''
# print(mail)

####################################################

#ex4
# string = 'Ana are mere'
# print(string[0]) #A - prima litera
# print(string[-1]) #e - ultima litera

####################################################

#ex5
# string2 = 'Andrada are mere'
# print(string2[0:3]) #And - primele 3 litere
# print(string2[:3])  #And - primele 3 litere
# print(string2[:])   #Andrada are mere - tot stringul

# string3 = 'Jennifer'
# print(string3[1:-1]) #ennife

####################################################

#ex6
# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(message)
# print(msg)

####################################################

#ex7
# prop = 'Ana are mere'
# print(len(prop))          #12

# print(prop.title())       #Ana Are Mere

# print(prop.upper())       #ANA ARE MERE
# print(prop.lower())       #ana are mere

# print(prop.find('j'))     #-1 -> nu exista caracterul in prop data
# print(prop.find('a'))     #2  -> pozitia 2
# print(prop.find('are'))   #4 -> de pe pozitia 4

# print(prop.replace('mere','pere')) #Ana are pere

# print('mere' in prop)     #True  -> exista 'mere' in prop
# print('Mere' in prop)     #False -> nu exista 'Mere' in prop

####################################################

#ex8
# print(10 / 3)       #3.3333333....
# print(10 // 3)      #3  (int)
# print(10 % 3)       #1  (rest)
# print(10 * 3)       #30
# print(2 ** 5)       #32 -> 2^5(la putere)

####################################################

#ex9
# x = 10
# x = x + 3   #13
# print(x)
# x += 3   #16
# print(x)

####################################################

#ex10
# x = 2.7
# print(round(x))     #3   -> rotunjire
# print(abs(-2.9))    #2.9 -> val absoluta

####################################################

#ex11
# import math

# print(math.ceil(2.7))   #3
# print(math.floor(2.7))  #2
# print(math.fabs(-2.7))  #2.7

####################################################

#ex12
# is_hot = False
# is_cold = True
# #if id_hot = true
# if is_hot:      
#     print('It s a hot day')
# elif is_cold:
#     print('It s a cold day')
# else:
#     print('It s a lovely day')

# print('Enjoy your day')

####################################################

#ex13
# price = 100
# has_good_credit = False

# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f'Down payment: ${down_payment}')     #Down payment: $20.0

####################################################

#ex14
# has_high_income = True
# has_good_credit = True
# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")
# #Eligible for loan

# a = True
# b = False
# if a or b:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")
# #Eligible for loan

# c = True
# d = True
# if c and not d: # true and (not true) => true and false => false
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")
# #not eligible for loan

####################################################

#ex15
# temperature = 30
# #if temperature > 30:
# if temperature == 30:
#     print("It's a hot day")
# else:
#     print("It's a cold day")

# name = 'Jo'

# if len(name) < 3:
#     print("Name must be at least 3 characters")
# elif len(name) > 50:
#     print("Name must be a maximum of 50 characters")
# else:
#     print("Name looks good!")

####################################################

#ex16
# weight = (int)(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
# #input function always return a string

# #if unit == 'l' or unit == 'L':
# if unit.upper() == 'L':
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")

####################################################

#ex17
# i = 1
# while i <=5:
#     print(i)
#     i = i + 1 #i += 1
# print("Done")
# # 1
# # 2   
# # 3   
# # 4   
# # 5   
# # Done

##--------------------------------

# i = 1
# while i <=5:
#     print("*" * i)
#     i = i + 1 
# print("Done")

####################################################

#ex18
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = (int)(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won")
#         break
# else:
#     print("Sorry, you failed")

####################################################

#ex19
# command = ""
# started = False

# #while command.lower() != "quit": #while command.upper() != "QUIT":
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print("""
#         start - to start the car
#         stop - to stop the car
#         quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand that.")

####################################################

#ex20
# for item in 'Python':
#     print(item)
# # P
# # y
# # t
# # h
# # o
# # n

#-----------------------------

# for item in [1, 2, 3, 4]:
#     print(item)
# # 1
# # 2
# # 3
# # 4

#-----------------------------

# for item in range(5):
#     print(item)
# # 0
# # 1
# # 2
# # 3
# # 4

#-----------------------------

# for item in range(3, 10):
#     print(item)
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9

#-----------------------------

# for item in range(3, 10, 2): #din 2 in 2
#     print(item)
# # 3
# # 5
# # 7
# # 9


####################################################

#ex21
# prices = [10, 20, 30]
# total = 0

# for price in prices:
#     total += price
# print(f"Total: {total}")    #Total: 60

####################################################

#ex22
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# # (0, 0)
# # (0, 1)
# # (0, 2)
# # (1, 0)
# # (1, 1)
# # (1, 2)
# # (2, 0)
# # (2, 1)
# # (2, 2)
# # (3, 0)
# # (3, 1)
# # (3, 2)

####################################################

#ex23
# numbers = [5, 2, 5, 2, 2]
# for x in numbers:
#     print("x" * x)

# # xxxxx
# # xx   
# # xxxxx
# # xx   
# # xx

#----------------------------------

# numbers = [5, 2, 5, 2, 2]
# for x in numbers:
#     output = ''
#     for count in range(x):
#         output += 'x'
#     print(output)

# # xxxxx
# # xx   
# # xxxxx
# # xx   
# # xx

####################################################

#ex24
# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[2:])    #['Mosh', 'Sarah', 'Mary']
# print(names[2:4])   #['Mosh', 'Sarah']
# print(names[:])     #['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

# names[0] = "Jon"
# print(names)        #['Jon', 'Bob', 'Mosh', 'Sarah', 'Mary']

####################################################

#ex25
# numbers = [3, 11, 2, 8, 4, 10]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max) #11

####################################################

#ex26
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# #print(matrix[0][1])     #2
# #matrix[0][1] = 20
# #print(matrix[0][1])     #20

for row in matrix:
    for item in row:
        print(item)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9