n = int(input())
names = dict()

for i in range(n):
    name = input()
    if name not in names:
        print('OK')
        names[name] = 1
    else:
        num = names[name]
        print(name+str(num))
        names[name] = num + 1
