def encode(password):
    encoded = ""
    for char in password:
        # Wrap around if digit+3 exceeds 9
        encoded += str((int(char)+3)%10)
    return encoded

def decode(string):
    decoded = ""
    for char in string:
        integer = int(char) - 3
        if integer < 0:
            integer += 10
        decoded += str(integer)
    return decoded

def main():
    while True:
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = input("Please enter an option: ")

        if choice == '1':
            password = input(f'Please enter your password to encode: ')
            encode_password =encode(password)
            print("Your password has been stored ")

        elif choice == '2':
            decoded_password = decode(encode_password)
            print(f"The encoded password is {encode_password}, and the original password is {decoded_password}.")

        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

# how to push the code into the responsotary
# Becsause every time I try it doesnt even ask me for my password or anything
