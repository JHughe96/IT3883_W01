# Program Name: Assignment4A.py
# Course: IT3883/Section W01
# Student Name: Jason Hughes
# Assignment Number: Assignment4A
# Due Date: 11/06/2026
# Purpose: Program to send and receive a message with Assignment4B
# List specific resources used to complete the assignment: 

import socket

# Both programs will be using the same network address and port
# 127.0.0.1 is the host
HOST = "127.0.0.1"
PORT = 45000


def main():
    # Get the text input for Program B
    message = input("Enter a message to send to Program B: ")

    try:
        # Create a TCP socket and close when finished
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.settimeout(10)

            # Connect to Program B, which is listening
            client_socket.connect((HOST, PORT))

            # Convert and send the message
            client_socket.sendall(message.encode("utf-8"))

            # Tell Program B we are finished although we can still receive
            client_socket.shutdown(socket.SHUT_WR)

            # Receive the response until Program B closes the connection
            response_parts = []
            while True:
                data = client_socket.recv(4096)
                if not data:
                    break
                response_parts.append(data)

            # Convert the received message into text and print result
            response = b"".join(response_parts).decode("utf-8")
            print("Response from Program B:", response)

    except (ConnectionError, OSError) as error:
        # Display a helpful message if Program B cannot be reached, may not be listening
        print("Network error:", error)
        print("Make sure Program B is running and using the same IP address and port.")


if __name__ == "__main__":
    main()
