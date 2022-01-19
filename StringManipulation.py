print('Введите исходную строку в которой хотите заменить слово')
input_string = input()
print('Введите номер слова которое хотите заменить')
input_position = int(input()) - 1
print('Введите слово на которое вы хотите заменить ')
words = input_string.split(' ')
if len(words[input_position]) <= 2:
    final_result = format(input_string, words[input_position + 1])
    print(final_result)
else:
    final_result = format(input_string, words[input_position])
