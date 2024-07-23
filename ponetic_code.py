
# 포네틱 코드로 변환
def to_phonetic(text):
    nato = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
        'K': 'Kilo', 'L': 'Linux', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee',
        'Z': 'Zulu'
    }
    result = []
    for char in text.upper():
        if char in nato:
            result.append(nato[char])
        else:
            result.append(char)  # 알파벳과 숫자가 아닌 경우 그대로 추가
    return ' '.join(result)

# 이중 포네틱 코드로 변환
def second_phonetic_conversion(phonetic_text):
    # 원본 데이터
    extended_nato_old = {
        "A": "ALPHA LIMA PAPA HOTEL ALPHA",
        "B": "BRAVO ROMEO ALPHA VICTOR OSCAR",
        "C": "CHARLIE HOTEL ALPHA ROMEO LIMA INDIA ECHO",
        "D": "DELTA ECHO LIMA TANGO ALPHA",
        "E": "ECHO CHARLIE HOTEL OSCAR",
        "F": "FOXTROT OSCAR XRAY TANGO ROMEO OSCAR TANGO",
        "G": "GOLF OSCAR LIMA FOXTROT",
        "H": "HOTEL OSCAR TANGO ECHO LIMA",
        "I": "INDIA NOVEMBER DELTA INDIA ALPHA",
        "J": "JULIETT UNIFORM LIMA INDIA ECHO TANGO TANGO",
        "K": "KILO INDIA LIMA OSCAR",
        "L": "LIMA INDIA MIKE ALPHA",
        "M": "MIKE INDIA KILO ECHO",
        "N": "NOVEMBER OSCAR VICTOR ECHO MIKE BRAVO ECHO ROMEO",
        "O": "OSCAR SIERRA CHARLIE ALPHA ROMEO",
        "P": "PAPA ALPHA PAPA ALPHA",
        "Q": "QUEBEC UNIFORM ECHO BRAVO ECHO CHARLIE",
        "R": "ROMEO OSCAR MIKE ECHO OSCAR",
        "S": "SIERRA INDIA ECHO ROMEO ROMEO ALPHA",
        "T": "TANGO ALPHA NOVEMBER GOLF OSCAR",
        "U": "UNIFORM NOVEMBER INDIA FOXTROT OSCAR ROMEO MIKE",
        "V": "VICTOR INDIA CHARLIE TANGO OSCAR ROMEO",
        "W": "WHISKEY HOTEL INDIA SIERRA KILO ECHO YANKEE",
        "X": "XRAY ROMEO ALPHA YANKEE",
        "Y": "YANKEE ALPHA NOVEMBER KILO ECHO ECHO",
        "Z": "ZULU UNIFORM LIMA UNIFORM"
    }
    extended_nato = {'A': 'Alfa Linux Foxtrot Alfa', 'B': 'Bravo Romeo Alfa Victor Oscar', 'C': 'Charlie Hotel Alfa Romeo Linux India Echo', 'D': 'Delta Echo Linux Tango Alfa', 'E': 'Echo Charlie Hotel Oscar', 'F': 'Foxtrot Oscar Xray Tango Romeo Oscar Tango', 'G': 'Golf Oscar Linux Foxtrot', 'H': 'Hotel Oscar Tango Echo Linux', 'I': 'India November Delta India Alfa', 'J': 'Juliett Uniform Linux India Echo Tango Tango', 'K': 'Kilo India Linux Oscar', 'L': 'Linux India November Uniform Xray', 'M': 'Mike India Kilo Echo', 'N': 'November Oscar Victor Echo Mike Bravo Echo Romeo', 'O': 'Oscar Sierra Charlie Alfa Romeo', 'P': 'Papa Alfa Papa Alfa', 'Q': 'Quebec Uniform Echo Bravo Echo Charlie', 'R': 'Romeo Oscar Mike Echo Oscar', 'S': 'Sierra India Echo Romeo Romeo Alfa', 'T': 'Tango Alfa November Golf Oscar', 'U': 'Uniform November India Foxtrot Oscar Romeo Mike', 'V': 'Victor India Charlie Tango Oscar Romeo', 'W': 'Whiskey Hotel India Sierra Kilo Echo Yankee', 'X': 'Xray Romeo Alfa Yankee', 'Y': 'Yankee Alfa November Kilo Echo Echo', 'Z': 'Zulu Uniform Linux Uniform'}    
    words = phonetic_text.split()
    result = []
    for word in words:
        for char in word.upper():
            if char in extended_nato:
                result.append(extended_nato[char])
            else:
                result.append(char)  # 알파벳과 숫자가 아닌 경우 그대로 추가
    return '  '.join(result)

# sample.txt 불러오기
def load_from_txt(filename):
    with open(filename, 'r') as file:
        return file.read()

# phonetic_output.txt로 저장
def save_to_txt(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# S로 치환
def replace_with_s(text):
    return ''.join('S' if char.isalpha() else char for char in text)

# 파일 불러오기
input_text = load_from_txt("sample.txt")

# 결과물 변수
first_conversion = to_phonetic(input_text)
second_conversion = second_phonetic_conversion(first_conversion)
final_conversion = replace_with_s(second_conversion)

# txt 저장
save_to_txt("phonetic_output.txt", final_conversion)


# 결과물 출력
print("Original text:", input_text, '\n')
print("First conversion:", first_conversion, '\n')
print("Second conversion:", second_conversion, '\n')
print("Final conversion:", final_conversion)
