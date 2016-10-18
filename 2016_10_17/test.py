import os
import sys

ready = True
if ready:
    result = os.popen("python code.py").read()
else:
    result = os.popen("python solution.py").read()

result = result.strip().split('\n')
expected = open('solution.txt', 'rt', encoding='utf-8').read().strip().split('\n')
assert len(result) == len(expected)
for i in range(len(result)):
	sys.stdout.write('.')
	if result[i] != expected[i]:
		sys.stdout.write('\n')
		print("Error on line " + str(i))
		quit()
sys.stdout.write('\n')
print("All tests passed!")
