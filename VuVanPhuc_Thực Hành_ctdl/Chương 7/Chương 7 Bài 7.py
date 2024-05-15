class DoThi:
    def __init__(self):
        self.dt = {}

    def themDinh(self, dinh, ds_dinh_ke=[]):
        self.dt[dinh] = ds_dinh_ke

    def SoCungRa(self, v):
        try:
            return len(self.dt[v])
        except KeyError:
            return 'Đỉnh không tồn tại trong đồ thị'

# Sử dụng
dt = DoThi()
dt.themDinh('A', ['B', 'C'])
dt.themDinh('B', ['A'])
dt.themDinh('C', [])
print(dt.SoCungRa('A'))  # Output: 2
