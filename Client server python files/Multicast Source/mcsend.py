import socket

def doMCSend(esoc):
    mc_addr = ""
    mc_port = 50000
    esoc.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
    lhost = socket.gethostbyname("localhost")
    esoc.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(lhost))


    done = False
    while not done:
        try:
            umess = input("Me>")

            esoc.sendto(umess.encode(),(mc_addr, mc_port))

            if umess == "bye":
                done = True
        except Exception as e:
            print("Error...")
            print(e)
            done = True;
    print("Ending...")



if __name__ == "__main__":
    print("Hello, starting up...")

    soc = socket.socket(type=socket.SOCK_DGRAM)

    doMCSend(soc)

    soc.close()
