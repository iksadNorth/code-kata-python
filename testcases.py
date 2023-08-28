from solution import solution

# dict[테스트케이스 : 정답]
testcases = {
    "3people unFollowed me": "3people Unfollowed Me",
    "for the last week" : "For The Last Week",
}

for idx, (testcase, answer) in enumerate(testcases.items()):
    result = solution(testcase)
    correction = "O" if result == answer else "X"
    
    print(f"{idx+1}번째 테스트 케이스 : {correction}")
