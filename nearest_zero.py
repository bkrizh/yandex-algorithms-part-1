# id решения в Яндекс Контесте 85383031

def input_data():
    length_street = int(input())
    street = [0] * length_street
    return length_street, street


def find_empty_streets():
    length_street, street = input_data()
    spacing = [0 for x in range(length_street)]
    index = None
    for id, val in enumerate(street):
        if val == 0:
            index = id
            continue
        elif val != 0 and index is not None:
            spacing[id] = id-index
        else:
            spacing[id] = length_street

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
