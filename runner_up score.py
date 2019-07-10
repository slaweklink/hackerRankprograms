n = int(input())
arr = map(int, input().split())

arr1 = list(set(arr))
arr1 = sorted(arr1)
print(arr1[-2])
