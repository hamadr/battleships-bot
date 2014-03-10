#! /bin/python

import json
import sys
import random

if len(sys.argv) != 2:
	print "Expected one argument";
	exit(0)

jsonInStr = str(sys.argv[1])
jsonIn = None
try:
	jsonIn = json.loads(jsonInStr)
except:
	print "Could not decode JSON from argument"
	exit(0)

cmdStr = str(jsonIn["cmd"])

jsonOutDic = dict()

board = [
		 [0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0]
	    ]


if cmdStr == "init":
	#initialize the grid
	generating = 2
	while generating <= 5:
		orientation = random.randint(0, 1)
		x = 0
		y = 0

		if orientation == 0:
			#h
			x = random.randint(0, 6)
			y = random.randint(0, 6 - generating)
		else:
			#v
			x = random.randint(0, 6 - generating)
			y = random.randint(0, 6)

		toFill = generating
		if orientation == 0:
			#horizontal
			for c in range(y, y + generating):
				if board[x][c] != 0:
					break
				else:
					toFill -= 1
			if toFill != 0:
				continue
			for c in range(y, y + generating):
				board[x][c] = 1
		else:
			#vertical
			for c in range(x, x + generating):
				if board[c][y] != 0:
					break
				else:
					toFill -= 1
			if toFill != 0:
				continue
			for c in range(x, x + generating):
				board[c][y] = 1
		orientationStr = "horizontal" if (orientation == 0) else "vertical"
		jsonOutDic[str(generating)] = dict([("pos", str(x) + str(y)), ("orientation", orientationStr)])
		generating += 1

elif cmdStr == "move":
	x = random.randint(0, 6)
	y = random.randint(0, 6)
	jsonOutDic["move"] = str(x) + str(y)
print json.dumps(jsonOutDic)
