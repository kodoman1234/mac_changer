import re
import subprocess
import optparse

def get_user_input():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
    parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address!")

    return parse_object.parse_args()
def change_mac_address(user_interface,user_mac):
    subprocess.call(["ifconfig", user_interface ,"down"])
    subprocess.call(["ifconfig", user_interface ,"hw","ether",user_mac])
    subprocess.call(["ifconfig", user_interface ,"up"])

def check_new_mac(interface):

    ifconfig = subprocess.check_output(["ifconfig",interface]).decode('utf-8')
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("My MacChanger Started...")
(user_inputs,arguments) = get_user_input()
change_mac_address(user_inputs.interface,user_inputs.mac_address)
finalized_mac = check_new_mac(user_inputs.interface)

if finalized_mac == user_inputs.mac_address:
    print("Successs!!!")
else:
    print("U couldn't change the mac address")