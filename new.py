def encoder(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password = encoded_password + encoded_digit
    return encoded_password

def decoder(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password = decoded_password + decoded_digit
    return decoded_password
def main():
    while True:
        print("\n","Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")
            pass
        elif option == 2:
            decoded_password = decoder(encoded_password)
            print("The encoded password is", encoded_password, ", and the original password is", decoded_password, ".")
            pass
        elif option == 3:
            break


if __name__ == "__main__":
    main()