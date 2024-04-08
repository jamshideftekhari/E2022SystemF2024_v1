import Pyro4 

@Pyro4.expose
class GreatignMaker(object):
    def get_greeting(self, name):
        return f"Hello, {name}"

daemon = Pyro4.Daemon()
uri = daemon.register(GreatignMaker)
print("Ready. object uri: ", uri)
daemon.requestLoop()    

    



