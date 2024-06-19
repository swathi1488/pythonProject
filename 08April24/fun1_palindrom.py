original_str="pradeep"
def is_palindrom(original_str):
    return ' '.join(reversed(original_str))
rev_str=is_palindrom(original_str)
print(rev_str)
if original_str==rev_str:
    print("is palindrom")
else:
    print("not a palindrom")