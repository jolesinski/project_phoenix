from server.common import get_dispatcher
from werkzeug.serving import run_simple

if __name__ == '__main__':
    dispatcher = get_dispatcher()
    dispatcher.run_application()
