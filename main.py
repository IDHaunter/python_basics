_l = [x for x in range(10) if x % 2 == 0]
print(f"list comprehension: {_l}")

d = {}

for i in range(10):
    d[i] = str(i)

dd = {i: str(i) for i in d.values()}
print(f"dict: {d}")
print(f"dict comprehension: {dd}")

s = 'separator'
ls = [f" {value} " for value in _l]

j = s.join(ls)
print(f"join: {j}")
