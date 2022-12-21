from boxscores.celery import cel

@cel.task(name='hello_world', queue='boxscores')
def hello(name='world', name2='d'):
    return 'hello ' + name


print("executed tasks.py")