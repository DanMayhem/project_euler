#!python
"""
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""
#no 4, 5
keylog = list(map(int, """319 680 180 690 129 620 762 689 762 318 368 710 720 710 629 168 160 689 716 731 736 729 316 729 729 710 769 290 719 680 318 389 162 289 162 718 729 319 790 680 890 362 319 760 316 729 380 319 728 716""".split()))

def is_code_for(p, m):
	i, j, k = list(map(int, list(str(p))))
	m = list(map(int, list(str(m))))
	try:
		ii = m.index(i)
		m = m[ii+1:]
		jj = m.index(j)
		m = m[jj+1:]
		kk = m.index(k)
		return True
	except ValueError:
		return False

def test_password(p):
	for k in keylog:
		if not is_code_for(k, p):
			return False
	return True

for i in range(71236890, 79863210, 10):
	print(i)
	if test_password(i):
		print("found: {0}".format(i))
		exit()
print("failed")



