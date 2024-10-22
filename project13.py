#Write a python program to count total number of notes in the given amount?
amount = int(input("Enter the amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

for note in notes:
    count = amount // note
    if count > 0:
        print(f"{note} Rs notes: {count}")
    amount %= note
