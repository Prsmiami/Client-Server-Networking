import socket


if __name__ == "__main__":
    print("Hello, starting up...")

    mc_addr = "224.0.0.70"
    mc_port = 50000
    soc = socket.socket(type=socket.SOCK_DGRAM)

    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    soc.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
    soc.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)

    soc.bind(("",mc_port))
    lhost = socket.gethostbyname("localhost");
    soc.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(lhost))

    soc.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(mc_addr) + socket.inet_aton(lhost))

    while 1:
        data, addr = soc.recvfrom(256)
        print("Got:", data.decode())


    soc.close()

