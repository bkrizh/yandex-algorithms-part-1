# id решения в Яндекс Контесте 85392657

from collections import Counter


def input_data():
    k = int(input()) * 2
    matrix = list((''.join([input() for i in range(4)])).replace('.', '0'))
    return k, matrix


def get_max_score():
    k, matrix = input_data()
    count = 0
    numbers_dict = Counter(matrix)

    for key, val in numbers_dict.items():
        if key in '123456789' and val <= k:
            count += 1

    print(count)


if __name__ == '__main__':
    get_max_score()
