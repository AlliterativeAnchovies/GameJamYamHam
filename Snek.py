
snekPosition = [0,0]

def moveSnek(x, y):
	snekPosition[0] += x
	snekPosition[1] += y
	print("Snek moved", x, y)