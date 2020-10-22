n = int(input())
m = 0
arr = []
while m < n:
	arr.append(int(input())


i = 1
sec_big = arr[0]
while i < n:
    if sec_big < arr[i]:
        sec_big = arr[i]
    i += 1

i = 0
li = []
while i < n:
    if sec_big == arr[i]:
       li.append(i)
    i += 1

copy = []
for i in arr:
    copy.append(i)

i = 0
while i < len(li) - 1:
    li[i+1] = li[i+1] - 1
    del copy[li[i]]
    i += 1

del copy[li[i]]

print(copy)

i = 0
sec_big = copy[0]
while i < len(copy):
    if sec_big < copy[i]:
        sec_big = copy[i]
    i += 1

print(sec_big)
