import requests
import json


def main():
    url = "http://localhost:12345/"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "setJointAngle",
        "params": {"joint": 1, "angle": 3.14},
        "jsonrpc": "2.0",
        "id": 1,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print response
    #assert response["result"] == "echome!"
    #assert response["jsonrpc"]
    #assert response["id"] == 0

if __name__ == "__main__":
    main()
