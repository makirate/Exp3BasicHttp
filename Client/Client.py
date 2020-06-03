import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
    s.connect(('54.65.248.63', 50007))
    # サーバにメッセージを送る
    s.sendall(b'hello')
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
    data = s.recv(1024)
    #
    print(repr(data))