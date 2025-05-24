#Q1
print ("Q1")
name = "dan"
age = 20
height = 5.10

print(f"Hey there my name is {name}! I am {age} years old and {height:.2f} feet tall")

#Q2
print ("Q2")
print()

num_1 = 10
num_2 = 20

print (f"Sum of {num_1} and {num_2} is {num_1 + num_2}")
print (f"Subtraction of {num_1} and {num_2} is {num_1 - num_2}")
print (f"Multiplication of {num_1} and {num_2} is {num_1 * num_2}")
print (f"Division of {num_1} and {num_2} is {num_1 / num_2}")

#Q3
print ("Q3")
print()
num = float(input("Enter a number: "))

if num > 0:
    print("This number is positive. Awesome!")
elif num < 0:
    print("This number is negative. Better luck next time!")
else:
    print("This number is zero. Neutral!")