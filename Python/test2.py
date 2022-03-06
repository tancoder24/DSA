total_volunters = input()
collection_by_volunter = list( map(int, input().split()) )

pairs = ["0"]

for _ in range(int(input())):
    x, y = input().split()
    for pair in pairs:
        if x in pair or y in pair:
            pair.update([x,y])
        else: 
            pairs.append(set([x,y]))

for pair in pairs:
    sum = 0
    for p in pair:
        sum += collection_by_volunter[p-1]
    if sum > max:
        max = sum
print(pairs)
print(max)