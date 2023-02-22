from asyncio import sleep
import http.client

if __name__ == "__main__":
    
    for i in range(0,100):
        connection = http.client.HTTPSConnection("69dqz7p6x6.execute-api.eu-west-1.amazonaws.com")
        connection.request("GET", "/Stage/bikes/123")
        response = connection.getresponse()
        print("Status: {} and reason: {}".format(response.status, response.reason))
        connection.close()
        sleep(1)
    