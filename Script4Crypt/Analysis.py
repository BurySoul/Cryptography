def ic(text):
    letter_counts = {}
    total_letters = 0
    for char in text:
        if char.isalpha():
            char = char.lower()
            total_letters += 1
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    ic = 0
    # 打印每个字母及其出现频率
    for letter, count in sorted(letter_counts.items()):
        frequency = count / total_letters
        ic += frequency * frequency
    return ic


def sorted_letter_frequency(input_str):
    frequency = {}
    for char in input_str:
        if char.isalpha():
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return sorted_frequency


def print_matrix_with_coordinates_horizontal(text):
    rows, cols = 12, 7
    print('  ', end='')
    for col in range(1, cols + 1):
        print(col, end=' ')
    print()
    row_index = 1
    for i in range(0, len(text), cols):
        print(row_index, end=' ')
        row_index += 1

        for char in text[i:i + cols]:
            print(char, end=' ')
        print()


def print_matrix_vertical(text):
    rows, cols = 12, 7
    matrix = [[' ' for _ in range(cols)] for _ in range(rows)]

    for index, char in enumerate(text):
        row = index % rows
        col = index // rows
        matrix[row][col] = char

    print('  ', end='')
    for col in range(1, cols + 1):
        print(col, end=' ')
    print()
    for row in range(rows):
        print(row + 1, end=' ')
        for col in range(cols):
            print(matrix[row][col], end=' ')
        print()



input_str = "rndriineusenyvuterfpciaimelnplsoeeuenoqucolseffsfiiewmihatcoegislttrsstsamioafeaborn"
a = sorted_letter_frequency(input_str)

print_matrix_with_coordinates_horizontal(input_str)

print_matrix_vertical(input_str)