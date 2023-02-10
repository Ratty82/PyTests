import paho.mqtt.subscribe as receiver
import json

def on_message_print(client, userdata, message):
    msg = json.loads(message.payload)
    #slot_value = msg['slot_duration']
    #optimal_schedules_value = msg['n_optimal_schedules']
    print('Received message in JSON: ' ,msg)
    #print('Slot value :' , slot_value)
    #print('Optimal schedules value :',optimal_schedules_value)

receiver.callback(on_message_print, "test_EA", hostname="172.22.13.60")
