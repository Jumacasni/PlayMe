import subprocess

def test():
	subprocess.run(
		['pytest', 'playme/test']
	)