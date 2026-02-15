"""
백준 7562번: 실버1 나이트의 이동
문제
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?



입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

--------------------------------------------------------------

예제 입력 1 
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
예제 출력 1 
5
28
0

"""

"""
미로 최단 거리 찾기 문제와 유사한 풀이
갈 수 있는 방향 directions 선언
길에 최소 이동 수를 대입하면서 진행
현재 위치를 매개변수로 받고 최종 위치까지의 최소 이동 수 return
"""

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
graph = []
directions = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
curr_x, curr_y = 0, 0
final_x, final_y = 0, 0
N = 0

def bfs(x, y):
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

                if x == final_x and y == final_y:
                    return graph[x][y]
                    break

for _ in range(T):
    N = int(input())
    graph = [[0]*N for _ in range(N)]
    curr_x, curr_y = map(int, input().split())
    final_x, final_y = map(int, input().split())

    print(bfs(curr_x, curr_y))