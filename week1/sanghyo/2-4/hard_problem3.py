# 간결하게 바꿔보기
string = input().upper()
set_string = list(set(string))
count = [0 for _ in range(len(set_string))]

i = 0
for char in set_string:
    count[i] = string.count(char)
    i += 1

max_char = max(count)
idx = count.index(max_char)
max_dup = 0

for i in range(len(count)):
    if max_char == count[i]:
        max_dup += 1

if max_dup > 1:
    print("?")
else:
    print("%s" % set_string[idx])
