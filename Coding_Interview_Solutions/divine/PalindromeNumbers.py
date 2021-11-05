# palindrome is a concept that means the content will be same as they difined even tough when we iterate them in reverse order.

def is_palindrome(con):
    length = len(con)
    for i in range(length//2):
        if con[i] == con[length-i-1]:
            continue
        else:
            return False
    return True



string = input()  # stdin
 
print(is_palindrome(string))