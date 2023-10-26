import socket

def find_service_name() :
    protocolname = 'tcp'
    for port in [80, 25] :
        print ("port: %s => service name: %")