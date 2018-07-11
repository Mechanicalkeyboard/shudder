import requests
import time

try:
    print("trying localhost")
    url = 'http://127.0.0.1:8080/shutdown'
    response = requests.post(url)
    print(response.status_code)
    statusCode = 200
    while statusCode == 200 or statusCode == 503:
        dockerPs = 'http://127.0.0.1:8080/status'
        status = requests.get(dockerPs)
        statusCode = status.status_code
        print(statusCode)
        time.sleep(5)
    print(status.status_code)
except: 
    print("all done")