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
