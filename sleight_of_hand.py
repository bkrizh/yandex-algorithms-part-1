# id решения в Яндекс Контесте 85460617

def input_data():
    k = int(input()) * 2
    matrix = list((''.join([input() for _ in range(4)])).replace('.', ''))
    return k, matrix


def get_max_score():
    k, matrix = input_data()
    count = 0
    key = set(matrix)
    numbers_dict = dict.fromkeys(key, 0)
    print(numbers_dict)

    for elem in matrix:
        numbers_dict[elem] += 1

    for key, val in numbers_dict.items():
        if val <= k:
            count += 1

    print(count)


if __name__ == '__main__':
    get_max_score()
