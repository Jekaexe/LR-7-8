a = input()
b = []
c = []
for i in range(len(a)):
    if "x" not in a or "w" not in a:
        print('Символа нет')
        break
for i in range(len(a)):
    if a[i] == "x":
        b.append(i)
    if a[i] == "w":
        c.append(i)
if b > c:
    print('Раньше встречается w')
elif c > b:
    print('Раньше встречается x')

