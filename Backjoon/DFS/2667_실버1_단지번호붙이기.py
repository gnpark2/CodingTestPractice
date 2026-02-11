"""
백준 2667번: 실버1 단지번호붙이기

문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

--------------------------------------------------------------

예제 입력 1 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
예제 출력 1 
3
7
8
9

"""

"""
strip([chars]) : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거한다.
lstrip([chars]) : 인자로 전달된 문자를 String의 왼쪽에서 제거한다.
rstrip([chars]) : 인자로 전달된 문자를 String의 오른쪽에서 제거한다.

input().split()으로 하면 "01101".split()  →  ["01101"] 이처럼 하나의 정수로 인식되기 때문에
[01101] → [1101]   # 정수 하나만 들어감
input().rstrip()으로 문자열로 받아서 list()로 각각의 문자로 쪼개줘야 한다.

방향 리스트를 만들어 상하좌우를 확인한다.
count 변수를 전역변수로 선언하여 dfs 돌 때마다 1씩 증가시켜 단지 내 집의 수를 센다.
set_num 변수를 만들어 단지 번호를 매긴다.
stack 리스트에 단지 내 집의 수를 저장한 후 오름차순으로 정렬하여 출력한다.
"""
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
set_num = 1
stack = []

def dfs(x, y):
    if graph[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] = set_num
        global count
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                count += 1
                dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            count = 1
            dfs(i, j)
            set_num += 1
            stack.append(count)

stack.sort()
print(set_num - 1)
for num in stack:
    print(num)