stack = []
test = 'tacoca'

def solution(str):
    new = ''
    for i in str.lower(): 
        if i in 'abcdefghijklmnopqrstuvwxyz1234567890':
            new.append(i)

    return new == new[::-1]
# print(solution(test))

def solution2(str1, str2):   
    bank = {}
    for i in str1:
        if i not in bank.keys():
            bank[i] = 1
        else:
            bank[i] += 1
            
    for j in str2:
        if j not in bank.keys():
            return False
        else:
            if bank[j] != 0:
                bank[j] -= 1
            else:
                return False
    print(bank)
    return sum(bank.values()) == 0

print(solution2("aacc", "ccac"))  # Expected: false