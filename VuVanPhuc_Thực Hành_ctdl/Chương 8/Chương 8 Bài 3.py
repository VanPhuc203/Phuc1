class Album:
    def __init__(self, ten_album):
        self.ten_album = ten_album
        self.bai_hat = []

    def them_bai_hat(self, ten_bai_hat, ten_nhac_si, ten_ca_si):
        self.bai_hat.append({
            'ten_bai_hat': ten_bai_hat,
            'ten_nhac_si': ten_nhac_si,
            'ten_ca_si': ten_ca_si
        })

class TuDien:
    def __init__(self):
        self.albums = {}

    def NhapAlbum(self, ten_album, danh_sach_bai_hat):
        album = Album(ten_album)
        for bai_hat_info in danh_sach_bai_hat:
            ten_bai_hat, ten_nhac_si, ten_ca_si = bai_hat_info
            album.them_bai_hat(ten_bai_hat, ten_nhac_si, ten_ca_si)
        self.albums[ten_album] = album

    def XemAlbum(self, ten_album):
        if ten_album in self.albums:
            album = self.albums[ten_album]
            print(f"Album: {album.ten_album}")
            print("Bài hát:")
            for bai_hat in album.bai_hat:
                print(f"- Tên bài hát: {bai_hat['ten_bai_hat']}")
                print(f"  + Nhạc sĩ: {bai_hat['ten_nhac_si']}")
                print(f"  + Ca sĩ: {bai_hat['ten_ca_si']}")
        else:
            print("Không tìm thấy album!")

# Ví dụ sử dụng:
tudien_album = TuDien()

# Nhập thông tin album
tudien_album.NhapAlbum("Yên", [
    ("Nàng thơ", "Hoàng Dũng", "Hoàng Dũng"),
    ("Em hát ai nghe", "Orange", "Orange"),
    ("Đen đá không đường", "LyLy", "AMEE")
])

# Hiển thị thông tin album
tudien_album.XemAlbum("Yên")
