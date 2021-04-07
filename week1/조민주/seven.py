def seven():
  word=input().lower()
  words=list(word)
  #리스트key부분만들기
  alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  lists=[]
  #리스트value부분만들기
  for i in range(26):
      c=words.count(alpha[i])
      lists.append(c)
  #딕셔너리로 대응시키기
  solution= {x:y for x,y in zip(alpha,lists)}
  #key로 가장 많이 나온 알파벳 찾기
  max_sol=max(solution,key=solution.get)
  number=solution[max_sol]
  #두번이상 나온 알파벳 거르기
  add=0   
  for value in solution.values():
    if (number == value):
      add=add+1
  if (add>1):
    print ("?")
  else:
    print (max_sol.upper())

seven()