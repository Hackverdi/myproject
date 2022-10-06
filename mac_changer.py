import subprocess
import optparse
import re
def opt():
    parser = optparse.OptionParser()
    parser.add_option("-i","--iface",dest="iface" ,help="the interface to which the mac address belongs")
    parser.add_option("-m","--mac",dest="mac_add",help="the mac address you want to change")
    user_input=parser.parse_args()[0]
    return user_input


def subp(interface,mac_address):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
    subprocess.call(["ifconfig",interface,"up"])
def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None
print('----------------------------------------------------------------------------------------------------------->')
print("Mac changer started....")
user_opt = opt()
ifcon=subp(user_opt.iface,user_opt.mac_add)
finalized_mac = control_new_mac(str(user_opt.iface))
if finalized_mac == user_opt.mac_add:
    print("mac changer fnished ")
    print("Success! ")
else:
    print("mac changer finished")
    print("Error! ")
