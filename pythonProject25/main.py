data = list(input().split(" "))
while "" in data:
    data.remove("")

a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])

if d <= b:
    print(a)
else:
    print(a + (d - b) * c)



data = list(input().split(" "))
while "" in data:
    data.remove("")
if data[1] >= data[3]:
    print(int(data[0]))
else:
    print(int(data[0]) + (int(data[3]) - int(data[1])) * int(data[2]))