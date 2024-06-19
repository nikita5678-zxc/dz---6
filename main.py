import random
points = 0
max_record = []
game_count = 0
print('Введите ваше имя')
user_name = input().lstrip()
with open('words.txt', 'rt') as file:
    for line in file:
        line = line.replace('\n', '')
        word = ''.join(random.sample(line, len(line)))
        print(f'Угадайте слово: {word}')
        answer = input().lstrip()
        if answer == line:
            print('Верно! Вы получаете 10 очков')
            points += 10
        else:
            print(f'Неверно! Верный ответ - {line}')
with open('history.txt', 'at') as file:
    file.write(f'\n{user_name} - {points}')

with open('history.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        line = line.split("-")
        line.remove(line[0])
        max_record.append(','.join(line))

with open('history.txt', 'rt') as file:
    for line in file:
        game_count += 1

print(f'Всего игр сыграно: {game_count} \nМаксимальный рекорд: {max(max_record)}')