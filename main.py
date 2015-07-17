import sys
import string

if __name__ == "__main__":
	t1 = ""
	t2 = ""
	t3 = ""
	t4 = ""

	try:
		print "Input dict is " + sys.argv[1]
	except:
		print "Need 3 args at least(0 given)!"
		print "Usage: ", sys.argv[0], " <input dict1> <output dict2> <output dict3> [separator]"
		print "Exit!"
		exit(-1)
	else:
		t1 = sys.argv[1]

	try:
		print "Output dict 1 is " + sys.argv[2]
	except:
		print "Need 3 args at least(1 given)!\nExit!"
		exit(-1)
	else:
		t2 = sys.argv[2]

	try:
		print "Output dict 2 is " + sys.argv[3]
	except:
		print "Need 3 args at least(2 given)!\nExit!"
		exit(-1)
	else:
		t3 = sys.argv[3]

	try:
		print "Separator is " + sys.argv[4]
	except:
		print "Separator is blank"
	else:
		t4 = sys.argv[4]

	with open(t1, 'r') as f1, open(t2, 'w+') as f2, open(t3, 'w+') as f3:
		f1len = len(f1.read())
		f1.seek(0)
		if f1len == 0:
			print "Input dict is empty!"
			exit(0)
		else:
			f1data = []
			f2data = []
			f3data = []
			fdataline = ""
			while(True):
				fdataline = f1.readline()
				if not fdataline:
					break
				fdataline = fdataline.strip()
				if t4 != "":
					f1data = string.split(fdataline, t4, 1)
				else:
					f1data = string.split(fdataline, maxsplit=1)
				f2data.append(f1data[0])
				f3data.append(f1data[1])
			f2data = sorted(list(set(f2data)))
			f3data = sorted(list(set(f3data)))
			f2.write(string.join(f2data, "\n"))
			f3.write(string.join(f3data, "\n"))
