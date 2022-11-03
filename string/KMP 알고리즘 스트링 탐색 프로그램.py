def initNext(p):
     M = len(p)
     next[0] = -1
     i = 0
     j = -1
     while i < M:
         if j != -1 and p[i] == p[j]: next[i] = next[j]
         else: next[i] = j
         while j >= 0 and p[i] != p[j]:
             j = next[j]
         i += 1
         j += 1
def KMP(p, t, s):
     M = len(p)
     N = len(t)
     initNext(p)
     i = s
     j = 0
     while j < M and i < N:
         while j >= 0 and t[i] != p[j]:
             j = next[j]
         i += 1
         j += 1
     if j == M: return i - M
     else: return i
next = [0] * 50
text = 'ababacabcbababcacacaababca' + '\0'
pattern = 'ababca'
m = len(pattern)
n = len(text)
start = 0
while True:
     position = KMP(pattern, text, start)
     start = position + 1
     if start <= n - m: print('패턴이 나타난 위치: ', position)
     else: break
print('스트링 탐색 종료')
