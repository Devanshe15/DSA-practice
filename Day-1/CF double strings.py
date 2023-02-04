for _ in range(int(input())):
	n = int(input())
	ss = [input() for _ in range(n)]
	d = {x: True for x in ss}
	for s in ss:
	
		ok = 0
		for i in range(1, len(s)):
			if d.get(s[:i]) and d.get(s[i:len(s)]):
				ok=1
		print(ok, end='')
	print()