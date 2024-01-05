from collections import deque

### Task 2.2
def is_palindrome(str):
    clean_str = ''.join(str.lower().split())
    d = deque(clean_str)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

def task2():
    input_string = "A man a plan a canal Panama"
    result = is_palindrome(input_string)

    if result:
        print(f'"{input_string}" - це паліндром.')
    else:
        print(f'"{input_string}" - не паліндром.')

task2()
