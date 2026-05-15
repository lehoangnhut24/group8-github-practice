# sinh_vien.py

class SinhVien:
    def __init__(self, mssv, ten, tuoi=None, lop=None, diem_tb=0.0):
        self.mssv = mssv
        self.ten = ten
        self.tuoi = tuoi
        self.lop = lop
        self.diem_tb = diem_tb

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

    # ================== NGHIỆP VỤ ==================
    def xep_loai(self):
        """Xếp loại học lực"""
        if self.diem_tb >= 8:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def matches(self, tu_khoa):
        """Tìm kiếm theo MSSV hoặc tên"""
        tu_khoa = tu_khoa.lower()
        return tu_khoa in self.mssv.lower() or tu_khoa in self.ten.lower()

    # ================== HIỂN THỊ ==================
    def __str__(self):
        return (
            f"MSSV: {self.mssv} | "
            f"Tên: {self.ten} | "
            f"Tuổi: {self.tuoi} | "
            f"Lớp: {self.lop} | "
            f"Điểm TB: {self.diem_tb:.2f} | "
            f"Xếp loại: {self.xep_loai()}"
        )

    # ================== CHUYỂN ĐỔI DỮ LIỆU ==================
    def to_dict(self):
        """Chuyển object -> dict (dùng để lưu file JSON)"""
        return {
            "mssv": self.mssv,
            "ten": self.ten,
            "tuoi": self.tuoi,
            "lop": self.lop,
            "diem_tb": self.diem_tb
        }

    @staticmethod
    def from_dict(data):
        """Tạo object từ dict"""
        return SinhVien(
            data.get("mssv"),
            data.get("ten"),
            data.get("tuoi"),
            data.get("lop"),
            data.get("diem_tb", 0.0)
        )
