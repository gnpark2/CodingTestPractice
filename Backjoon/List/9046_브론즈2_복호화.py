"""
백준 9046번 복호화

문제
암호학에서 치환 암호(substitution cipher)란, 평문에 들어있는 각각의 문자를 주어진 치환 방법으로 암호화하는 방법 중 하나다.

가장 단순한 방법은 평문의 알파벳을 암호문의 알파벳으로 대치시켜 치환시키는 것이다.

예를 들어, 아래와 같은 알파벳 대치표가 주어졌다고 하자.

평문 알파벳 대치표 : abcdefghijklmnopqrstuvwxyz
암호문 알파벳 대치표 : wghuvijxpqrstacdebfklmnoyz
위에 주어진 치환 방법을 통해 암호화하면 평문 "hello there"은 "xvssc kxvbv"가 된다.

한 가지 흥미로운 점은 영어 문법 특성상, 알파벳 'e'가 다른 영문 알파벳에 비해 자주 쓰인다는 것이다.

즉, 암호문 알파벳 대치표 없이 암호문을 복호화하려 할 때, 암호문 알파벳 빈도수를 체크하면 암호문 알파벳 빈도수 중 가장 빈번하게 나타나는 알파벳이 'e'라는 사실을 유추해볼 수 있다.

위 방법으로 암호문 알파벳의 빈도수를 체크하고, 가장 빈번하게 나타나는 문자를 출력하는 프로그램을 작성하면 된다.

만약 주어진 암호문에서 가장 빈번하게 나타나는 문자가 여러 개일 경우, 그 빈번한 문자 중 어느 것이 평문 알파벳 'e'를 가리키는지 확실하게 알 수 없기 때문에 "모르겠음"을 의미하는 '?'를 출력하면 된다.

입력
입력의 T(1 ≤ T ≤ 20)는 테스트 케이스로, 입력 제일 상단에 주어진다. 각각의 테스트 케이스는 한 줄마다 소문자와 공백으로 이루어진 영어 문장이 주어진다. 이 문장의 길이는 적어도 1이상이며 255이하다.

출력
각각의 테스트 케이스에 대해, 가장 빈번하게 나타나는 문자를 출력하거나 빈번하게 나타나는 문자가 여러 개일 경우 '?'를 출력한다.

--------------------------------------------------------------

예제 입력 1 
3
asvdge ef ofmdofn
xvssc kxvbv
hull full suua pmlu

예제 출력 1 
f
v
?

"""

encrypt = []

T = int(input())

for i in range(T):
    encrypt = input()

    encrypt = encrypt.replace(" ","")

    used_alphabet = set(encrypt)
    cnt = []
    
    for j in range(0, len(used_alphabet)):
        cnt.append(encrypt.count(list(used_alphabet)[j]))

    if cnt.count(max(cnt)) > 1:
        print("?")
    else:
        print(list(used_alphabet)[cnt.index(max(cnt))])