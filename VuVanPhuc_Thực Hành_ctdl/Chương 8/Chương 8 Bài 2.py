class TuDien:
    def __init__(self):
        # Khởi tạo từ điển rỗng
        self.tu_dong_nghia = {}
        self.tu_trai_nghia = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        # Hàm băm lấy ký tự đầu tiên của từ
        ky_tu_dau = tu[0]

        # Thêm từ và các từ đồng nghĩa vào từ điển
        if dong_nghia:
            if ky_tu_dau not in self.tu_dong_nghia:
                self.tu_dong_nghia[ky_tu_dau] = {tu: []}
            self.tu_dong_nghia[ky_tu_dau][tu].extend(dong_nghia)

        # Thêm từ và các từ trái nghĩa vào từ điển
        if trai_nghia:
            if ky_tu_dau not in self.tu_trai_nghia:
                self.tu_trai_nghia[ky_tu_dau] = {tu: []}
            self.tu_trai_nghia[ky_tu_dau][tu].extend(trai_nghia)

    def DongNghia(self, tu):
        ky_tu_dau = tu[0]

        # Kiểm tra xem từ đồng nghĩa có trong từ điển không
        if ky_tu_dau in self.tu_dong_nghia and tu in self.tu_dong_nghia[ky_tu_dau]:
            return self.tu_dong_nghia[ky_tu_dau][tu]
        else:
            return []

    def TraiNghia(self, tu):
        ky_tu_dau = tu[0]

        # Kiểm tra xem từ trái nghĩa có trong từ điển không
        if ky_tu_dau in self.tu_trai_nghia and tu in self.tu_trai_nghia[ky_tu_dau]:
            return self.tu_trai_nghia[ky_tu_dau][tu]
        else:
            return []

# Ví dụ sử dụng:
tudien = TuDien()
tudien.NhapTu("Bút xanh", dong_nghia=["Blue pen"], trai_nghia=["Ruler"])
tudien.NhapTu("Thước", dong_nghia=["Ruler"], trai_nghia=["Bút xanh"])

tu_dong_nghia = tudien.DongNghia("Bút xanh")
tu_trai_nghia = tudien.TraiNghia("Bút xanh")
print("Từ đồng nghĩa của 'Bút xanh':", tu_dong_nghia)
print("Từ trái nghĩa của 'Bút xanh':", tu_trai_nghia)
