

def FileEncode(socket_, data):
    lens = len(data)

    lens_bytes = lens.to_bytes(4, byteorder = 'big')

    socket_.send(lens_bytes)
    socket_.send(data)


def FileDecode(socket_):
    data = bytes()

    len_bytes = socket_.recv(4)

    lens = int.from_bytes(len_bytes, byteorder = 'big')

    data = data + socket_.recv(lens)

    return data


