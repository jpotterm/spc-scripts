import paramiko


def connect(user, host, port=22, password=None):
    '''
    Return an ssh connection to `user`@`host`.
    '''
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=user, password=password)
    return client
