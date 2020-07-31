def what_to_do(instructions):
    simon = 'Simon says'
    if instructions.startswith(simon) or instructions.endswith(simon):
        return 'I ' + instructions.replace(simon, '').lstrip().rstrip()
    return "I won't do it!"

