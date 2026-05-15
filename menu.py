import json
import os
from sinh_vien import SinhVien

class QuanLySinhVien:
    def __init__(self, file_path="data_sinhvien.json"):
        self.file_path = file_path
        self.danh_sach = self.load_data()

    # ================== XỬ LÝ FILE ==================
    def load_data(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [SinhVien.from_dict(item) for item in data]
        except Exception as e:
            print(f"Lỗi đọc file: {e}")
            return []

    def save_data(self):
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([sv.to_dict() for sv in self.danh_sach], f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Lỗi lưu file: {e}")

    # ================== CHỨC NĂNG ==================
    def them_sinh_vien(self):
        print("\n--- THÊM SINH VIÊN MỚI ---")
        mssv = input("Nhập MSSV: ")
        # Kiểm tra trùng MSSV
        if any(sv.mssv == mssv for sv in self.danh_sach):
            print("Lỗi: MSSV đã tồn tại!")
            return

        ten = input("Nhập tên: ")
        try:
            tuoi = int(input("Nhập tuổi: "))
            lop = input("Nhập lớp: ")
            diem = float(input("Nhập điểm TB: "))
            
            new_sv = SinhVien(mssv, ten, tuoi, lop, diem)
            self.danh_sach.append(new_sv)
            self.save_data()
            print("Thêm thành công!")
        except ValueError as e:
            print(f"Dữ liệu không hợp lệ: {e}")

    def hien_thi_danh_sach(self):
        print("\n--- DANH SÁCH SINH VIÊN ---")
        if not self.danh_sach:
            print("Danh sách trống.")
        for sv in self.danh_sach:
            print(sv)

    def tim_kiem_sinh_vien(self):
        tu_khoa = input("\nNhập MSSV hoặc Tên cần tìm: ")
        ket_qua = [sv for sv in self.danh_sach if sv.matches(tu_khoa)]
        
        print(f"\nTìm thấy {len(ket_qua)} kết quả:")
        for sv in ket_qua:
            print(sv)

    def xoa_sinh_vien(self):
        mssv = input("\nNhập MSSV cần xóa: ")
        for sv in self.danh_sach:
            if sv.mssv == mssv:
                self.danh_sach.remove(sv)
                self.save_data()
                print("Đã xóa thành công!")
                return
        print("Không tìm thấy sinh viên có MSSV này.")

# ================== GIAO DIỆN MENU ==================
def main():
    qlsv = QuanLySinhVien()
    
    while True:
        print("\n" + "="*30)
        print("   HỆ THỐNG QUẢN LÝ SINH VIÊN")
        print("="*30)
        print("1. Xem danh sách sinh viên")
        print("2. Thêm sinh viên mới")
        print("3. Tìm kiếm sinh viên")
        print("4. Xóa sinh viên")
        print("0. Thoát")
        print("="*30)
        
        lua_chon = input("Chọn chức năng (0-4): ")
        
        if lua_chon == "1":
            qlsv.hien_thi_danh_sach()
        elif lua_chon == "2":
            qlsv.them_sinh_vien()
        elif lua_chon == "3":
            qlsv.tim_kiem_sinh_vien()
        elif lua_chon == "4":
            qlsv.xoa_sinh_vien()
        elif lua_chon == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()