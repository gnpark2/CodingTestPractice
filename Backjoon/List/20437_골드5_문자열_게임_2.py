"""
백준 20437번: 골드5 문자열 게임 2

문제
작년에 이어 새로운 문자열 게임이 있다. 게임의 진행 방식은 아래와 같다.

알파벳 소문자로 이루어진 문자열 W가 주어진다.
양의 정수 K가 주어진다.
어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
위와 같은 방식으로 게임을 T회 진행한다.

입력
문자열 게임의 수 T가 주어진다. (1 ≤ T ≤ 100)

다음 줄부터 2개의 줄 동안 문자열 W와 정수 K가 주어진다. (1 ≤ K ≤ |W| ≤ 10,000) 

출력
T개의 줄 동안 문자열 게임의 3번과 4번에서 구한 연속 문자열의 길이를 공백을 사이에 두고 출력한다.

만약 만족하는 연속 문자열이 없을 시 -1을 출력한다.

--------------------------------------------------------------

예제 입력 1 
2
superaquatornado
2
abcdefghijklmnopqrstuvwxyz
5
예제 출력 1 
4 8
-1
첫 번째 문자열에서 3번에서 구한 문자열은 aqua, 4번에서 구한 문자열은 raquator이다.

두 번째 문자열에서는 어떤 문자가 5개 포함된 문자열을 찾을 수 없으므로 -1을 출력한다.

예제 입력 2 
1
abaaaba
3
예제 출력 2 
3 4

"""

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    W = input().rstrip()
    K = int(input())
    char_dict = {}

    for i in range(len(W)):
        if W[i] in char_dict:
            char_dict[W[i]].append(i)
        else:
            char_dict[W[i]] = [i]
        
    min_len = 0
    max_len = 0

    for char in char_dict:
        if len(char_dict[char]) < K:
            continue
        
        for i in range(len(char_dict[char]) - K + 1):
            start = char_dict[char][i]
            end = char_dict[char][i + K - 1]
            length = end - start + 1
            
            if min_len == 0 or length < min_len:
                min_len = length
            if length > max_len:
                max_len = length
            
    if min_len == 0 or max_len == 0:
        print(-1)
    else:
        print(min_len, max_len)