words={'apple','banana','chery','date','elderberry','fig'}
min_len=6
def check_len(word1):
    return len(word1)>min_len
output=list(filter(check_len,words))
print(output)