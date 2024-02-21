def hex_frequency_analysis_sorted(hex_str):
    hex_values = hex_str.split()

    frequency = {}
    for value in hex_values:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequency


hex_input = "16 8D 2C 97 3A 82 3B C3 30 85 7F 90 3E 9A 36 8D 38 C3 3C 8B 3A 86 2C 86 7F B5 36 80 2B 8C 2D 8A 3E 8D 2C C3 2C 82 36 87 7F 93 2D 96 31 86 2C C3 28 8B 3A 8D 7F 97 37 86 36 91 7F 93 36 80 2B 96 2D 86 7F 94 3E 90 7F 82 3D 8C 2A 97 7F 97 30 C3 3D 86 7F 97 3E 88 3A 8D 52 E9"
sorted_frequency = hex_frequency_analysis_sorted(hex_input)
print(sorted_frequency)