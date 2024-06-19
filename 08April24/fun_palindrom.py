original_str="kommina"
def is_palindrom(original_str):
    reverse_str=original_str[::-1]
    print(reverse_str)
    if original_str==reverse_str:
        print("is palindrom")
    else:
        print("not a palindrom")
is_palindrom(original_str)
