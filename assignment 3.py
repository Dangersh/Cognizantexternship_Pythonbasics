python = "python is amazing"
print(python[0:6])
print(python[10:18])

print(python[-1:-18:-1])

python_2 = " hello, python world!."
python_2.strip(" ")
python_2 = python_2.capitalize()
python_2 = python_2.replace("world", "universe")
python_2 = python_2.upper()
print(python_2)

palindrome = str(input("Enter a word: "))
if palindrome == palindrome[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")