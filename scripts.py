import subprocess

def test():
	subprocess.run(
		['pytest', 'tests']
	)