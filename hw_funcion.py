# Question 1

""" def Quadratic_solver(a, b, c):
    if a==0:
        print("forbidden divide by 0")
        return
    if b**2-4*a*c<0:
        print("The divergent must be positive ")
        return
    
    x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    return x1,x2

print("Quadratic equation solver ax^2+bx+c")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
x1,x2=Quadratic_solver(a,b,c)
print("The first solution: ",x1)
print("The second solution: ",x2)
 """
# Question 2

""" def biggest_divider():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    divide_list=[]
    if num1>num2:
        large_num=num1
        small_num=num2
    else:
        large_num=num2
        small_num=num1
    for i in range(1,small_num+1):
        if large_num%i==0 and small_num%i==0:
            divide_list.append(i)
    print(divide_list)
    largest=max(divide_list)
    print("The largest divider is: ",largest)

def pow_your_num():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    pow_result=pow(num1,num2)
    print("pow result is: ",pow_result)

def sqrt_your_num():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    sqrt_result=num1**(1/num2)
    print("pow result is: ",sqrt_result)


print(" a-the biggest divider\n b-the result of pow (a,b)\n c-the result of sqrt(a,b)\n d-exit")
user_chose=None
while user_chose!="d":
    user_chose=input("entre your chose: ")
    if user_chose=="a":
        biggest_divider()
    if user_chose=="b":
        pow_your_num()
    if user_chose=="c":
        sqrt_your_num()
    if user_chose=="d":
        exit """

# Question 8

""" def print_string(my_str,num):
    print(my_str*num)

my_str=input("Enter the string you want to print: ")
quantaty_to_print=int(input("Enter how much times you want to print your string"))
print_string(my_str,quantaty_to_print) """

# Question 10

""" import datetime
def print_time_now():
    now=datetime.datetime.now()
    print(now)
    print_time_now() """


# Question 11

""" import random
def my_super_list(new_list):
    print("is function list: ",new_list)
    print(len(new_list))
    for i in range(1,len(new_list)+len(new_list)-1,2):
        new_list.insert(i,"|")
    print(new_list)
    print(len(new_list))



new_list=[]
list_size=int(input("enter the size of list you want create: "))
first_random=int(input("enter the begin of random number on the list: "))
last_random=int(input("enter the last of random number on the list: "))
for i in range(list_size):
        new_list.append(random.randint(first_random,last_random))
print(new_list)
my_super_list(new_list) """


# Question 19




import colorama
import random
def special_square(hight, length):
    for i in range(0, hight):
        for j in range(0, length):
            if (1 <= i < hight-1 and j == 0):
                print("*", end='')
            elif 1 <= i < hight-1 and j == length-1:
                print("*", end='')
            elif 1 <= i < hight-1 and 1 <= j < length-1:
                print(" ", end='')
            elif i == 0:
                print("*", end='')
            elif i == hight-1:
                print("*", end='')
        print("")


random_size = random.sample(range(1, 10), 2)
length = random_size[1]
hight = random_size[0]
print("\nhard coded square size\n")
special_square(4, 6)
print("\nrandom square size of hight: ",
      random_size[0], "and length: ", random_size[1], "\n")
special_square(hight, length)
print("\n")
hight_user = int(input("enter the hight of square: "))
print("\n")
length_user = int(input("enter the length of square: "))
print("\nUser choose the  size of square hight = ",
      hight_user, "and length = ", length_user, "\n")
special_square(hight_user, length_user)
