#практика 11
#Задание 1
#with open('test.txt', 'w', encoding='utf-8') as file:
#    file.write('Привет, файл!')
#with open('test.txt', 'r', encoding='utf-8') as file:
#    content = file.read()
#    print(content)
#задание 2
#with open('numbers.txt', 'w') as file:
#    for i in range(1, 11):
#        file.write(str(i))

#with open('numbers.txt', 'r') as file:
#    numbers = [int(line.strip()) for line in file]
#    total_sum = sum(numbers)
#    print(f'Сумма чисел:', total_sum)
#задание 3
#num_lines = 5
#with open('user_text.txt', 'w', encoding='utf-8') as file:
#    print(f'Введите {num_lines} строк:')
#    for i in range(num_lines):
#        line = input(f'Строка {i + 1}: ')
#        file.write(line + '\n')
#print('\nСтроки, содержащие больше 5 символов:')
#with open('user_text.txt', 'r', encoding='utf-8') as file:
#    for line in file:
#        clean_line = line.rstrip('\n')
#        if len(clean_line) > 5:
#            print(clean_line)
#задание 4
#try:
#    with open('data.txt', 'r', encoding='utf-8') as file:
#        lines = file.readlines()
#        line_count = len(lines)
#    print(f'Количество строк в файле: {line_count}')
#except FileNotFoundError:
#    print('Ошибка: файл data.txt не найден!')
#except Exception as e:
#    print(f'Произошла ошибка:', e)
#задание 5
#try:
#    with open('file.txt', 'r', encoding='utf-8') as file:
#        text = file.read()
#        words = text.split()
#        word_count = len(words)
#    print(f'Количество слов в файле:', word_count)
#except FileNotFoundError:
#    print('Ошибка: файл не найден!')
#except Exception as e:
#    print(f'Произошла ошибка: ', e)
#задание 6
#with open('log.txt', 'w', encoding='utf-8') as file:
#    file.write('Первая строка лога\n')
#    file.write('Вторая строка лога\n')
#    file.write('Третья строка лога\n')
#with open('log.txt', 'a', encoding='utf-8') as file:
#    file.write('Четвёртая строка (добавлена)\n')
#    file.write('Пятая строка (добавлена)\n')
 #   file.write('Шестая строка (добавлена)\n')
#with open('log.txt', 'r', encoding='utf-8') as file:
#    content = file.read()
#    print('Содержимое файла log.txt:')
 #   print(content)
#задание 7
#try:
#    with open('numbers.txt', 'r', encoding='utf-8') as file:
#        numbers = list(map(float, file.read().strip().split()))
#        max_number = max(numbers)
#        min_number = min(numbers)        
#        print(f'Максимальное число:', max_number)
#        print(f'Минимальное число:', min_number)
#except FileNotFoundError:
#    print('Ошибка: файл numbers.txt не найден!')
#except ValueError:
#    print('Ошибка: в файле содержатся некорректные данные (не числа)!')
#except Exception as e:
#    print(f'Произошла непредвиденная ошибка:', e)
#задание 8
#try:
#    with open('source.txt', 'r', encoding='utf-8') as source_file:
#        content = source_file.read()
#    with open('copy.txt', 'w', encoding='utf-8') as copy_file:
#        copy_file.write(content) 
#    print('Файл успешно скопирован!')
#except FileNotFoundError:
#    print('Ошибка: исходный файл source.txt не найден!')
#except Exception as e:
#    print(f'Произошла ошибка:', e)
#задание 9
#try:
#   with open('input.txt', 'r', encoding='utf-8') as input_file:
#        text = input_file.read()
#   upper_text = text.upper()
#    with open('output_upper.txt', 'w', encoding='utf-8') as output_file:
#        output_file.write(upper_text)
#    print('Текст успешно преобразован и сохранён в output_upper.txt!')
#except FileNotFoundError:
#   print('Ошибка: файл input.txt не найден!')
#except Exception as e:
#    print(f'Произошла ошибка:', e)



