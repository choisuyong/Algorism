# 문자열 재정렬
# 알파벳 대문자와 숫자로만 구성된 문자열을 이하의 기준에 맞추어 재정렬 하시오
# ----- 기준
# 1. 알파벳을 오름차순으로 정렬
# 2. 오름차순으로 정렬된 알파벳 뒤에 숫자를 더한값을 출력

string = input()
result = []
num = 0
for char in string :
    if char.isalpha() :
        result.append(char)
    else :
        num += int(char)

result.sort()
if num != 0 :
    result.append(str(num))

print(''.join(result))
