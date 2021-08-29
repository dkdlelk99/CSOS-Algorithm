from collections import deque

N = int(input())

q = deque([i for i in range(1, N+1)])

"""
전형적인 큐 문제
1. 제일 위 카드 버리기
- 큐에서 제거
2. 그 다음 카드 제일 아래로 옮기기
- 큐에서 제거 후 추가
"""

while len(q) > 1:
  q.popleft()
  q.append(q.popleft())

print(q.pop())