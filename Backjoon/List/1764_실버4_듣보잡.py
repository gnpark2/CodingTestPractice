"""
백준 1764 실버4 듣보잡

문제
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

출력
듣보잡의 수와 그 명단을 사전순으로 출력한다.

--------------------------------------------------------------

예제 입력 1 
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

예제 출력 1 
2
baesangwook
ohhenrie

"""

"""
1차 에러 - 시간초과
이중반복문에서 시간초과 발생

N, M = map(int, input().split())

not_heard = []
not_seen = []
not_heard_seen = []

for _ in range(N):
    not_heard.append(input())

for _ in range(N+2, N+2+M):
    not_seen.append(input())

for i in range(len(not_heard)):
    for j in range(len(not_seen)):
        if not_heard[i] == not_seen[j]:
            not_heard_seen.append(not_heard[i])

not_heard_seen.sort()

print(len(not_heard_seen))
for i in range(len(not_heard_seen)):
    print(not_heard_seen[i])

"""

# set의 교집합을 활용한 풀이
N, M = map(int, input().split())

not_heard = set()
not_seen = set()

for _ in range(N):
    not_heard.add(input())

for _ in range(M):
    not_seen.add(input())

not_heard_seen = sorted(not_heard & not_seen)

print(len(not_heard_seen))
for name in not_heard_seen:
    print(name)
