from src.help_variables import giorni_settimana,momenti_giorno,orario_to_start_index

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


def get_totale_ore_lavorate(work_week,user)-> int:
	''' ritorna le ore totali lavorate da un utente'''
	tot_ore = 0
	for giorno in work_week:
		for _,users in giorno.items():
			if type(users)==list and user in users:
				tot_ore +=1
	return tot_ore


def get_totale_ore(schedule,element='')-> int:
	''' ritorna le ore totali (necessarie o disponibili) di una schedule'''
	tot_ore = 0
	for user_or_job,turno in schedule.items():
		for _,settimana in turno.items():
			for giorno in settimana:
				if (element and user_or_job == element):
					tot_ore += int(giorno)
				elif (not element):
					tot_ore += int(giorno)
	return tot_ore


def rewrite_needed_jobs_as_weeklist(LAVORI_SETTIMANALI) -> list:
	''' Dato un dizionario {lavoro:{orario:[lista_di_necessità]}},
	orario può assumere i seguenti valori: mattina,pranzo,pomeriggio,sera
	ritorna una lista dove ogni elemento è un dizionario dei lavori necessari quel giorno
	[lavori_lunedì_mattina,lavori_martedì_mattina,...,lavori_domenica_sera]'''
	res_list = [{} for x in range(28)]
	for lavoro,turno in LAVORI_SETTIMANALI.items():
		for orario,giorni in turno.items():
			i = orario_to_start_index[orario]
			for giorno in giorni:
				if giorno>0:
					res_list[i][lavoro]=giorno
				i += 1
	return res_list


def get_time_from_index(index_of_day) -> str:
	if index_of_day < 7: return 'M'
	if 7 <= index_of_day < 14: return 'P'
	if 14 <= index_of_day < 21: return 'A'
	if 21 <= index_of_day: return 'S'


def get_available_user(UTENTI_TURNI,index_of_day) -> list:
	'''Ritorna la lista di utenti disponibili in quello specifico momento'''
	available_users = []
	time = get_time_from_index(index_of_day)
	day = index_of_day % 7
	for user,turn in UTENTI_TURNI.items():
		if turn[time][day]>0:
			available_users.append(user)
	return available_users


def get_less_loaded_user(available_users,work_week) -> str:
	'''ritorna il miglior utente che può lavorare in quel giorno'''
	min_loaded_user = None
	min_load = 99
	for user in available_users:
		user_load_so_far = get_totale_ore_lavorate(work_week,user)
		if user_load_so_far < min_load:
			min_load = user_load_so_far
			min_loaded_user = user
	return min_loaded_user
	

def update_TURNI_UTENTI(UTENTI_TURNI,user,index_of_day) -> dict:
	''' aggiorna il dizionario dei turni degli utenti'''
	time = get_time_from_index(index_of_day)
	day = index_of_day % 7
	UTENTI_TURNI[user][time][day] -= 1
	return UTENTI_TURNI


def assign(work_week,job,list_of_users,index_of_day) -> bool:
	work_week[index_of_day][job] = list_of_users
	return True


def get_schedule(UTENTI_TURNI,LAVORI_SETTIMANALI) -> dict:
	''' date le disponibilità degli utenti ed i lavori settimanali, ritorna una schedule che distribuisce i lavori tra gli utenti'''
	work_week = rewrite_needed_jobs_as_weeklist(LAVORI_SETTIMANALI)
	for index_of_day,day in enumerate(work_week):
		for job,needed_users in day.items():
			list_of_users = []
			for _ in range(needed_users):
				available_users = get_available_user(UTENTI_TURNI,index_of_day)
				user = get_less_loaded_user(available_users,work_week)
				if not user:
					time = get_time_from_index(index_of_day)
					day = index_of_day % 7
					print('Impossibile completare per {} {}'.format(
						giorni_settimana[day],
						momenti_giorno[time]
					))
					return work_week
				UTENTI_TURNI = update_TURNI_UTENTI(UTENTI_TURNI,user,index_of_day)
				list_of_users.append(user)
			assign(work_week,job,list_of_users,index_of_day)
	return work_week


def pretty_print(work_week):
	'''Stampa leggibile dei lavori della settimana'''
	res_str = ''
	for index_of_day,day in enumerate(work_week[0:7]):
		res_str += "\n\n"+giorni_settimana[index_of_day]+"\n\t\tMattina\n"
		for job,users in day.items():
			res_str += "\t{} svolto da {}\n".format(job,','.join(users))
		res_str +="\t\tPranzo\n"
		for job,users in work_week[index_of_day+7].items():
			res_str += "\t{} svolto da {}\n".format(job,','.join(users))
		res_str +="\t\tPomeriggio\n"
		for job,users in work_week[index_of_day+14].items():
			res_str += "\t{} svolto da {}\n".format(job,','.join(users))
		res_str +="\t\tSera\n"
		for job,users in work_week[index_of_day+21].items():
			res_str += "\t{} svolto da {}\n".format(job,','.join(users))
	return res_str