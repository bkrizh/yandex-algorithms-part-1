# id решения в Яндекс Контесте 85266122

def input_data():
    length_street = int(input())
    street = [int(num) for num in input().split(' ')]
    return length_street, street


def find_empty_streets():
    length_street, street = input_data()
    spacing = []
    index = None
    for id, val in enumerate(street):
        if val == 0:
            index = id
            spacing.append(0)
            continue
        elif val != 0 and index is not None:
            spacing.append(id-index)
        else:
            spacing.append(length_street)

    index = None
    reversed_spacing = list(reversed(spacing))

    for i, value in enumerate(reversed_spacing):
        if value == 0:
            index = i
            continue
        elif (value != 0 and index is not None and i - index < value):
            reversed_spacing[i] = i - index

    print(*reversed(reversed_spacing))


if __name__ == '__main__':
    find_empty_streets()
