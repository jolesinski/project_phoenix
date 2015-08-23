class BaseController(object):
    def __init__(self, bus):
        self.bus = bus

    def _send_frame(self, data):
        response = self.bus.send_frame(data=data)
        return {
            'response': response,
            'status': self.bus.status,
        }
