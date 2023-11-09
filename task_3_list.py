m = int(input())
n = int(input())
arr = list(map(int, input().split()))

num_boats = [0] * n

arr.sort(reverse=True)


for i in range(n):
    for j in range(m):
        if num_boats[i] < n and arr[i] <= j:
            num_boats[i] += 1

print(max(num_boats))
