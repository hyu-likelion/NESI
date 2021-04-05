def solution(participant, completion):
    N=len(completion)
    participant.sort()
    completion.sort()
    for i in range(N):
        if (participant[i]==completion[i]):
            continue
        else:
            print (i)
            answer=participant[i]
            return answer
    
    answer = participant[-1]
    return answer