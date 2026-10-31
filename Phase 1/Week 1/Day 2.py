# Session Notes

print("30","10","2026",sep="-")
print("30","10","2026",sep="/")

print("a","b","c",sep=",")

print("a","b","c",sep="|")

print("Loading",end="")
print(".....",end="")
print("Done")


price = 135600

print(f"{price:,}")



#Practice Problems
#Q1) Print your name, age, and city on three separate lines.

name = "Vishnu"
age = 21
city = "Hyderabad"

print(name)
print(age)
print(city)

#or
print("Vishnu\n21\nHyderabd")


#Q2) Print three values separated by hyphens using sep.

print("Hyderabad","Delhi","Manali",sep="-")

#Q3) Print Loading... then done on the same line using end.

print("Loading...",end=" ")
print("Done")

#Q4) Print a date as 2024/01/15 using sep.

print("2024","01","15",sep="/")

#Q5) Use \n to print a two-line address from one print call.

print("ASR YSR TOWERS, Miyapur\nHyderabad, Telangana")

#Q6) Use \t to print a name and score in aligned columns.

print("Name:\tScore")
print("Vishnu:\t95")

#Q7) Print a Windows file path with literal backslashes.

print("C:\\Users\\uvish\\OneDrive\\Desktop\\Consistency. AI\\Python Practise")

#Q8) Print a sentence containing double quotes.

print("Ram said,\"Let's go to Kashmir next month.\"")

#Q9) Build a sentence from name and age using an f-string.

name = "Vishnu"
age = 21

print(f"My name is {name} and i am {age} years old.")

#Q10) Build the same sentence using comma-separated print

name = "Vishnu"
age = 21

print("My name is", name, "and i am", age, "years old.")

#Q11) Build the same sentence using + and str().

name= "Vishnu"
age = 21

print("My name is "+name+" and i am "+str(age)+" years old.")

#Q12) Explain why 'Age: ' + 25 fails and fix it three ways.

print("Age: " + str(25))
print("Age:",25)
print(f"Age: {25}")

#Q13) Print pi rounded to 2 decimal places with an f-string.

pi = 3.141592653589793
print(f"Pi: {pi:.2f}")

#Q14) Print 1250000 with thousands separators.

num= 1250000
print(f"{num:,}")

#Q15) Print 0.256 as a percentage with one decimal.

num = 0.256
print(f"{num:.1%}")

#Q16) Print an empty line between two messages.

print("My name is Vishnu,")

print()

print("I am Learrning Py.")

#Q17) Predict output: print('a','b',sep='',end='!') then print('c')

print('a', 'b', sep='', end='!')
print('c')

#Q18) Print a 3x3 box of stars using \n in one string.

print("***\n***\n***")

#Q19) Add an inline comment explaining a line of code.

Age = 21           # this stores the age of a person.
print(Age)

#Q20) Write a 3-line block comment using #.

# I am Vishnu.
# I like to play Badminton.
# I like watching movies.

#Q21) Write a multi-line comment using triple quotes.

""" I am Vishnu.
I like to play Badminton.
I like watching movies. """

#Q22) Comment out a line of code so it doesn't run

print("Hello World!")

# print("This line will not execute")

print("Thank you!")

#Q23) Write a function with a one-line docstring.

def hi():
    """Displays a welcome message."""
    print("Welcome to Python Pracitcee.")

hi()

#Q24) Print a function's docstring via __doc__.

def hi():
    """Displays a welcome message."""
    print("Hello Vishnu")

print(hi.__doc__)

#Q25) sep and end problem

print("1", "2", "3", sep="-", end="!\n")
print("next")

#Q26) Print ‘Total: $1,250.50 (20.0% off)’ from total = 1250.5 and discount = 0.2.

total = 1250.5
discount = 0.2

print(f"Total: ${total:,.2f} ({discount:.1%}off)")