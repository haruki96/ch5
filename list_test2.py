colors = ["purple", "orange", "green"]
colors = str(colors)

guess = input("What color do you think?")
guess = str(guess)

if guess in colors:
    print("good!")
else:
    print("miss!")
