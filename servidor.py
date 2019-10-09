import Pyro4
import json
import requests

@Pyro4.expose
class GithubUser:
    def getUserInfo(self, username):
        api_url_base = 'https://https://api.github.com/users/{}'.format(username)
        headers = {'Content-Type': 'application/json'}
        response = requests.get(api_url_base, headers = headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

daemon = Pyro4.Daemon()
uri = daemon.register(GithubUser)
print(uri)
daemon.requestLoop()
