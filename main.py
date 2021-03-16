from src.leggi_utenti_turni import leggi_utenti_turni
from src.leggi_lavori_settimanali import leggi_lavori_settimanali
from src.help_functions import get_totale_ore,get_schedule,get_totale_ore_lavorate
from src.docx import create_schedule_document

UTENTI_TURNI = {}
LAVORI_SETTIMANALI = {}


def main() -> bool:
	'''Processo principale'''
	global UTENTI_TURNI
	global LAVORI_SETTIMANALI

	ore_disponibili_iniziali = {}
	for user in UTENTI_TURNI:
		ore_disponibili_iniziali[user] = get_totale_ore(UTENTI_TURNI,user)
	
	schedule = get_schedule(UTENTI_TURNI,LAVORI_SETTIMANALI)
	footer = '\n\n'
	for user in UTENTI_TURNI:
		footer += ('{} ha lavorato per {}/{} questa settimana\n'.format(
			user,
			get_totale_ore_lavorate(schedule,user),
			ore_disponibili_iniziali[user]
			)
		)

	create_schedule_document(schedule,footer)
	return True


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