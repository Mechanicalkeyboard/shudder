import requests
import os
import time
try:
    print("Getting AMI ID")
    ami_id_route='http://169.254.169.254/latest/meta-data/ami-id'
    ami_id = requests.get(ami_id_route)
    ami_id='i-0dd87e2cff5cf660c'
    service=os.environ['service']
    print(service)
    region=os.environ['region']
    print(region)
    environment=os.environ['environment']
    print(environment)
    if environment == 'prod': 
        domain = "cxengage.net"
    else:
        domain = "cxengagelabs.net"
    eureka_url='http://' + region + '-' + environment + '-eureka.'+ domain +':8080/eureka/v2/apps/' + service + '/' + ami_id + '/status?value=DOWN'
    print(eureka_url)
    eureka=requests.put(eureka_url)
    print(eureka)
    time.sleep(30)
    print("trying localhost")
    url = 'http://localhost:8080/shutdown'
    response = requests.post(url)
    print(response.status_code)
    statusCode = 200
    while statusCode == 200 or statusCode == 503:
        dockerPs = 'http://localhost:8080/status'
        status = requests.get(dockerPs)
        statusCode = status.status_code
        print(statusCode)   
        time.sleep(5)
    print(status.status_code)
except: 
    print("all done")