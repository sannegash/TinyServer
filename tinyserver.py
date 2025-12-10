"""
 Implements a simple HTTP/1.0 Server

"""
import socket
import os  

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)
print('Open http://localhost:%s in your browser' % SERVER_PORT)
while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    fin = open('htdocs/index.html')
    content = fin.read() 
    fin.close()
    request = client_connection.recv(1024).decode()
    print(request)

    #Parse HTTP headers 
    headers = request.split('\n')
    filename = headers[0].split()[1]

    #Get the content of the file 

    if filename == "/":
        filename = "/index.html"
    try: 
        fin = open('htdocs' + filename)
        content = fin.read()
        fin.close()

        response = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:
        fin = open('htdocs/404.html')
        errormessage = fin.read()
        fin.close()

        response = 'HTTP/1.0 200 OK\n\n' +  errormessage

    # Send HTTP response
    client_connection.sendall(response.encode())
    #Reload on file changes
    event_handler = AnyFileChanges()
    observer = Observer()
    observer.schedule(event_handler, path='htdocs/', recursive=True)
    observer.start()
    # Close client connection
    client_connection.close()

# Close socket
server_socket.close()
