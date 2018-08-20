def f(n):
	if n==0:
		return [[]]
	a = [[1,2],[3,1]]
	for i in loop:
	loop = range(n, 0, -1)
	tmp = [tmp.append((i, f(n-i)))
	print(tmp)
	return [[i] + elem2 for (i, elem) in tmp for elem2 in elem]

	#  return [i + elem for (elem,i) in zip(loop, loop)]

if __name__ == "__main__":
	print(f(5))
