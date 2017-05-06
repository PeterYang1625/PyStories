# Tuesdays examples

num1 = 12
num2 = 8

# addition
result = num1 + num2
print(result)

# subtraction
result = num1 - num2
print(result)

# multiplication
result = num1 * num2
print(result)

# real division
result = num1 / num2
print(result)

# integer division
result = num1 // num2
print(result)

print("num2 =", num2)
# same as: num2 = num2 + 4
num2 += 4
print("num2 =", num2)

dessert = input("What is your favorite dessert? ")
dessert = dessert.strip()
dessertLower = dessert.lower()
if dessertLower == "cupcakes" or dessertLower == "cupcake":
    print("Great choice!")
    kind = input("What is your favorite kind of cupcake? ")
    print(kind)
elif dessertLower == "brownies":
    print("I love brownies!")
elif dessertLower == "white chocolate":
    print("That is NOT real chocolate")
else:
    print("Your favorite dessert is " + dessert)

print("Thanks for your input.")

dessert1 = input("Enter a dessert: ")
dessert2 = input("Enter another dessert: ")

# comparison of strings is by alphabetical order
if dessert1 < dessert2:
    print(dessert1 + " is less than " + dessert2)
else:
    print(dessert1 + " greater than " + dessert2)
