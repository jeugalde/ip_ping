# ip_ping

The purpose of the script is to get a list of pinged machines with the command 'ping' + ip_address and the result will be a txt file as output with all pinged machines and a message in the program as 'ip_success' if ping

How does it work: from the input file called ip_source.txt upload and save all IP machines to check ping response and get an output 'ip_success' in the program and the output result is saved in a txt file with all pinged machines. if no ping print('no ping')


import os
import time

with open('ip_source.txt') as file:
    ip_ping = file.read().splitlines()
    print(ip_ping)

    for ip in ip_ping:
        response = os.system('ping -c 2 {}'.format(ip)) # ping -c 2 for Mac / ping -n 2 for PC
        if response == 0:
            print('{}     --> ip_success!'.format(ip))
            with open('output_success.txt','a') as f:
                print(ip, file=f, sep="\r\n")
        else:
            print('{}     --> no ping'.format(ip))
            time.sleep(2)
