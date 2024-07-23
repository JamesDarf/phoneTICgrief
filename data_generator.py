nato = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
        'K': 'Kilo', 'L': 'Linux', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee',
        'Z': 'Zulu'
    }

def to_phonetic(text):
   
    result = []
    for char in text.upper():
        if char in nato:
            result.append(nato[char])
        else:
            result.append(char)  # 알파벳과 숫자가 아닌 경우 그대로 추가
    return ' '.join(result)

second = {}

for k, v in nato.items():
    second[k] = to_phonetic(v)


ssss = {}

for k, v in second.items():
    ssss[k] = ''.join('S' if char.isalpha() else char for char in v)


print(second)
print(ssss)