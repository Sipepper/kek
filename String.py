print('введите что ли бо:')
input_string = input()
sample_string = "Это строка в которую {} новую строку"
preliminary_string = sample_string.format(input_string)
print(preliminary_string)
final_string = preliminary_string.replace(input_string, 'замена в строке')
print(final_string)
print(len(final_string))
if final_string.find('строка') != -1:
    print(True)

