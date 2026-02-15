from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start]) 
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# Dictionary

from collections import deque

def bfs(start_node, graph):
    queue = Deque([start_node])
    visited = set([start_node])

    while queue:
        current_node = queue.popleft()

        for next_node in graph[current_node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)

    return -1


# 2D Array

from collections import deque

def bfs(start_x, start_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return -1


# 미로 문제 해결법 : 지나가는 길에 최소 이동 거리를 입력하면서 이동하기

def bfs(current_x, current_y, final_x, final_y):
    queue = deque([(current_x, current_y)])
    
    while queue:
        current_x, current_y = queue.popleft()

        for dx, dy in directions:
            nx, ny = current_x + dx, current_y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[current_x][current_y] + 1 # 최소 거리 수 입력
                    queue.append((nx, ny))

                if current_x == final_x and current_y == final_y:
                    return graph[current_x][current_y]
                    break
