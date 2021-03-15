def read_file_content(path)->str:
	''' Read the content of the resourse file and returns it as a list of lines
	'''
	with open(path) as f:
		content = f.read()
		content = content.split("\n")
		content
		f.close()
	return [line for line in content if not is_comment_line(line)]


def is_comment_line(line:str)-> bool:
	'''Return True if line is a comment i.e. starts with #'''
	return line.startswith('#')