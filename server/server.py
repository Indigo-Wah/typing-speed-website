
import socket 
import json
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('localhost', 8080))

print("Server is running on port 8080 ...")

server_socket.listen(5)

list_of_quotes : list = open("server/assests/quotes.txt").read().split("\n")

OK_RESPONSE = "HTTP/1.1 200 OK\r\nAccess-Control-Allow-Origin: *\r\n\r\n"
BAD_RESPONSE = "HTTP/1.1 400 BAD\r\nAccess-Control-Allow-Origin: *\r\n\r\n"

def analyze_text( POST_JSON ) -> str:
    # Parse input
    user_text = POST_JSON["text"].split(" ")
    user_test = POST_JSON["test"].split(" ")
    
    correct = 0

    # Compare based on ideal user_test
    for word in user_text:
        if word in user_test:
            correct += 1

    response = "accuracy: " + str(100 * (correct / len(user_text)))

    return response

while True:
    client_socket, client_address = server_socket.accept()

    data = client_socket.recv(1500)
    request = data.decode("utf-8")

    print(f"---------------------------------------\nGot Request\n---------------------------------------")

    # Parse
    # Split body
    request, body = request.split("\r\n\r\n")
    headers = request.split("\n")
    split_headers = headers[0].split(" ")
    method = split_headers[0]
    path = split_headers[1]
    version = split_headers[2]

    print("parsed:\n")
    print("Method: " + method)
    print("Path: " + path)
    print("Version: " + version)
    print("Headers: " + str(headers[1:]))
    print("")
    print("Body: \n" + body)

    if method == "GET":
        if path == "/quote":
            response_body = random.choice(list_of_quotes)
            response = OK_RESPONSE + response_body
            client_socket.sendall(response.encode())
            print("Sent response")
            client_socket.close()
    elif method == "POST":
        if path == "/text":
            if body == "":
                response = BAD_RESPONSE + "MISSING BODY"
                client_socket.sendall(response.encode())
                print("Sent 400 MISSING BODY")
                client_socket.close()
                continue
            
            # Parse JSON
            try:
                body = json.loads(body)
            except json.decoder.JSONDecodeError:
                response = BAD_RESPONSE + "MALFORMED BODY (JSON DECODE ERROR)"
                client_socket.sendall(response.encode())
                print("Sent 400 MALFORMED BODY (JSON DECODE ERROR)")
                client_socket.close()
                continue

            # Analyze text
            try:
                response = analyze_text(body)
            except Exception as e:
                print(e)
                response = BAD_RESPONSE + "MALFORMED BODY (JSON DECODE ERROR)\nExpecting:\n{'text':'user text', 'test':'compare text'}"
                client_socket.sendall(response.encode())
                print("Sent 400 MALFORMED BODY (JSON DECODE ERROR)")
                client_socket.close()
                continue
            response = OK_RESPONSE + response
            client_socket.sendall(response.encode())
            print("--------------------\nSent response \nOK 200")
            client_socket.close()

    else:
        response = "HTTP/1.1 405 BAD\r\nAccess-Control-Allow-Origin: *\r\n\r\n" + "METHOD NOT ALLOWED"
        client_socket.sendall(response.encode())
        print("Sent 405")
        client_socket.close()