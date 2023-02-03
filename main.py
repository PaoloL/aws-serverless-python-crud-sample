import src.GetBikes.webservice as get
import json

if __name__ == "__main__":
    get_event_file = open('events/get_bikes.json')
    event = json.load(get_event_file)
    context = []
    get.lambda_handler(event, context)
