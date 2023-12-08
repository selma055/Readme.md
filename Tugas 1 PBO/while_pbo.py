names = ["Selma", "Mulkya", "Kya", "Nisa"]

index = 0
while index < len(names):
    current_name = names[index]

    if len(current_name) <= 5:
        print("Hi, " + current_name + "!")
    else:
        print("Hello, " + current_name + "!")

    index += 1