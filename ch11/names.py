from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me first name: ")
    if first == "q":
        break
    last = input("Please give a last name: ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly formatted name: {formatted_name}.")
