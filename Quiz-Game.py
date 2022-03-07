print("Welcome to the Avengers Quiz")
print("    Avengers! ..Assemble      ")
score = 0
user_input = input("Avenger Fan. We welcome you. Let's start with the game. \nWhat is your age? \n")
age = 9
try:
    age = int(user_input)
except Exception:
    print("That's not an int!")
if age > 9:
    print("Great! Let's start the game.")
    question = input("Who was the founder of Marvel comics? \n Answer: ")
    if question == "Martin Goodman":
        print("Correct. You gain 1 point")
        score += 1
    else:
        print("Incorrect. You lose 1 point")
        score -= 1

    question = input("When did Martin started the marvel comics? \n Answer:")
    if question == "1939":
        print("Correct. You gain 1 point")
        score += 1
    else:
        print("Incorrect. You lose 1 point")
        score -= 1

    question = input(
        "What was the price of first marvel comic? Name the comic.\n(answer with cents. Eg: 5 Cents, 18 Cents \n Answer:")
    if question == "10 Cents":
        print("Correct. You gain 1 point")
        score += 1
    else:
        print("Incorrect. You lose 1 point")
        score -= 1

    question = input("The first comic was sold for______.\n(amount in integer) \n Answer:")
    if question == "1300000":
        print("Correct. You gain 1 point")
        score += 1
    else:
        print("Incorrect. You lose 1 point")
        score -= 1

    question = input("Who is current editor in chief?\n(Name with last name\n Answer:")
    if question == "Chester Cebulski":
        print("Correct. You gain 1 point")
        score += 1
    else:
        print("Incorrect. You lose 1 point")
        score -= 1

    if score > 1:
        print("You achieved " + str(score) + " points.")
    elif 2 < score < 2:
        print("You achieved " + str(score) + " point.")
    elif score < -1:
        print("You achieved " + str(score) + " points.")
elif age <9:
    print("dbvHSDjySDGj,c")
else:
    print("Hulk Smash")