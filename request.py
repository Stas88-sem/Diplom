import configuration
import requests

def create_order(body):
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER,
                         json=body)

def order_info(track):
    return requests.get(configuration.BASE_URL + configuration.ORDER_INFO + str(track))
