def createFile(path, data):
  with open(path, 'w') as file:
    file.write(data)

def openFile(path):
  return open(path, 'r').read()

def getStatus():
  return openFile('./status.txt')

def setStatus(arg):
  createFile('./status.txt', arg)
