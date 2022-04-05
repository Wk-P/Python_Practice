l = [10, 11, 5, 6]
lp = ['A', 'B', 'C', 'D']

max = 0

if l[0] > l[1]:
	max = 0
	if l[max] < l[2]:
		max = 2
		if l[max] < l[3]:
			max = 3
else:
	max = 1
	if l[max] < l[2]:
		max = 2
		if l[max] < l[3]:
			max = 3
lp.append(max)
l[max] = -1

if l[0] > l[1]:
	max = 0
	if l[max] < l[2]:
		max = 2
		if l[max] < l[3]:
			max = 3
else:
	max = 1
	if l[max] < l[2]:
		max = 2
		if l[max] < l[3]:
			max = 3

lp.append(max)
l[max] = -1

if l[0] > l[1]:
	max = 0
	if l[max] < l[2]:
		max = 2
		if l[max] < l[3]:
			max = 3
else:
	max = 1
	if l[max] < l[2]:
		max = 2
		if l[max] < l[3]:
			max = 3

lp.append(max)
l[max] = -1

if l[0] > l[1]:
	max = 0
	if l[max] < l[2]:
		max = 2
		if l[max] < l[3]:
			max = 3
else:
	max = 1
	if l[max] < l[2]:
		max = 2
		if l[max] < l[3]:
			max = 3

lp.append(max)
l[max] = -1
print(lp[lp[4]], lp[lp[5]], lp[lp[6]], lp[lp[7]])
