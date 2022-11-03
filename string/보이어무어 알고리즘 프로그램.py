def index(c):
     if ord(c) == 32: return 0
     else: return ord(c)-64
def initSkip(p):
     M = len(p)
     for i in range(NUM):
         skip[i] = M
     for i in range(M):
         skip[index(p[i])] = M - i - 1
def BM(p, t, s):
     M = len(p)
     N = len(t) - 1
     initSkip(p)
     i = s + M - 1
     j = M - 1
     if i >= N: return N
     while j >= 0:
         while t[i] != p[j]:
             k = skip[index(t[i])]
             if M - j > k: i += M - j
             else: i += k
             if i >= N: return N
             j = M - 1
         i -= 1
         j -= 1
     return i + 1
NUM = 27
skip = [0] * NUM
text = 'STRING STARTING CONSISTING' + '\0'
pattern = 'STING'
m = len(pattern)
n = len(text)
start = 0
while True:
     position = BM(pattern, text, start)
     start = position + 1
     if start <= n - m: print('패턴이 나타난 위치 : ', position)
     else: break
print('스트링탐색종료') 
