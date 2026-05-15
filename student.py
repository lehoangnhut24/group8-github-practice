# sinh_vien.py

class SinhVien:
    VALID_STATUS = ["Đang học", "Bảo lưu", "Đã tốt nghiệp"]

    def __init__(
        self,
        mssv,
        ten,
        tuoi=None,
        lop=None,
        diem_tb=0.0,
        trang_thai="Đang học",
        lop_sinh_hoat=None
    ):
        self.mssv = mssv
        self.ten = ten
        self.tuoi = tuoi
        self.lop = lop
        self.diem_tb = diem_tb
        self.lop_sinh_hoat = lop_sinh_hoat
        self.set_trang_thai(trang_thai)

    # ================== GETTER / SETTER ==================
    def set_ten(self, ten):
        if not ten.strip():
            raise ValueError("Tên không được rỗng!")
        self.ten = ten

    def set_tuoi(self, tuoi):
        if tuoi is not None and tuoi < 0:
            raise ValueError("Tuổi phải >= 0")
        self.tuoi = tuoi

    def set_diem_tb(self, diem):
        if diem < 0 or diem > 10:
            raise ValueError("Điểm phải từ 0 đến 10")
        self.diem_tb = diem

    def set_trang_thai(self, trang_thai):
        if trang_thai not in SinhVien.VALID_STATUS:
            raise ValueError(f"Trạng thái không hợp lệ! {SinhVien.VALID_STATUS}")
        self.trang_thai = trang_thai

    def set_lop_sinh_hoat(self, lop_sinh_hoat):
        if lop_sinh_hoat is not None and not lop_sinh_hoat.strip():
            raise ValueError("Lớp sinh hoạt không hợp lệ!")
        self.lop_sinh_hoat = lop_sinh_hoat

    # ================== NGHIỆP VỤ ==================
    def xep_loai(self):
        if self.diem_tb >= 8:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def matches(self, tu_khoa):
        tu_khoa = tu_khoa.lower()
        return (
            tu_khoa in self.mssv.lower()
            or tu_khoa in self.ten.lower()
            or (self.lop_sinh_hoat and tu_khoa in self.lop_sinh_hoat.lower())
        )

    # ================== HIỂN THỊ ==================
    def __str__(self):
        return (
            f"MSSV: {self.mssv} | "
            f"Tên: {self.ten} | "
            f"Tuổi: {self.tuoi} | "
            f"Lớp: {self.lop} | "
            f"Lớp SH: {self.lop_sinh_hoat} | "
            f"Điểm TB: {self.diem_tb:.2f} | "
            f"Xếp loại: {self.xep_loai()} | "
            f"Trạng thái: {self.trang_thai}"
        )

    # ================== CHUYỂN ĐỔI DỮ LIỆU ==================
    def to_dict(self):
        return {
            "mssv": self.mssv,
            "ten": self.ten,
            "tuoi": self.tuoi,
            "lop": self.lop,
            "diem_tb": self.diem_tb,
            "trang_thai": self.trang_thai,
            "lop_sinh_hoat": self.lop_sinh_hoat
        }

    @staticmethod
    def from_dict(data):
        return SinhVien(
            data.get("mssv"),
            data.get("ten"),
            data.get("tuoi"),
            data.get("lop"),
            data.get("diem_tb", 0.0),
            data.get("trang_thai", "Đang học"),
            data.get("lop_sinh_hoat")
        )