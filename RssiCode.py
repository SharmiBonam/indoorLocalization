import requests
import string

url = "http://ec2-3-137-208-42.us-east-2.compute.amazonaws.com:64000/zone/best_zone"

zone1_rssi = requests.get("http://192.168.4.227").json()
zone1_rssi = int(zone1_rssi['rssi'])

#zone2_rssi = requests.get("http://IP Here").json()
#zone2_rssi = int(zone2_rssi['rssi'])

#zone3_rssi = requests.get("http://IP Here").json()
#zone3_rssi = int(zone3_rssi['rssi'])

def highest(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        largest_num = num1
    elif (num2 > num1) and (num2 > num3):
        largest_num = num2
    else:
        largest_num = num3
    print("The highest of the 3 RSSI values is : ", largest_num)
    
def lowest(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        smallest_num = num1
    elif (num2 < num1) and (num2 < num3):
        smallest_num = num2
    else:
        smallest_num = num3
    if (smallest_num == num1):
        zone = "Zone 1"
    elif (smallest_num == num2):
        zone = "Zone 2"
    elif (smallest_num == num3):
        zone = "Zone 3"
    #print("The lowest of the 3 RSSI values is : " \
    #      + str(smallest_num) + " at " + zone)
    payload = {'name': 'best_zone', 'zname': zone}
    response = requests.put(url=url, data=payload)
    
#highest(zone1_rssi, zone2_rssi, zone3_rssi)

lowest(zone1_rssi, zone2_rssi, zone3_rssi)
