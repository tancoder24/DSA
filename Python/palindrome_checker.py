N = int(input())
Str = input()
M = int(input())
lSet = set( map(int, input().split()) )
count = 0

for l in lSet:
    i = 0
    j = l

    while( j <= N ):
        if Str[i:j] == Str[i:j][::-1]:
            count += 1
        i += 1
        j += 1

print(count)
