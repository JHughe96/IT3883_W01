# Program Name: Assignment4B.py
# Course: IT3883/Section W01
# Student Name: Jason Hughes
# Assignment Number: Assignment4B
# Due Date: 11/06/2026
# Purpose: Program to receive and convert message from Assignment4A
# List specific resources used to complete the assignment: 

import socket

# Use the same IP address and port number as Program A.
HOST = "127.0.0.1"
PORT = 45000


def main():
    try:
        # Create a TCP server socket to wait for Program A to send input
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            server_socket.listen(1)
            print(f"Program B is listening on {HOST}:{PORT}-")

            # Wait for connection
            connection, address = server_socket.accept()
            with connection:
                print("Connected to:", address)

                # Read until Program A signals it is done
                message_parts = []
                while True:
                    data = connection.recv(4096)
                    if not data:
                        break
                    message_parts.append(data)

                # Decode the text, change it to uppercase, and display it
                message = b"".join(message_parts).decode("utf-8")
                print("Received from Program A:", message)
                uppercase_message = message.upper()

                # Send the uppercase text back to Program A
                connection.sendall(uppercase_message.encode("utf-8"))
                print("Sent back to Program A:", uppercase_message)

    except OSError as error:
        # Report problems such as an unavailable port.
        print("Network error:", error)


if __name__ == "__main__":
    main()
