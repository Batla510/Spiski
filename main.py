'''a = int(input())
b = int(input())
for i in range(a,b+1):
    print(i)'''

'''a = int(input())
b = int(input())
if a<b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)
        '''
'''n = int(input())
b = 0
for i in range(n):
    b += int(input())
print(b)'''
'''x = 1
n = int(input())
for i in range(1, n + 1):
    x *= i
print(x) '''

'''n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print() '''
'''n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1'''

'''n = int(input())
a = 2
b = 1
while a <= n:
    a *= 2
    b += 1
print(b - 1, a // 2)'''

'''x = int(input())
y = int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)'''
'''
len = 0
while int(input()) != 0:
    len += 1
print(len)'''
'''a = int(input())
b = 0
while a != 0:
    x = int(input())
    if x != 0 and a < x:
        b += 1
    a = x
print(b)'''

first_max = int(input())
second_max = int(input())
if first_max < second_max:
    first_max, second_max = second_max, first_max
element = int(input())
while element != 0:
    if element > first_max:
        second_max, first_max = first_max, element
    elif element > second_max:
        second_max = element
    element = int(input())
print(second_max)

'''
n = int(input()) 
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)
'''
'''
prev = -1 
curr_rep_len = 0
max_rep_len = 0
element = int(input())
while element != 0:
    if prev == element:
        curr_rep_len += 1
    else:
        prev = element
        max_rep_len = max(max_rep_len, curr_rep_len)
        curr_rep_len = 1
    element = int(input())
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)
'''
'''
a = input().split()
for i in range(0, len(a), 2):
    print(a[i])
'''
'''
a = [int(i) for i in input().split()] 
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])
'''
'''
index_of_max = 0  
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
print(a[index_of_max], index_of_max)
'''
'''
a = [int(i) for i in input().split()] 
x = int(input())
pos = 0
while pos < len(a) and a[pos] >= x:
    pos += 1
print(pos + 1)
'''
'''
a = [int(i) for i in input().split()] 
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))
'''
'''
a = [int(i) for i in input().split()]  
a[a.index(max(a))], a[a.index(min(a))] = a[a.index(min(a))], a[a.index(max(a))]
print(' '.join([str(i) for i in a]))
'''
'''
a = [int(s) for s in input().split()]  
k = int(input())
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(' '.join([str(i) for i in a]))
'''
'''
a = [int(s) for s in input().split()]  
k, C = [int(s) for s in input().split()]
a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(' '.join([str(i) for i in a]))
'''
'''
n = 8  
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)
'''
'''
correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')
'''