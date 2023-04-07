# id решения в Яндекс Контесте 85312705

def input_data():
    k = int(input()) * 2
    matrix = list((''.join([input() for i in range(4)])).replace('.', '0'))
    return k, matrix


def get_max_score():
    k, matrix = input_data()
    numbers = []

    for i in range(1, 10):
        count = matrix.count(str(i))
        numbers.append(count)

    count = 0

    for j, value in enumerate(numbers):
        if value != 0 and value <= k:
            count += 1

    print(count)


if __name__ == '__main__':
    get_max_score()
