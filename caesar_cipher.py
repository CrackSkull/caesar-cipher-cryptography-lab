choice = input("Type E for Encrypt or D for Decrypt: ")

message = input("Enter message: ")
shift = int(input("Enter shift value: "))

result = ""

if choice.upper() == 'D':
    shift = -shift

for char in message:
    if char.isalpha():
        shifted = ord(char) + shift

        if char.islower():
            while shifted > ord('z'):
                shifted -= 26
            while shifted < ord('a'):
                shifted += 26
            result += chr(shifted)

        elif char.isupper():
            while shifted > ord('Z'):
                shifted -= 26
            while shifted < ord('A'):
                shifted += 26
            result += chr(shifted)

    else:
        result += char

print("Result:", result)