def interpret(command):
    command = command.replace('()', 'o')
    command = command.replace('(al)', 'al')
    return command



print(interpret('G()()()()(al)'))