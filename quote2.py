import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(("localhost", 8888))

    quote = client_socket.recv(1024).decode()
    print("Quote of the day:", quote)

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()
