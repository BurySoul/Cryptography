# 传统IC
def index_of_coincidence_1(text):
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


# IC的无偏估计
def index_of_coincidence_2(text):
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
        if total_letters - 1 == 0:
            continue
        frequency = (count * (count - 1)) / (total_letters * (total_letters - 1))
        ic += frequency
    return ic


def letter_matrix(text, key_length):
    text_length = len(text)
    cols = text_length // key_length + (1 if text_length % key_length else 0)
    matrix = [['' for _ in range(cols)] for _ in range(key_length)]
    text_index = 0
    for i in range(cols):
        for j in range(key_length):
            if text_index < text_length:
                matrix[j][i] = text[text_index]
                text_index += 1
            else:
                matrix[j][i] = ''
    sum_ic = 0

    mode = 1
    result = 0
    if mode == 2:
        for i in range(key_length):
            ic = index_of_coincidence_2(''.join(matrix[i]))
            # print(f"key_length = {key_length}, col = {i}, ic = {ic}")
            sum_ic += ic
        result = sum_ic / key_length

    else:
        result = ""
        for i in range(key_length):
            ic = index_of_coincidence_1(''.join(matrix[i]))
            # print(f"key_length = {key_length}, col = {i}, ic = {ic}")
            temp = round(ic, 4)
            if result != "":
                result += f", {temp}"
            else:
                result += f"{temp}"
    return result


ciphertext = input("Please enter the ciphertext:")

for i in range(1, len(ciphertext)):
    print(f"key length = {i}, ic = {letter_matrix(ciphertext, i)}")
    if i > 61:
        break
