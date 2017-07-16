import subprocess


def run(args, cwd=None, input=None):
    '''
    Takes a list with the first item being the command to run and the remaining
    items being the arguments. Returns the output of the command as a string or
    raises an exception if the command returns an error code.
    '''
    if input is not None and isinstance(input, str):
        input = input.encode('utf-8')
    result = subprocess.run(args, stdout=subprocess.PIPE, cwd=cwd, input=input, check=True)
    return result.stdout.decode('utf-8')
