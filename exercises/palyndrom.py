# is_palindrome("A man a plan a canal Panama")  # True
# is_palindrome("Python")                        # False

def is_palindrome(text):
    text = text.replace(" ", "").lower()  # Normalize the text by removing spaces and converting to lowercase
    len_text = len(text)
    middle_index_text = int(len_text/2)
    
    
    for i in range(middle_index_text):
        if text[i] != text[-(1 + i)]:
            raise Exception(f"The word '{text}' is not a palindrome")
    
    print(f"The word '{text}' is a palindrome")

# is_palindrome("A man a plan a canal Panama")
# is_palindrome("Python")

print("---------------------------")

t = " A man a plan a canal Panama "

def is_palindrome(text):
    text = ''.join(text.strip().split()).lower()

    return text == text[::-1]

print(is_palindrome(t))

def is_palindrome(text):
    text = ''.join(text.strip().split()).lower()

    for i in range(len(text) // 2):
        if text[i] != text[-(i + 1)]:
            return False

    return True


print(is_palindrome(t))