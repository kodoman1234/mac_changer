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

print("My MacChanger Started...")
(user_inputs,arguments) = get_user_input()
change_mac_address(user_inputs.interface,user_inputs.mac_address)