from jsonrpc import JSONRPCResponseManager
from jsonrpc.dispatcher import Dispatcher
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response

from server.bus.controllers import StepperMotor

class MethodDispatcher(Dispatcher):
    def __init__(
            self, address='localhost', port=8383,
            bus_dispatcher=None, prototype=None):
        super(MethodDispatcher, self).__init__(prototype=prototype)
        self.address = address
        self.port = port
        self.bus_dispatcher = bus_dispatcher
        self.motor = StepperMotor(bus=bus_dispatcher)

    @Request.application
    def application(self, request):
        response = JSONRPCResponseManager.handle(request.data, self)
        return Response(response.json, mimetype='application/json')

    def run_application(self):
        run_simple(self.address, self.port, self.application)
