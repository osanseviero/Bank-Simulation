import json
from pprint import pprint
import Server

newServer = Server.Server

def load_json_multiple(segments):
    chunk = ""
    for segment in segments:
        chunk += segment
        try:
            yield json.loads(chunk)
            chunk = ""
        except ValueError:
            pass

def generateServerList(jsonFile):
	servers = []
	with open(jsonFile) as f:
		for parsed_json in load_json_multiple(f):
			servers.append(newServer(parsed_json))

	return servers


