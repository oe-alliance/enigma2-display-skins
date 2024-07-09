from glob import glob

for filename in glob("./**/*.xml", recursive=True):
	if "modify.py" in filename:
		continue
	try:
		content = open(filename, "r").read()
	except:
		print("Could not read", filename)
		continue
	if  'name="MessageBox_summary"' in content:
		open(filename, "w").write(content.replace('name="MessageBox_summary"', 'name="MessageBoxSummary"'))
	