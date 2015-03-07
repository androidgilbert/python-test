from sys import argv
script,input_file=argv
def print_all(f):
	f.read()
def rewind(f):
	f.seek(0)
def print_a_line(line_count,f):
	print line_count,f.readline()
current_input=open(input_file)
print_all(current_input)
rewind(current_input)
current_line=1
print_a_line(current_line,current_input)
current_line=current_line+1
print_a_line(current_line,current_input)
current_line=current_line+1
print_a_line(current_line,current_input)