def solution(new_id):
    new_id = new_id.lower()
    char = "~!@#$%^&*()=+[{]}:?,<>/"
    string = ""

    #1, 2
    for x in char:
        new_id = new_id.replace(x, "")

    # 3
    id_list = new_id.split(".")
    for i in id_list:
        if i != "":
            string = string + "." + i

    # 5
    # 3의 조건을 처리했을 때 빈 문장이 생기는 경우 4의 조건 체크에서 out of index 에러가 나기 때문에 5 조건 미리 처리
    if(string == ""):
        string += "a"

    # 4
    if string[0] == ".":
        # 3의 조건을 처리하면 string 값이 "."이 될 수는 없지만 혹시 몰라 예외처리
        string = string[1:] if len(string) >= 2 else "."
    # 3의 조건을 처리하면 string 맨 마지막에 "."이 올 수 없지만 혹시 몰라 처리
    if string[-1] == ".":
        string = string[:-1]

    # 6
    if(len(string) >= 16):
        string = (string[:15])
        if string[-1] == ".":
            string = string[:-1]

    # 7
    while(len(string) <= 2):
        string += string[-1]

    print(string)


solution("=.=")
