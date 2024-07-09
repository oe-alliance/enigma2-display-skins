from glob import glob

for filename in glob("./**/*.xml", recursive=True):
	newContent = []
	if "modify.py" in filename:
		continue
	try:
		content = open(filename, "r").read()
	except:
		print("Could not read", filename)
		continue
	if  'render="Picon"' in content:
		lines = [x for x in content.split("\n")]
		print("In file", filename)
		for line in lines:
			if 'render="Picon"' in line:
				line = line.replace(' alphatest="on"', '').replace(' alphatest="off"', '')
				line = line.replace('render="Picon"', 'render="Picon" alphatest="blend"')
					
			newContent.append(line)
		open(filename, "w").write("\n".join(newContent))
	