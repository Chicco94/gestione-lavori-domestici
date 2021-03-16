from src.leggi_utenti_turni import leggi_utenti_turni
from src.leggi_lavori_settimanali import leggi_lavori_settimanali
from src.help_functions import get_totale_ore,get_schedule,pretty_print,get_totale_ore_lavorate

UTENTI_TURNI = {}
LAVORI_SETTIMANALI = {}


def main() -> bool:
	'''Processo principale'''
	global UTENTI_TURNI
	global LAVORI_SETTIMANALI
	ore_disponibili = get_totale_ore(UTENTI_TURNI)
	ore_necessarie = get_totale_ore(LAVORI_SETTIMANALI)
	print("Questa settimana sono necessari {} slot\n a disposizione ci sono {} slot".format(ore_necessarie,ore_disponibili))

	ore_disponibili_iniziali = {}
	for user in UTENTI_TURNI:
		ore_disponibili_iniziali[user] = get_totale_ore(UTENTI_TURNI,user)
	
	schedule = get_schedule(UTENTI_TURNI,LAVORI_SETTIMANALI)
	pretty_print(schedule)
	for user in UTENTI_TURNI:
		print('{} ha lavorato per {}/{} questa settimana'.format(
			user,
			get_totale_ore_lavorate(schedule,user),
			ore_disponibili_iniziali[user]
			)
		)


def init() -> bool:
	'''Inizializzazione delle variabili d'ambiente e lettura dai file di configurazione'''
	global UTENTI_TURNI
	global LAVORI_SETTIMANALI
	UTENTI_TURNI = leggi_utenti_turni()
	LAVORI_SETTIMANALI = leggi_lavori_settimanali()
	return True

if __name__ == "__main__":
	init()
	main()