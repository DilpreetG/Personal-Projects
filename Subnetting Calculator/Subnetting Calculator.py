import ipaddress

def main():
    print("Hello! What would you like to achieve today?\n")
    todo_req()


def error_message(error_type):
    print('')
    print('____________________')
    print('')
    print(f"ERROR: Invalid {error_type}. Please try again.\n")
    return False


def todo_req():
    #TODO - Squash bugs (e.g. putting in 'g' for the ip address.)
    while True:
        inp = input("*** Q to quit ***\n"
                "1 - IP and CIDR/Subnet conversion\n"
                "2 - CIDR to Subnet or Subnet to CIDR (N/A)\n"
                "3 - TBD\n\n")
    
        if inp == '1':
            ip_address = input("Enter IP Address: ")
            if is_valid_IP(ip_address) is False:
                main()
            inptCIDR = input("Enter CIDR (e.g. /24, /30, etc.): ")
            if is_valid_CIDR(inptCIDR) is False:
                main()
            IP_subnet_CIDR(ip_address, inptCIDR)      
            
        elif inp == '2':
            #TODO
            error_message('Selection')
            pass
            #inpt = input("Please enter in the CIDR: ")
            #is_valid_cidr(inpt)
                
            
        elif inp == '3':
            #TODO
            pass
        elif inp == 'Q' or inp =='q':
            #TODO
            return False
        else:
            print("---------------------\nI'm sorry, that's not a valid input.\n")
 

def IP_subnet_CIDR(ip_address, subnet_mask):
    network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
    network_address = network.network_address
    broadcast_address = network.broadcast_address
    usable_ips = list(network.hosts())
        
    print(f"IP Address: {ip_address}")
    print(f"CIDR: {subnet_mask}")
    print(f"Network Address: {network_address}")
    print(f"Broadcast Address: {broadcast_address}")
    print(f"Usable IP Range: {usable_ips[0]} - {usable_ips[-1]}\n")


def is_valid_IP(ip):
    if len(ip) not in range(4,16):
        error_message('IP Address')
        return False
    
    for char in ip:
        if char.isdigit() or char == '.':
            continue
        else:
            error_message('IP Address')
            return False
        
    list_of_octets = ip.split('.')

    for i in list_of_octets:
        if int(i) in range(0, 256):
            continue
        else:
            error_message('IP Address')
            return False
    return True


def is_valid_CIDR(CIDR):
    if len(CIDR) == 2:
        if CIDR[0].isdigit() and CIDR[1].isdigit():
            return True
    else:
        error_message('CIDR')   


main()