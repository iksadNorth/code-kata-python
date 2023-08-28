def solution(s):
    answer, flag = list(s), True
    for idx, i in enumerate(answer):
        answer[idx] = i.upper() if flag else i.lower()
        flag = i==' '
    return "".join(answer)