phone_book = ["123", "456", "789"]
phone_book2 = ["12", "123", "1235", "567", "88"]
phone_book3 = ["119", "97674223", "1195524421"]
# zip 함수 사용 가능

# 1)


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        val = phone_book[i]
        compared_val = phone_book[i+1]
        if val == compared_val[:len(val)]:
            return False
    return True

# 2)
# def solution(phone_book):
#     phone_book.sort()
#     for i in range(len(phone_book) - 1):
#         if phone_book[i] in phone_book[i+1]:
#             if(phone_book[i+1].find(phone_book[i]) == 0):
#                 return False
#     return True


print(solution(phone_book))
