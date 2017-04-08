# send_requests.py
# Send request to GAE apps

import random
import requests
import json
import time
import logging


def parse_url():
	with open('listado_apps.txt', 'r') as f:
		urls = f.read().split('\n')

	return [u + '/api/' for u in urls]


METODOS = ['get', 'post', 'put', 'delete']
RECURSOS = [str(int(round(random.random() * 100000))) for _ in xrange(1000)]
TIEMPO_DORMIR = 1


def main():
	while True:
		urls = parse_url()

		metodo = random.choice(METODOS)

		recurso = random.choice(RECURSOS)

		for u in urls:
			if metodo == 'get':
				r = requests.get(u + recurso)
			elif metodo == 'post':
				r = requests.post(u + recurso, data=json.dumps({'data': str(int(round(random.random() * 100)))}))
			elif metodo == 'put':
				r = requests.put(u + recurso, data=json.dumps({'data': str(int(round(random.random() * 100)))}))
			elif metodo == 'delete':
				r = requests.delete(u + recurso)

			try:
				res_json = r.json()
			except ValueError:
				res_json = False

			res = 'URL: {}\tRecurso: {}\tStatus: {}\tMetodo: {}\tRespuesta: {}'.format(r.url,
			                                                                           recurso,
			                                                                           r.status_code,
			                                                                           metodo,
			                                                                           r.text.encode('utf-8')[:60])

			if res_json:
				res += '\tJSON: {}'.format(res_json)

			print res

		time.sleep(TIEMPO_DORMIR)


if __name__ == '__main__':
	main()
