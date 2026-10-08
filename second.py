# name = "POOJA"
# age=21
# if name:
#     print("i am in if body")
#     if age>25:
#         print("age is > 25")
#     else:
#         print("age is < 25")
# else:
#     print("i am in if else body")


# day =(input("enter a number : "))
# if day==1:
#     print("sunday")
# elif day==2:
#     print("monday")
# elif day==3:
#     print("tuesday")
# elif day==4:
#     print("wednesday")
# elif day==5:
#     print("thursday")
# elif day==6:
#     print("friday")
# elif day==7:
#     print("saturday")
# else:
#     print("entered number have no day")  


# IF

# num=int(input("enter a number : "))
# if num>0:
#     print("positive")


# mark=int(input("enter mark : "))
# if mark>=50:
#     print("pass")


# age=int(input("enter age : "))
# if age>=18:
#     print("eligible for vote")


# num=int(input("enter a number : "))
# if num/5:
#     print("Divisible by 5")


# num=int(input("enter a number : "))
# if num>100:
#     print("Number is greater than 100")
      

# IF ELSE

# num=int(input("enter a number : "))
# if num % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")


# mark=int(input("enter mark : "))
# if mark>=40:
#     print("passed")
# else:
#     print("failed")


# age=int(input("enter age : "))
# if age>=18:
#     print("eligible for vote")
# else:
#     print("not eligible")


# num=int(input("enter a number : "))
# if num>0:
#     print("positive")
# else:
#     print("negative")


# amount=int(input("enter amount : "))
# if amount >= 5000:
#     print("customer is eligible for a discount")
# else:
#     print("customer is not eligible for a discount")


# NESTED IF

# age=int(input("enter age : "))
# if age>=18:
#     licence = input("do you passed driving test . (Yes/No) : ")
#     if licence.lower()=='yes':
#         print("eligible")
#     else:
#         print("not eligible")
# else:
#     print("you are under  age")


# attendance=int(input("enter attendance percentage : "))
# if attendance>=75:
#     fee = input("have you paid exm fee . (yes/no) : ")
#     if fee.lower()=='yes':
#         print("eligible")
#     else:
#         print("pay exm fee")
# else:
#     print("not eligible")


# age = int(input("Enter your age: "))
# if age>=21:
#     salary=int(input("Enter your monthly salary: "))
#     if salary>=25000:
#         print("Eligible for loan")
#     else:
#         print("Not eligible for loan")
# else:
#     print("under age")


# login = input("Are you logged in? (yes/no): ")
# if login == "yes":
#     balance = float(input("Enter your balance: "))
#     price = float(input("Enter product price: "))
#     if balance >= price:
#         print("You can purchase the product")
#     else:
#         print(" balance is low")
# else:
#     print("login first")



# mark=int(input("enter your mark: "))
# if mark>=50:
#     exam=input("have you completed entrance exam? (yes?no): ")
#     if exam.lower()=='yes':
#         print("eligible for admission")
#     else:
#         print("please complete your entrance exam")
# else:
#     print("not eligible for admission")

    


# IF ELIF ELSE

# mark =int(input("enter mark : "))
# if mark >=90:
#     print("A Grade")
# elif mark>=75:
#     print("B Grade")
# elif mark>=60:
#     print("C Grade") 
# elif mark>=40:
#     print("D grade")
# else:
#     print("failed")



# num =int(input("enter a number : "))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")

 

# day =int(input("enter a number : "))
# if day==1:
#     print("sunday")
# elif day==2:
#     print("monday")
# elif day==3:
#     print("tuesday")
# elif day==4:
#     print("wednesday")
# elif day==5:
#     print("thursday")
# elif day==6:
#     print("friday")
# elif day==7:
#     print("saturday")
# else:
#     print("entered no.have no day")  



# amount =int(input("enter amount : "))
# if amount >=10000:
#     print("20% discount")
# elif amount>=5000:
#     print("10% discount")
# elif amount>=2000:
#     print("5% discount") 
# else:
#     print("no discount")


# age =int(input("enter age : "))
# if age<=12:
#     print("child")
# elif age<=19:
#     print("teenager")
# elif age<=59:
#     print("adult") 
# else:
#     print("Senior Citizen")


# loops

# print(range(10,20))

# print(list(range(5,20,2)))


# print(list(range(20,10,-1)))



# FOR LOOP


# n=5
# for i in range(n):
#     print(i)

# name="pooja"
# for i in name:
#     print(i,end=" ")

# numbers=[10,22,44,11,22,65,76,14]
# l=[]
# for i in numbers:
#     if i % 2==0:
#        l.append(i)
# print(l)


# names=["pooja","diya","mariyam","vishnu"]
# for i in names:
#     for j in i:
#         print(j,end="")
#     print()


# WHILE LOOP

# n=1
# while n<=10:
#     print(n)
#     n=n+1


# name="pooja"
# length= len(name)
# i=0
# while i<length:
#     print(name[i])
#     i=i+1

#for loop questions

# for i in range(1, 11):
#     print(i)

# for i in range(2,51,2):
#     print(i)

# for i in range(1,51,2):
#     print(i)

# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print(sum)

# num = int(input("Enter a number: "))
# for i in range(1, 11):

# sum = 0
# for i in range(2, 101, 2):
#     sum = sum + i
# print("Sum =", sum)
   

# for i in range(1, 11):
#     print(i, "=", i * i)


#While Loop – Program Questions


# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# i = 2
# while i <= 50:
#     print(i)
#     i = i + 2


# i = 20
# while i >= 1:
#     print(i)
#     i = i - 1



# list conprehension


# numbers=[1,2,3,4,5]
# a=[x**2 for x in numbers]
# print(a)

# l=[i for i in range(11) if i % 2==0]
# print(l)

def add():
    print(5+3)


# def name():
#     print("pooja")


# add()
# name()



# 1. with argument with return

# 2.with argument without return

# 3.without argument without return

# 4.without argument with return

# def number_add(a,b):
#     return a+b

# p=int(input("enter your first number: "))
# s=int(input("enter your second number: "))
# answer=number_add(p,s)
# print("answer= ",answer)



n=int(input("enter a number"))
if n==0:
    print("n is 0")
else:
    print("n is not 0")