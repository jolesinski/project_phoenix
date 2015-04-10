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
        # Test correct return
        payload = {
            "method": "setJointAngle",
            "params": {
                "joint": 1,
                "angle": 3.3
            },
            "jsonrpc": "2.0",
            "id": 0,
        }
        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 0
        assert response["jsonrpc"] == "2.0"
        assert isinstance(response["result"], int)
        assert response["result"] == 0

        # Test incorrect param name
        payload = {
            "method": "setJointAngle",
            "params": {
                "jointaa": 1,
                "angle": 3.3
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

        # Test incorrect param type
        payload = {
            "method": "setJointAngle",
            "params": {
                "joint": 1,
                "angle": 3
            },
            "jsonrpc": "2.0",
            "id": 2,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 2
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_getJointAngle_correct_params(self):
        # Test correct return
        payload = {
            "method": "getJointAngle",
            "params": {
                "joint": 1,
            },
            "jsonrpc": "2.0",
            "id": 0,
        }
        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 0
        assert response["jsonrpc"] == "2.0"
        assert type(response["result"]) is float
        assert response["result"] == 0.0

        # Test incorrect param name
        payload = {
            "method": "getJointAngle",
            "params": {
                "jointaa": 1,
                "angle": 3.3
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

        # Test incorrect param type
        payload = {
            "method": "getJointAngle",
            "params": {
                "joint": "1",
            },
            "jsonrpc": "2.0",
            "id": 2,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 2
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_setJointSpeed_correct_params(self):
        # Test correct return
        payload = {
            "method": "setJointSpeed",
            "params": {
                "joint": 1,
                "speed": 50
            },
            "jsonrpc": "2.0",
            "id": 0,
        }
        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 0
        assert response["jsonrpc"] == "2.0"
        assert isinstance(response["result"], int)
        assert response["result"] == 0

        # Test incorrect param name
        payload = {
            "method": "setJointSpeed",
            "params": {
                "jointaa": 1,
                "angle": 50
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

        # Test incorrect param type
        payload = {
            "method": "setJointSpeed",
            "params": {
                "joint": 1,
                "speed": 50.2
            },
            "jsonrpc": "2.0",
            "id": 2,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 2
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_getJointSpeed_correct_params(self):
        # Test correct params
        payload = {
            "method": "getJointSpeed",
            "params": {
                "joint": 1,
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

        # Test incorrect params
        payload = {
            "method": "getJointSpeed",
            "params": {
                "joint": 1,
                "speed": "3.3"
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

        # Test incorrect params
        payload = {
            "method": "getJointSpeed",
            "params": {
                "joint": [1, 2, 3],
            },
            "jsonrpc": "2.0",
            "id": 2,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 2
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_setCartesianPosition_correct_params(self):
        # Test correct params
        payload = {
            "method": "setCartesianPosition",
            "params": {
                "x": 45.6,
                "y": 21.4,
                "z": 10.0,
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

        # Test incorrect params names
        payload = {
            "method": "setCartesianPosition",
            "params": {
                "a": 45.6,
                "b": 21.4,
                "c": 10.0,
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

        # Test incorrect params type
        payload = {
            "method": "setCartesianPosition",
            "params": {
                "x": 45,
                "y": 21,
                "z": 10.0,
            },
            "jsonrpc": "2.0",
            "id": 2,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 2
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_getCartesianPosition_correct_params(self):
        # Test correct params
        payload = {
            "method": "getCartesianPosition",
            "jsonrpc": "2.0",
            "id": 0,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 0
        assert response["jsonrpc"] == "2.0"
        assert type(response["result"]) is list
        assert type(response["result"][0]) is float
        assert response["result"] == [0.0, 0.0, 0.0]

        # Test incorrect params
        payload = {
            "method": "getCartesianPosition",
            "params": {
                "myParam": 2,
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

    def test_setGripper_correct_params(self):
        # Test correct params
        payload = {
            "method": "setGripper",
            "params": {
                "open": True
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

        # Test incorrect params name
        payload = {
            "method": "setGripper",
            "params": {
                "close": True
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

        # Test incorrect params type
        payload = {
            "method": "setGripper",
            "params": {
                "open": 1
            },
            "jsonrpc": "2.0",
            "id": 2,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 2
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_setWheelSpeed_correct_params(self):
        # Test correct params
        payload = {
            "method": "setWheelSpeed",
            "params": {
                "wheel": 0,
                "speed": 80,
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

        # Test incorrect paramas name
        payload = {
            "method": "setWheelSpeed",
            "params": {
                "circle": 0,
                "velocity": 80,
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

        # Test incorrect paramas type
        payload = {
            "method": "setWheelSpeed",
            "params": {
                "wheel": 0.0,
                "speed": 80,
            },
            "jsonrpc": "2.0",
            "id": 2,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 2
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602

    def test_getWheelSpeed_correct_params(self):
        # Test correct params
        payload = {
            "method": "getWheelSpeed",
            "params": {
                "wheel": 0,
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

        # Test incorrect params
        payload = {
            "method": "getWheelSpeed",
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

        # Test incorrect params type
        payload = {
            "method": "getWheelSpeed",
            "params": {
                "wheel": True,
            },
            "jsonrpc": "2.0",
            "id": 2,
        }

        response = requests.post(self.test_url,
                                 data=json.dumps(payload),
                                 headers=self.test_headers).json()

        assert response["id"] == 2
        assert response["jsonrpc"] == "2.0"
        assert response["error"]["message"] == "Invalid params"
        assert response["error"]["code"] == -32602
