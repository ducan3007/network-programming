import numpy as np
''''
protocol.py: File này định nghĩa các hàm để đóng gói package

Common: Các gói tin dùng chung cho cả hai bên
Server: Gói tin mà server sẽ GỬI
Client: Gói tin mà Client sẽ GỬI
'''

# Common: Đổi bytes thành int
def _get_ints(data):
    return int.from_bytes(data, 'little')

# Common: đổi int thành bytes
def _int_to_bytes(num):
    return int.to_bytes(num, 4, 'little')

# Common: Đổi string thành bytes
def _get_str(data):
    return data.decode()


# Common: Lấy type của package
def _get_type(data):
    if (len(data) >= 4):
        type = int.from_bytes(data[:4], 'little')
        return type

# Common: desrialize ma trận 2 chiều,
# Output: kích thước mảng, ma trận 2 chiều
def deserialize_matrix(package):
    data_type = _get_str(package[0:5])
    shape = _get_ints(package[5:9])
    len_ = _get_ints(package[9:13])
    bytes = package[13:13+len_]

    return (shape, np.frombuffer(bytes, dtype=data_type).reshape((shape, shape)))
    

# Server: gửi khi hai bên HÒA - 888
def game_draw():
    return int.to_bytes(888, 4, 'little')

# Server: Tạo gói tin Board cast (Ko quang trọng lắm) - 100
def _server_boardcast(data):
    type = int.to_bytes(100, 4, 'little')
    _len = int.to_bytes(len(data), 4, 'little')
    return type + _len + data


# Server: tạo match và gửi cho người chơi - 201
def _server_match_making(data):
    return int.to_bytes(201, 4, 'little') + data

# Server bị lỗi - 500
def server_error():
    return int.to_bytes(500, 4, 'little')

# Server Accept connection - 200
def accept_connection(uuid):
    type = int.to_bytes(200, 4, 'little')
    message = f'Connection accepted, your UUID is {uuid}'.encode()
    _len = int.to_bytes(len(message), 4, 'little')
    return type + _len + message


# Server: gửi cho người thắng - 999
def you_won():
    return int.to_bytes(999, 4, 'little')

# Server: gửi cho người thua - 777 
def you_lost():
    return int.to_bytes(777, 4, 'little')

# Server: gửi ma trận khi kết thúc ván chơi - 222 
def send_result(matrix, history):
    return int.to_bytes(222, 4, 'little') + _int_to_bytes(len(matrix)) + matrix + _int_to_bytes(len(history)) + history

# Server: Gửi cho player có lượt đi tiếp theo - 202
def can_move():
    return int.to_bytes(202, 4, 'little')

#  Server: Chưa đến lượt - 401
def cant_move():
    return int.to_bytes(401, 4, 'little')

# Server: nước đi ko hợp lệ - 402
def invalid_move():
    return int.to_bytes(402, 4, 'little')


# Server gửi update nước đi cho 2 người - 205 
def update_board(number):
    return int.to_bytes(205, 4, 'little') + _int_to_bytes(number)


# Clients: chọn số - 203 
def _select_number(number):
    return int.to_bytes(203, 4, 'little') + _int_to_bytes(number)

# Client: kiểm tra xem đến lượt mình chưa - 204 
def get_next_move():
    return int.to_bytes(204, 4, 'little')






