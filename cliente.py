import Pyro4

uri = input('Digite a URI')
if uri:
    objectremote = Pyro4.Proxy(uri)
    username = input('Digite o seu username')
    if username:
        print(objectremote.GithubUser(username))
    else:
        print('Nao eh permitido usuario vazio')
else:
    print('Como se conectar sem URI?')

