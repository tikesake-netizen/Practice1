def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]


text = input("Enter a word or phrase: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")