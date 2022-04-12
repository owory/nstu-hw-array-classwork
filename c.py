a = list(map(int, input().split()))
print(sum([i for i in a if i % 10 == 5]) / len([i for i in a if i % 10 == 5]))
