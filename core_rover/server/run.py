from core.dispatcher import application
from werkzeug.serving import run_simple

if __name__ == '__main__':
    run_simple('localhost', 8383, application)
