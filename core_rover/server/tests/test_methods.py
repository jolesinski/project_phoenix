import requests
import json


class TestMethods:
    @classmethod
    def setup_class(self):
        self.test_url = "http://localhost:8383/jsonrpc"
        self.test_headers = {'content-type': 'application/json'}

    def test_setup(self):
        assert self.test_url
        assert self.test_url == "http://localhost:8383/jsonrpc"
        assert self.test_headers
        assert self.test_headers == {'content-type': 'application/json'}

    def test_setJointAngle_correct_params(self):
        payload = {
            "method": "setJointAngle",
            "params": {
                "joint": 1,
                "angle": "3.3"
            },
            "jsonrpc": "2.0",
            "id": 0,
        }
        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 0
        assert response["jsonrpc"] == "2.0"
        assert type(response["result"]) is int
        assert response["result"] == 0

        payload = {
            "method": "setJointAngle",
            "params": {
                "jointaa": 1,
                "angle": "3.3"
            },
            "jsonrpc": "2.0",
            "id": 1,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 1
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_getJointAngle_correct_params(self):
        payload = {
            "method": "getJointAngle",
            "params": {
                "joint": 1,
            },
            "jsonrpc": "2.0",
            "id": 2,
        }
        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 2
        assert response["jsonrpc"] == "2.0"
        assert type(response["result"]) is float
        assert response["result"] == 0.0

        payload = {
            "method": "getJointAngle",
            "params": {
                "jointaa": 1,
                "angle": "3.3"
            },
            "jsonrpc": "2.0",
            "id": 3,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 3
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_setJointSpeed_correct_params(self):
        payload = {
            "method": "setJointSpeed",
            "params": {
                "joint": 1,
                "speed": 50
            },
            "jsonrpc": "2.0",
            "id": 4,
        }
        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 4
        assert response["jsonrpc"] == "2.0"
        assert type(response["result"]) is int
        assert response["result"] == 0

        payload = {
            "method": "setJointSpeed",
            "params": {
                "jointaa": 1,
                "angle": 50
            },
            "jsonrpc": "2.0",
            "id": 5,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 5
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_getJointSpeed_correct_params(self):
        payload = {
            "method": "getJointSpeed",
            "params": {
                "joint": 1,
            },
            "jsonrpc": "2.0",
            "id": 6,
        }
        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 6
        assert response["jsonrpc"] == "2.0"
        assert type(response["result"]) is int
        assert response["result"] == 0

        payload = {
            "method": "getJointSpeed",
            "params": {
                "joint": 1,
                "speed": "3.3"
            },
            "jsonrpc": "2.0",
            "id": 7,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 7
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_setCartesianPosition_correct_params(self):
        payload = {
            "method": "setCartesianPosition",
            "params": {
                "x": "45.6",
                "y": "21.4",
                "z": "10.0"
            },
            "jsonrpc": "2.0",
            "id": 8,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 8
        assert response["jsonrpc"] == "2.0"
        assert type(response["result"]) is int
        assert response["result"] == 0

        payload = {
            "method": "setCartesianPosition",
            "params": {
                "a": "45.6",
                "b": "21.4",
                "c": "10.0"
            },
            "jsonrpc": "2.0",
            "id": 9,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 9
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_getCartesianPosition_correct_params(self):
        payload = {
            "method": "getCartesianPosition",
            "jsonrpc": "2.0",
            "id": 10,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 10
        assert response["jsonrpc"] == "2.0"
        assert type(response["result"]) is list
        assert type(response["result"][0]) is float
        assert response["result"] == [0.0, 0.0, 0.0]

        payload = {
            "method": "getCartesianPosition",
            "params": {
                "myParam": 2,
            },
            "jsonrpc": "2.0",
            "id": 11,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 11
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_setGripper_correct_params(self):
        payload = {
            "method": "setGripper",
            "params": {
                "open": True
            },
            "jsonrpc": "2.0",
            "id": 12,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 12
        assert response["jsonrpc"] == "2.0"
        assert type(response["result"]) is int
        assert response["result"] == 0

        payload = {
            "method": "setGripper",
            "params": {
                "close": True
            },
            "jsonrpc": "2.0",
            "id": 13,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 13
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_setWheelSpeed_correct_params(self):
        payload = {
            "method": "setWheelSpeed",
            "params": {
                "wheel": 0,
                "speed": 80,
            },
            "jsonrpc": "2.0",
            "id": 14,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 14
        assert response["jsonrpc"] == "2.0"
        assert type(response["result"]) is int
        assert response["result"] == 0

        payload = {
            "method": "setWheelSpeed",
            "params": {
                "circle": 0,
                "velocity": 80,
            },
            "jsonrpc": "2.0",
            "id": 15,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 15
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_getWheelSpeed_correct_params(self):
        payload = {
            "method": "getWheelSpeed",
            "params": {
                "wheel": 0,
            },
            "jsonrpc": "2.0",
            "id": 16,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 16
        assert response["jsonrpc"] == "2.0"
        assert type(response["result"]) is int
        assert response["result"] == 0

        payload = {
            "method": "getWheelSpeed",
            "jsonrpc": "2.0",
            "id": 17,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 17
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602
