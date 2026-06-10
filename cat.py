# my_cat = {'size': 'fat', 'color':'gray'}

# print(f"My cat is {my_cat['size']} and his fur's color is {my_cat['color']}.")

their_birthdays = {'Kiki': 'March 17', 'Momo': 'December 4', 'Sophie': 'June 22'}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == '':
        break

    if name in their_birthdays:
        print(f"{name}'s birthday is {their_birthdays[name]}")
    else:
        print(f"I don't have {name}'s birthday information.")
        print(f"What is {name}'s birthday?")
        bday = input()
        their_birthdays[name] = bday
        print("Birthday database updated.")

    print("Current database:")
    for name, bday in their_birthdays.items():
        print(f"{name}: {bday}")

