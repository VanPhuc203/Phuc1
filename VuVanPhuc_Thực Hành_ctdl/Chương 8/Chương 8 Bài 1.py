class TuDien:
    def __init__(self):
        # Khởi tạo từ điển rỗng
        self.tu_dong_nghia = {}
        self.tu_trai_nghia = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        # Hàm băm lấy ký tự đầu tiên của từ
        ky_tu_dau = tu[0]

        # Thêm từ và từ đồng nghĩa vào từ điển
        if ky_tu_dau not in self.tu_dong_nghia:
            self.tu_dong_nghia[ky_tu_dau] = {tu: []}
        if dong_nghia:
            self.tu_dong_nghia[ky_tu_dau][tu].append(dong_nghia)

        # Thêm từ và từ trái nghĩa vào từ điển
        if ky_tu_dau not in self.tu_trai_nghia:
            self.tu_trai_nghia[ky_tu_dau] = {tu: []}
        if trai_nghia:
            self.tu_trai_nghia[ky_tu_dau][tu].append(trai_nghia)

    def TraTu(self, tu):
        ky_tu_dau = tu[0]

        # Kiểm tra xem từ đồng nghĩa có trong từ điển không
        if ky_tu_dau in self.tu_dong_nghia and tu in self.tu_dong_nghia[ky_tu_dau]:
            tu_dong_nghia = self.tu_dong_nghia[ky_tu_dau][tu]
        else:
            tu_dong_nghia = None

        # Kiểm tra xem từ trái nghĩa có trong từ điển không
        if ky_tu_dau in self.tu_trai_nghia and tu in self.tu_trai_nghia[ky_tu_dau]:
            tu_trai_nghia = self.tu_trai_nghia[ky_tu_dau][tu]
        else:
            tu_trai_nghia = None

        return tu_dong_nghia, tu_trai_nghia

# Ví dụ sử dụng:
tudien = TuDien()
tudien.NhapTu("mèo", "cat", "dog")
tudien.NhapTu("mèo", "kitty", "fish")

tu_dong_nghia, tu_trai_nghia = tudien.TraTu("mèo")
print("Từ đồng nghĩa:", tu_dong_nghia)
print("Từ trái nghĩa:", tu_trai_nghia)
