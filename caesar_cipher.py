def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


print("===== Caesar Cipher =====")

mode = input("Enter mode (encrypt/decrypt): ").lower()

if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode!")
else:
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    result = caesar_cipher(message, shift, mode)

    print("\nResult:", result)