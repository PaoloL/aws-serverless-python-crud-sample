import src.GetBikes.webservice as get
import src.PutBikes.webservice as put
import src.PostBikes.webservice as post
import json

if __name__ == "__main__":
    print("Simulate GET Bikes")
    get_event_file = open('events/get_bikes.json')
    event = json.load(get_event_file)
    context = []
    get.lambda_handler(event, context)

    print("Simulate POST Bikes")
    post_event_file = open('events/post_bikes.json')
    event = json.load(post_event_file)
    context = []
    post.lambda_handler(event, context)

    print("Simulate PUT Bikes")
    post_event_file = open('events/put_bikes.json')
    event = json.load(post_event_file)
    context = []
    put.lambda_handler(event, context)
