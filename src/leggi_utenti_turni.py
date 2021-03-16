from src.help_functions import read_file_content

def leggi_utenti_turni()-> dict():
	file_content = read_file_content('./resources/turni_utenti')
	res_dict = {}
	for line in file_content:
		user,time,days = read_line_content(line)
		if user in res_dict:
			res_dict[user][time] = days
		else:
			res_dict[user] = {time:days}
	return res_dict



def read_line_content(line:str)->tuple:
	'''From a string like person|H|L|M|M|G|V|S|D| returns
		 - person
		 - time (morning,afternoon)
		 - days of week as a list of booleans'''
	values = line.replace(' ','').replace('\t','').split('|')
	person = values[0]
	time = values[1]
	days = [int(x) if (x!='') else 0 for x in values[2:]]
	return person,time,days