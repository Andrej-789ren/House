
#Задание 1
#with open('test.txt', 'w', encoding='utf-8') as file:
#  file.write('Hi file')
#with open('test.txt', 'r', encoding='utf-8') as file:
#  print(file.read())
#Задание 2
#with open('numbers.txt', 'w') as file:
#  for number in range(1,11):
#    file.write(str(number))
#total_sum=0
#with open('numbers.txt', 'r') as file:
#  for line in file:
#    cleaned_line=line.strip()
#    number = int(cleaned_line)
#    total_sum += number
#print('Summa=', total_sum)
#Задание3
#print("Введите 5 строк:")
#user_lines = []
#for i in range(5):
#    line = input(f"Строка {i + 1}: ")
#    user_lines.append(line)

#with open("user_text.txt", "w", encoding="utf-8") as file:
#    for line in user_lines:
#        file.write(line + "\n")

#print("\nСтроки, содержащие больше 5 символов:")
#with open("user_text.txt", "r", encoding="utf-8") as file:
#    for line in file:
        
#        clean_line = line.rstrip("\n")
        
#       if len(clean_line) > 5:
#           print(clean_line)
#Задание 4
#with open('data.txt', 'r', encoding='utf-8') as file:
#    count = 0
#    for line in file:
#        count += 1
#print(count)
#задание 5
#def count_words_simple(filename):
#    with open(filename, 'r', encoding='utf-8') as file:
#        content =file.read()
#        words = content.split()
#        return len(words)
#word_count = count_words_simple('file.txt')
#print('word_count')
