def bruteForce(p, t, s):
     M = len(p)
     N = len(t)
     i = s
     j = 0
     while j < M and i < N:
         if t[i] != p[j]:
             i -= j
             j = -1
         i += 1
         j += 1
     if j == M: return i - M
     else: return i
text = 'ababacabcbababcacacbcaababca' + '\0'
pattern = 'ababca'
m = len(pattern)
n = len(text)
start = 0
while True:
     position = bruteForce(pattern, text, start)
     start = position + 1
     if start <= n - m:
         print('패턴이 나타난 위치 : ', position)
     else: break
print('스트링 탐색 종료') 
