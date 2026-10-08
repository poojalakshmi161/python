# from calculator_fn import add,sub,div,mul


# while True:
#     print("1:add")
#     print("2:sub")
#     print("3:div")
#     print("4:mul")
#     print("5:exit")

#     choice=int(input("enter your choice: "))

#     if choice==1:
#         number1=int(input("enter your first number: "))
#         number2=int(input("enter your second number: "))
#         answer=add(number1,number2)
#         print(f"{number1}+{number2}={answer}")
#     elif choice==2:
#         number1=int(input("enter your first number: "))
#         number2=int(input("enter your second number: "))
#         answer=sub(number1,number2)
#         print(f"{number1}-{number2}={answer}")
#     elif choice==3:
#         number1=int(input("enter your first number: "))
#         number2=int(input("enter your second number: "))
#         if number1==0:
#             print("cannot divided by 0")
#         else:
#             answer=div(number1,number2)
#             print(f"{number1}/{number2}={answer}")
#     elif choice==4:
#         number1=int(input("enter your first number: "))
#         number2=int(input("enter your second number: "))
#         answer=mul(number1,number2)
#         print(f"{number1}*{number2}={answer}")
#     elif choice==5:
#         break
            



# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result
# print(factorial(5))


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#         return True
# print(is_prime(7))



# def count_vowels(text):
#     count = 0
#     for ch in text:
#         if ch.lower() in "aeiou":
#             count += 1
#     return count
# print(count_vowels("Hello World"))