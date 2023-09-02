import socket
from pathlib import Path
from utils import extract_route, read_file, build_response
from views import index
from error import er

CUR_DIR = Path(__file__).parent
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    print('*'*100)
    print(request)

    route = extract_route(request)
    print(route)
    filepath = CUR_DIR / route
    if filepath.is_file():
        print('1'*100)
        response = build_response() + read_file(filepath)
    elif route == '':
        print('2'*100)
        response = index(request)
    elif 'delete' in route and 'img' not in route:
        print('3'*100)
        response = index(request)
    elif 'editar' in route and 'img' not in route:
        print('4'*100)
        response = index(request)
    elif 'update' in route and 'img' not in route :
        print('5'*100)
        response = index(request)
    elif "reenvio" in route and 'img' not in route:
        print('6'*100)
        response = index(request)

    else:
        print("7"*100)
        response = er()

    client_connection.sendall(response)

    client_connection.close()

server_socket.close()