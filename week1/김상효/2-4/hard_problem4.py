completion = ["josipa", "filipa", "marina", "nikola"]
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]


def solution(participant, completion):
    idx = 0
    participant.sort()
    completion.sort()

    if len(completion) == 0:
        answer = participant[0]
    else:
        for i in range(len(completion)):

            if(completion[i] != participant[i]):
                answer = participant[i]
                break
            idx = i

    if idx == len(completion) - 1:
        answer = participant[idx + 1]
    return answer
