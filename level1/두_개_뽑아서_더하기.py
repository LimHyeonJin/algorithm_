def solution(numbers):
    answer = []
    for idx in range(len(numbers)):
        for idx2 in range(idx+1,len(numbers)):
            x = numbers[idx] + numbers[idx2]
            if x not in answer:
                answer.append(x)
    answer = sorted(answer)           
    return answer
