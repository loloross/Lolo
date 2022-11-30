print("Hello, World")
name = input("What's your name? ")
print("Hello " + name + "!")
if name.lower() == "steven":
    print("You're the coolest person in the world!")

temperature = int(input("What's the temperature right now? ")) # this will crash if the user enters something that isn't a number
if temperature <= 32:
    print("Wow, it's freezing!")
elif temperature <= 60:
    print("It's sweater weather.")
else:
    print("Let's go outside!")