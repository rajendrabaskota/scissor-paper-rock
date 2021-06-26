import socket
from _thread import *
from game import Game
import pickle

server = "192.168.1.91"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, server started")

connected = set()
games = {}
id_count = 0


def threaded_client(conn, p, game_id):
    global id_count
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if game_id in games:
                game = games[game_id]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset()
                    elif data != "get":
                        game.player(p, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))

            else:
                break
        except:
            break

    print("Lost Connection")
    try:
        del games[game_id]
        print("Closing game", game_id)
    except:
        pass
    id_count -= 1
    conn.close()


game_id_proxy = 0
game_id = 0

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    id_count += 1
    p = 0

    game_id_proxy = game_id
    game_id = (id_count - 1) // 2

    if id_count % 2 == 1:
        if game_id in games:
            game_id += 1

        games[game_id] = Game(game_id)
        start_new_thread(threaded_client, (conn, p, game_id))
    else:
        games[game_id_proxy].ready = True
        p = 1
        start_new_thread(threaded_client, (conn, p, game_id_proxy))
