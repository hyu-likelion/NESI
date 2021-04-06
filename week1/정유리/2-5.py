phone_book = ["123","456","789"]	
def solution(phone_book):
    answer = True
    phone_book.sort()
    size = len(phone_book)
    for i in range(size - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            answer = False
            break
    return answer
PB = solution(phone_book)
print(PB)
