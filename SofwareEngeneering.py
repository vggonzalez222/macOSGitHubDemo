def encode(password):
    encoded = ""
    for char in password:
        # Wrap around if digit+3 exceeds 9
        encoded += str((int(char)+3)%10)
    return encoded



def main():
    while True:
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = input("Please enter an option: ")

        if choice == '1':
            password = input(f'Please enter your password to encode: ')
            encode_password =encode(password)
            print("Your password has been stored ")



        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

# how to push the code into the responsotary
# Becsause every time I try it doesnt even ask me for my password or anything
