import sys
from collections import deque

set_num = int(sys.stdin.readline())

for i in range(set_num):
  # N : 문서의 개수를 나타냄
  # M : 몇번째에 놓여있는지를 나타냄
  N, M = list(map(int, input().split()))
  element_list = deque(map(int, input().split()))
 
  cnt = 0
  # 접근 방법 : queue
  while element_list:
    top = max(element_list)
    M -= 1
    queue_front = element_list.popleft()
    # max 아닌 경우 => end로 밀려나게 됨
    if top != queue_front:
      element_list.append(queue_front)
      if M < 0:
        M = len(element_list)-1
    else:
      cnt+=1
      if M == -1 :
        print(cnt)
        break
