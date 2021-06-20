import sys
sys.stdin=open("input.txt","rt")
T=int(input())
for t in range(T):
    n, s, e, k= map(int,input().split())
    a=list(map(int,input().split()))
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1,a[k-1]))

# 추가 코드
# import sys
# sys.stdin = open('input.txt','r')
# n= int(sys.stdin.readline())
# for i in range(n):
#     _,s,e,k = map(int,sys.stdin.readline().split())
#     lis = list(map(int,sys.stdin.readline().split()))
#     res = sorted(lis[s-1:e])[k-1]
#     print('# {0} {1}'.format(i+1,res))

'''
설명 입력예제 1기준으로 input()은 파일에서 데이터를 읽을 때,
한줄씩 읽게 된다. 여기서 for문 T로 2가 오고, 다음 n,s,e,k에 6 2 5 3이
들어오며 그 다음 a에 5 2 7 3 8 9가 들어오고, 나머지 아래의 코드를 실행후
T가 2이니 0이 반복되고, 그 다음 1로 실행되어 다시 15 3 10 3을 n,s,e,k에 오고,
a에 4 15...15가 입력되어 for문이 실행된 뒤 마친다.
'''
