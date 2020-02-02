import paho.mqtt.client as mqtt
import settings

def connect_to_message_broker():
	if settings.BROKER == 1:    

	    client = mqtt.Client()

	    client.username_pw_set("hjzjzxtj", "JZVpPmykkAsQ")

	    client.connect("soldier.cloudmqtt.com", 10982, 60)

	    return client
	return None    
