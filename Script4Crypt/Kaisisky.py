import re
import sympy
import pandas as pd


def ic(text):
    # 存储每个字母的出现次数
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


# 找到text中重复出现的序列
def find_duplicate_sequences(text):
    # 使用正则表达式查找长度大于2的重复出现的序列
    pattern = re.compile(r'([a-zA-Z0-9]{4,})(?=.*\1)')
    duplicates = re.findall(pattern, text)
    return duplicates


# 计算某个substring在text中多次重复之间的间隔，得到间隔int列表
def distance_between_occurrences(text, substring):
    first_index = text.find(substring)
    second_index = text.find(substring, first_index + len(substring))
    result = []
    while second_index != -1:
        result.append(second_index - first_index)
        first_index = text.find(substring, first_index + len(substring))
        second_index = text.find(substring, second_index + len(substring))
    return result


# 去掉所有非字母元素
def letters_only(text):
    # 使用正则表达式匹配字母，并将非字母字符替换为空格
    return re.sub(r'[^a-zA-Z]', '', text)


# 通过因子重复次数，计算key长度的概率
def probability_of_key_length(dataframe):
    counts = dataframe.apply(lambda col: col.str.count('✓').sum())
    total_rows = len(df)
    percentages = (counts / total_rows) * 100
    percentages = percentages.sort_values(ascending=False)
    print("====Probability of each key length====")
    for index, value in percentages.items():
        print(f"  {index} - {round(value, 1)}%")
    print()
    return percentages.index.tolist()


def get_factors(number):
    factors = sympy.factorint(number)
    result = []
    # 遍历每个质因数及其指数
    for prime, exponent in factors.items():
        new_factors = [prime ** i for i in range(1, exponent + 1)]
        result.extend(new_factors)
    return result


def draw_factors(dict_factors):
    rows = []
    for key, values in dict_factors.items():
        for value in values:
            rows.append((key, value))
    df = pd.DataFrame(index=list(dict_factors.keys()), columns=sorted(list(set.union(*dict_factors.values()))))
    # 填充表格
    for row, col in rows:
        if col in dict_factors[row]:
            df.at[row, col] = '✓'
        else:
            df.at[row, col] = ''
    # 打印 DataFrame
    print("==============Graph of factors of interval length in repeating sequences==============")
    print(df.to_string())
    print()
    return df


def cut_text_with_gap(text, gap):
    text_list = []
    gap_count = 0
    while gap_count < gap:
        text_temp = text[gap_count::gap]
        gap_count += 1
        text_list.append(text_temp)

    return text_list


def decrypt_vigenere(ciphertext, key):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""

    key_length = len(key)
    key_indices = [alphabet.index(k.upper()) for k in key]

    for i, char in enumerate(ciphertext):
        if char.upper() in alphabet:
            idx = (alphabet.index(char.upper()) - key_indices[i % key_length]) % len(alphabet)
            plaintext += alphabet[idx].lower() if char.islower() else alphabet[idx]
        else:
            plaintext += char

    return plaintext


text = "Gvune hmv kjvy gp znjhneu yys mzumvgy gfnffnkm fthnmwyzsx. Giy kvjjs te rfzzd kc-if znjhx fb f usxb qfcssuow ff fgdtzbydssk ptfy. Nw mtl rt ecy xsy kc fe ohkwazhd fb Rfbirm, bffp fb nk cs Kijjrfp. Cs Wfnuod, tvjty yf gjv kmrh lfoqj vfms sfh gvss ncwbsi fb. Jzhmvf bffp fb yysr kvje, cw dcav hmva yf bjoh bvsp’j znjh. Dfi fcgt dod nosk ht fank ftlhnes rvsyzblj osu qqrgx dsjkwsxg."

# text 预处理，全小写 + 仅保留字母
text = text.lower()
letters_text = letters_only(text)

# 寻找存在的重复序列，并去掉重复的
duplicates = find_duplicate_sequences(letters_text)
duplicates = list(set(duplicates))
print("Repeat Sequences:", duplicates)
# 字典 - key：重复序列，value：包含重复序列的所有间隔的list
dict_duplicates = dict.fromkeys(duplicates, [])
# 字典 - key：因式分解后的因子，value：该因子出现的次数
dict_factors = {}
for i in range(len(duplicates)):
    # 得到重复序列duplicates[i]在letters_text中的间隔int列表
    dict_duplicates[duplicates[i]] = distance_between_occurrences(letters_text, duplicates[i])
    for j in range(len(dict_duplicates[duplicates[i]])):
        # 对间隔int列表中的每个间隔进行因式分解，得到字典factor - key：因子，value：次数
        factors_list = get_factors(dict_duplicates[duplicates[i]][j])
        dict_factors[duplicates[i]] = set((dict_factors.get(duplicates[i], set([])) | set(factors_list)))

# 在console中绘制 序列-因子 表
df = draw_factors(dict_factors)
# 按概率从高到低拿到key长度list
probability_of_key_length = probability_of_key_length(df)
# 拿到最有可能的key长度，对letters_text进行切割，并随后计算各个的IC
cut_list = cut_text_with_gap(letters_text, probability_of_key_length[0])


for i in range(len(cut_list)):
    print(cut_list[i])


