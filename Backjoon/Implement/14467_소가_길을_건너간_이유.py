"""
백준 14467번: 브론즈1 소가 길을 건너간 이유

문제
닭이 길을 건너간 이유는 과학적으로 깊게 연구가 되어 있지만, 의외로 소가 길을 건너간 이유는 거의 연구된 적이 없다. 이 주제에 관심을 가지고 있었던 농부 존은 한 대학으로부터 소가 길을 건너는 이유에 대한 연구 제의를 받게 되었다.

존이 할 일은 소가 길을 건너는 것을 관찰하는 것이다. 존은 소의 위치를 N번 관찰하는데, 각 관찰은 소의 번호와 소의 위치 하나씩으로 이루어져 있다. 존은 소를 10마리 가지고 있으므로 소의 번호는 1 이상 10 이하의 정수고, 소의 위치는 길의 왼쪽과 오른쪽을 의미하는 0과 1 중 하나다.

이 관찰 기록을 가지고 소가 최소 몇 번 길을 건넜는지 알아보자. 즉 같은 번호의 소가 위치를 바꾼 것이 몇 번인지 세면 된다.

입력
첫 줄에 관찰 횟수 N이 주어진다. N은 100 이하의 양의 정수이다. 다음 N줄에는 한 줄에 하나씩 관찰 결과가 주어진다. 관찰 결과는 소의 번호와 위치(0 또는 1)로 이루어져 있다.

출력
첫 줄에 소가 길을 건너간 최소 횟수를 출력한다.

--------------------------------------------------------------

예제 입력 1 
8
3 1
3 0
6 0
2 1
4 1
3 0
4 0
3 1
예제 출력 1 
3


"""

"""
딕셔너리 정리

선언 : dictonary = {"apple": 3, "banana": 5, "orange": 7}
선언 : dictionary = dict(apple=3, banana=5,orange=7)
리스트로부터 선언 : 
    fruit_names = ["apple", "banana", "orange"]
    fruit_counts = [3, 5, 7]
    dictionary = dict(zip(fruit_names, fruit_counts))
빈 딕셔너리 선언 : dictionary = {}

특정 키 값 접근 : dictonary["apple"]

수정 : dictonary["apple"] = 10

추가 : dictonary["grape"] = 9

키 삭제 : del dictonary["apple"]

키 삭제 및 반환 : dictonary.pop("apple")

키 확인 : if "apple" in dictionary:
            print("존재")

get()메서드 확용 : a = dictionary.get("apple", 0)
                    print(a)
                결과 : 3
뒤의 0 은 키가 존재하지 않으면 기본값으로 0을 가져옴
                b = dictionary.get("peach", 8)
                    print(b)
                결과 : 8

모든 키와 값에 접근 :
키 가져오기 : keys = dictionary.keys()
값 가져오기 : values = dictionary.values()
키와 값 모두 가져오기 : items = dictionary.items()

"""

import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
cow = dict()

for _ in range(N):
    x, y = map(int, input().split())
    if x not in cow:
        cow[x] = y
    else :
        if cow.get(x) != y:
            cow[x] = y
            cnt += 1

print(cnt)