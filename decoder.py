# 원본 데이터
original_data = {
    "A": "ALPHA LIMA PAPA HOTEL ALPHA",
    "B": "BRAVO ROMEO ALPHA VICTOR OSCAR",
    "C": "CHARLIE HOTEL ALPHA ROMEO LIMA INDIA ECHO",
    "D": "DELTA ECHO LIMA TANGO ALPHA",
    "E": "ECHO CHARLIE HOTEL OSCAR",
    "F": "FOXTROT OSCAR X-RAY TANGO ROMEO OSCAR TANGO",
    "G": "GOLF OSCAR LIMA FOXTROT",
    "H": "HOTEL OSCAR TANGO ECHO LIMA",
    "I": "INDIA NOVEMBER DELTA INDIA ALPHA",
    "J": "JULIET UNIFORM LIMA INDIA ECHO TANGO",
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

# 변환된 데이터 (A를 S로 변경)
transformed_data = {
    "SSSS SSSS SSSSSSS SSSS": "A",
    "SSSSS SSSSS SSSS SSSSSS SSSSS": "B",
    "SSSSSSS SSSSS SSSS SSSSS SSSS SSSSS SSSS": "C",
    "SSSSS SSSS SSSS SSSSS SSSS": "D",
    "SSSS SSSSSSS SSSSS SSSSS": "E",
    "SSSSSSS SSSSS SSSS SSSSS SSSSS SSSSS SSSSS": "F",
    "SSSS SSSSS SSSS SSSSSSS": "G",
    "SSSSS SSSSS SSSSS SSSS SSSS": "H",
    "SSSSS SSSSSSSS SSSSS SSSSS SSSS": "I",
    "SSSSSSS SSSSSSS SSSS SSSSS SSSS SSSSS SSSSS": "J",
    "SSSS SSSSS SSSS SSSSS": "K",
    "SSSS SSSSS SSSS SSSS": "M",
    "SSSSSSSS SSSSS SSSSSS SSSS SSSS SSSSS SSSSS": "N",
    "SSSSS SSSSSS SSSSSSS SSSS SSSSS": "O",
    "SSSS SSSS SSSS SSSS": "P",
    "SSSSSS SSSSSSS SSSS SSSSS SSSS SSSSSSS": "Q",
    "SSSSS SSSSS SSSS SSSS SSSSS": "R",
    "SSSSSS SSSSS SSSS SSSSS SSSS": "S",
    "SSSSS SSSS SSSSSSS SSSS SSSSS": "T",
    "SSSSSSS SSSSSSSS SSSS SSSSSSS SSSSS SSSSS SSSS": "U",
    "SSSSSS SSSSS SSSSSSS SSSS SSSSS SSSSS": "V",
    "SSSSSSS SSSSS SSSS SSSSS SSSS SSSSSS": "W",
    "SSSS SSSSS SSSS SSSSSS": "X",
    "SSSSSS SSSS SSSSSSS SSSS SSSS SSSS": "Y",
    "SSSS SSSSSSS SSSS SSSSSSS": "Z"
}

# 변환 함수
def convert_to_S(value):
    return ' '.join(word.replace('A', 'S') for word in value.split())

# 검증
def validate_transformation(original_data, transformed_data):
    correct = True
    for letter, phrase in original_data.items():
        transformed_phrase = convert_to_S(phrase)
        if transformed_phrase not in transformed_data:
            print(f"Error: Key '{transformed_phrase}' not found in transformed_data.")
            correct = False
        elif transformed_data[transformed_phrase] != letter:
            print(f"Error: Expected '{letter}' for '{transformed_phrase}', but got '{transformed_data[transformed_phrase]}'")
            correct = False
    return correct

# 검증 실행
if validate_transformation(original_data, transformed_data):
    print("All transformations are correct.")
else:
    print("Some transformations are incorrect.")
