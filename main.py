from src.leggi_utenti_turni import leggi_utenti_turni
from src.leggi_lavori_settimanali import leggi_lavori_settimanali

def main():
	'''Processo principale'''
	return 0

def init():
	'''Inizializzazione delle variabili d'ambiente e lettura dai file di configurazione'''
	utenti_turni = leggi_utenti_turni()
	lavori_settimanali = leggi_lavori_settimanali()
	print(utenti_turni)
	print(lavori_settimanali)
	return None

if __name__ == "__main__":
	init()
	main()