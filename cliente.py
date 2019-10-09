import Pyro4
import json

uri = input('Digite a URI: ')
if uri:
    objectremote = Pyro4.Proxy(uri)
    username = input('Digite o seu username: ')
    if username:
        userInfo = objectremote.getUserInfo(username)
        if userInfo == None:
            print('Usuario nao encontrado')
        else:
            print(json.dumps(userInfo, indent=4, sort_keys=True))
    else:
        print('Nao eh permitido usuario vazio')
else:
    print('Como se conectar sem URI?')

