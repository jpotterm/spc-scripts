class CommandError(Exception):
    '''
    Remote command returned an exit code other than 0
    '''
    pass


def run(connection, command):
    '''
    Takes an ssh `connnection` and a string of a `command` to run and executes it
    on the remote machine. Returns the output of the command as a string if the
    command succeeds and raises an exception if it fails.
    '''
    stdin, stdout, stderr = connection.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()

    if exit_status == 0:
        return stdout.read().decode('utf-8')
    else:
        message = stderr.read().decode('utf-8')
        raise CommandError('Command "{}" exited with code "{}" and message "{}"'.format(command, exit_status, message))
