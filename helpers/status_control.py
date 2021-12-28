def _write_status_file(path, data):
    with open(path, 'w') as file:
        file.truncate()
        file.write(data)

def _open_status_file(path):
    return open(path, 'r').read()

def get_invites_status():
    return _open_status_file('./.bot_status')

def set_invites_status(arg):
    _write_status_file('./.bot_status', arg)
