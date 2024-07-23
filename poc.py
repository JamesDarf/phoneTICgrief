import os

# 원본 데이터
extended_nato = {'A': 'Alfa Linux Foxtrot Alfa', 'B': 'Bravo Romeo Alfa Victor Oscar', 'C': 'Charlie Hotel Alfa Romeo Linux India Echo', 'D': 'Delta Echo Linux Tango Alfa', 'E': 'Echo Charlie Hotel Oscar', 'F': 'Foxtrot Oscar Xray Tango Romeo Oscar Tango', 'G': 'Golf Oscar Linux Foxtrot', 'H': 'Hotel Oscar Tango Echo Linux', 'I': 'India November Delta India Alfa', 'J': 'Juliett Uniform Linux India Echo Tango Tango', 'K': 'Kilo India Linux Oscar', 'L': 'Linux India November Uniform Xray', 'M': 'Mike India Kilo Echo', 'N': 'November Oscar Victor Echo Mike Bravo Echo Romeo', 'O': 'Oscar Sierra Charlie Alfa Romeo', 'P': 'Papa Alfa Papa Alfa', 'Q': 'Quebec Uniform Echo Bravo Echo Charlie', 'R': 'Romeo Oscar Mike Echo Oscar', 'S': 'Sierra India Echo Romeo Romeo Alfa', 'T': 'Tango Alfa November Golf Oscar', 'U': 'Uniform November India Foxtrot Oscar Romeo Mike', 'V': 'Victor India Charlie Tango Oscar Romeo', 'W': 'Whiskey Hotel India Sierra Kilo Echo Yankee', 'X': 'Xray Romeo Alfa Yankee', 'Y': 'Yankee Alfa November Kilo Echo Echo', 'Z': 'Zulu Uniform Linux Uniform'}

# 변환된 데이터 (A를 S로 변경)
transformed_data = {'A': 'SSSS SSSSS SSSSSSS SSSS', 'B': 'SSSSS SSSSS SSSS SSSSSS SSSSS', 'C': 'SSSSSSS SSSSS SSSS SSSSS SSSSS SSSSS SSSS', 'D': 'SSSSS SSSS SSSSS SSSSS SSSS', 'E': 'SSSS SSSSSSS SSSSS SSSSS', 'F': 'SSSSSSS SSSSS SSSS SSSSS SSSSS SSSSS SSSSS', 'G': 'SSSS SSSSS SSSSS SSSSSSS', 'H': 'SSSSS SSSSS SSSSS SSSS SSSSS', 'I': 'SSSSS SSSSSSSS SSSSS SSSSS SSSS', 'J': 'SSSSSSS SSSSSSS SSSSS SSSSS SSSS SSSSS SSSSS', 'K': 'SSSS SSSSS SSSSS SSSSS', 'L': 'SSSSS SSSSS SSSSSSSS SSSSSSS SSSS', 'M': 'SSSS SSSSS SSSS SSSS', 'N': 'SSSSSSSS SSSSS SSSSSS SSSS SSSS SSSSS SSSS SSSSS', 'O': 'SSSSS SSSSSS SSSSSSS SSSS SSSSS', 'P': 'SSSS SSSS SSSS SSSS', 'Q': 'SSSSSS SSSSSSS SSSS SSSSS SSSS SSSSSSS', 'R': 'SSSSS SSSSS SSSS SSSS SSSSS', 'S': 'SSSSSS SSSSS SSSS SSSSS SSSSS SSSS', 'T': 'SSSSS SSSS SSSSSSSS SSSS SSSSS', 'U': 'SSSSSSS SSSSSSSS SSSSS SSSSSSS SSSSS SSSSS SSSS', 'V': 'SSSSSS SSSSS SSSSSSS SSSSS SSSSS SSSSS', 'W': 'SSSSSSS SSSSS SSSSS SSSSSS SSSS SSSS SSSSSS', 'X': 'SSSS SSSSS SSSS SSSSSS', 'Y': 'SSSSSS SSSS SSSSSSSS SSSS SSSS SSSS', 'Z': 'SSSS SSSSSSS SSSSS SSSSSSS'}
ponetic_code = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
        'K': 'Kilo', 'L': 'Linux', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee',
        'Z': 'Zulu',
    }

# input data
second_data = open("./phonetic_output.txt").read()


codes = second_data.split("  ")
string = "" # result matching "HELLO"

for code in codes:
    for k, v in transformed_data.items():
        if code == v:
            string += k
            break
    # string += " "
print(f"string: {string}")

letters = string
result = ""
index = 0
while index < len(letters):
     for k, v in ponetic_code.items():
        if letters[index:index+len(v)] == v.upper():
            result += k
            index = index + len(v)
            break

# for letter in letters:
#     for k, v in ponetic_code.items():
#         if letter == v.upper():
#             result += v
#             break

print(f"result: {result}")

