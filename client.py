import socket


client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_destination = ('127.0.0.1', 9999)


client.settimeout(2.0) #client will not wait forever
for attempt in range(1,6):
    client.sendto("hello server whiplash".encode("utf-8"),server_destination)
    try:
        print(f"[Attempt {attempt}] SENDING...")
        client.sendto(b"Hello Distributed World",server_destination )
        data,server_source =client.recvfrom(1024)
        print(f"[SUCCESS] Received: {data.decode()}")
        break
    except (socket.timeout,ConnectionResetError):
        print(f"no response for attempt{attempt}")
        if attempt == 5:
            print("[FAILURE] Server is unreachable after 5 tries.")
        
    
