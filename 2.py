f = [1,2]
total = 2

while sum(f) < 4000000:
    nextitem = sum(f)
	if nextitem % 2 == 0:
        total += nextitem
    f = [f[1], nextitem]

print total
