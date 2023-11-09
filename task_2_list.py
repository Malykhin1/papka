n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] = arr[(i+n-1)%n]
for num in arr:
    print(num)

