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


def get_totale_ore(schedule)-> int:
	''' ritorna le ore totali (necessarie o disponibili) di una schedule'''
	tot_ore = 0
	for _,turno in schedule.items():
		for _,settimana in turno.items():
			for giorno in settimana:
				tot_ore += int(giorno)
	return tot_ore


def rewrite_needed_jobs_as_weeklist(LAVORI_SETTIMANALI) -> list:
	''' Dato un dizionario {lavoro:{orario:[lista_di_necessità]}},
	ritorna una lista dove ogni elemento è un dizionario dei lavori necessari quel giorno
	[lavori_lunedì_mattina,lavori_martedì_mattina,...,lavori_domenica_pomeriggio]'''
	res_list = [{} for x in range(14)]
	for lavoro,turno in LAVORI_SETTIMANALI.items():
		for orario,giorni in turno.items():
			i = 0 if orario == 'M' else 7 
			for giorno in giorni:
				if giorno>0:
					res_list[i][lavoro]=giorno
				i += 1
	return res_list

def get_schedule(UTENTI_TURNI,LAVORI_SETTIMANALI) -> dict:
	''' date le disponibilità degli utenti ed i lavori settimanali, ritorna una schedule che distribuisce i lavori tra gli utenti'''
	print(LAVORI_SETTIMANALI)
	print(rewrite_needed_jobs_as_weeklist(LAVORI_SETTIMANALI))
	return {}