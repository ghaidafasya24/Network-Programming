import socket

def convent_integer():
    data = 1234
    #32-bit
    print ("original: %s ==> Long Host Byte Order: %s, Network byte order: %s"
    %(data, socket.ntoh1(data), socket.hton1(data)))
    #16-bit
    print ("original: %s ==> Short Host Byte Order: %s, Network byte order: %s"
    %(data, socket.ntohs(data), socket.htons(data)))

if __name__ == '__main__' :
    convert_integer()