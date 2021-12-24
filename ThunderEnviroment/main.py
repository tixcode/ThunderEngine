from thunderenviroment import *

env = Enviroment("db.tenv")
env.data['key'] = 26
env.data['releaser'] = True
env.save()
print(env.data['releaser'])