print('input your string')
input_string = input()
if len(input_string) % 2 == 0:
    if input_string[0:int(len(input_string)/2)] == (input_string[int(len(input_string)/2):])[::-1]:
        print('your string is a palindrome')
    else:
        print('your string is not a palindrome')
else:
    if input_string[0:int((len(input_string)-1)/2)] == (input_string[int((len(input_string)+1)/2):])[::-1]:
        print('your string is a palindrome')
    else:
        print('your string is not a palindrome')