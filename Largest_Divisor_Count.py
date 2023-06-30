n = int(input())
num_list = []
dic = {}
dic2 = {}
dic3 = []
lisv = []
x = 1
t = 0
num_list.append(n)

while x != 20:
    n = int(input())
    x += 1
    num_list.append(n)
    num_list.sort()

for i in num_list:
    for l in range(1, i + 1):
        if i % l == 0:
            t += 1

    dic[i] = t
    dic3.append(t)
    t = 0

lisv = list(dic.values())
lisv.sort()
lisk = list(dic.keys())
liskv = [(i, dic[i]) for i in lisk]
liskv.sort()
dic2 = dict(liskv)
p = lisv[-1]

result = f"Number with Largest Divisors: {liskv[-1][0]}\nCount of Divisors: {dic2[liskv[-1][0]]}"
print(result)