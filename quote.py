import socket
import threading
import random

quotes = ["It is better to die than do nothing. - Mudeok/Naksu",
          "Fighting is like a game of tug-of-war. Your opponent will pull if you feign letting your guard down. That is when you should strike. - Mudeok/Naksu",
          "All the pain that does not kill you will only make you stronger. - Mudeok/Naksu",
          "A truly skilled individual attacks when their enemy least expects it. - Mudeok/Naksu"]
          
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 8888))
    s.listen(5)
    print("Quote of the day on port 8888")

    while True:
        (connection_socket, client_addr) = s.accept()
        print(f"Incoming connection from {client_addr}")
        client_t = threading.Thread(target=client_quote, args=(connection_socket,))
        client_t.start()

def client_quote(connection_socket):
    client_quote = random.choice(quotes)
    connection_socket.send(client_quote.encode())
    connection_socket.close()

if __name__ == "__main__":
    main()
