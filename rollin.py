import os
import time
tags = ["the", "agile", "rust-colored", "fox", "leaped", "above", "the", "moon"]
for o in range(0, len(tags)):
	tag = tags[o]
	for i in range(0, (len(tag) + 1) * 2):
		os.system("clear")
		if (i > len(tag) + 1):
			print(tag[:(((len(tag) + 1) * 2) - i)])
		else:
			print(tag[:i])
		time.sleep(.1)
