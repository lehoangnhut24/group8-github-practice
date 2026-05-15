import json
import os
from sinh_vien import SinhVien

class QuanLySinhVien:
    def __init__(self, file_path="data_sinhvien.json"):
        self.file_path = file_path
        self.danh_sach = self.load_data()

    def load_data(self):
        """Đọc dữ liệu và chuyển đổi thành danh sách object"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    return [SinhVien.from_dict(item) for item in json.load(f)]
            except: return []
        return []

    def save_data(self):
        """Lưu danh sách vào file JSON"""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([sv.to_dict() for sv in self.danh_sach], f, ensure_ascii=False, indent=4)

    def xoa_sinh_vien(self, mssv):
        """Xóa theo MSSV và tự động lưu file"""
        ban_dau = len(self.danh_sach)
        self.danh_sach = [sv for sv in self.danh_sach if sv.mssv != mssv]
        if len(self.danh_sach) < ban_dau:
            self.save_data()
            return True
        return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    ql = QuanLySinhVien()
    
    while True:
        clear_screen()
        print("="*65)
        print(f"{'HỆ THỐNG QUẢN LÝ CỬA HÀNG (SINH VIÊN MODULE)':^65}")
        print("="*65)
        print(f" {'1. Xem danh sách':<20} | {'2. Thêm sinh viên':<20}")
        print(f" {'3. Tìm kiếm':<20} | {'4. Xóa sinh viên':<20}")
        print(f" {'0. Lưu & Thoát':<20}")
        print("-" * 65)
        
        chon = input(" >> Nhập lựa chọn: ").strip()
        
        if chon == "1":
            print(f"\n{'DANH SÁCH SINH VIÊN':^65}")
            print("-" * 65)
            print(f"{'MSSV':<10} | {'Họ Tên':<20} | {'Lớp':<10} | {'Điểm':<5} | {'Loại'}")
            print("-" * 65)
            if not ql.danh_sach:
                print(f"{'(Danh sách hiện đang trống)':^65}")
            else:
                for sv in ql.danh_sach:
                    # Tận dụng định dạng cột từ __str__ của sinh_vien.py
                    print(sv)
            input("\n[Enter] để quay lại...")

        elif chon == "2":
            print("\n[THÊM MỚI]")
            mssv = input(" - MSSV: ").strip()
            if any(sv.mssv == mssv for sv in ql.danh_sach):
                print(" !! Lỗi: MSSV này đã tồn tại.")
            else:
                ten = input(" - Họ tên: ").strip()
                lop = input(" - Lớp: ").strip()
                try:
                    diem = float(input(" - Điểm TB (0-10): "))
                    if 0 <= diem <= 10:
                        ql.danh_sach.append(SinhVien(mssv, ten, lop=lop, diem_tb=diem))
                        ql.save_data()
                        print(" >> Đã thêm thành công!")
                    else: print(" !! Điểm không hợp lệ.")
                except: print(" !! Lỗi định dạng điểm.")
            input("\n[Enter] để tiếp tục...")

        elif chon == "3":
            tk = input("\nNhập MSSV hoặc Tên cần tìm: ")
            kq = [sv for sv in ql.danh_sach if sv.matches(tk)]
            print(f" >> Tìm thấy {len(kq)} kết quả.")
            for sv in kq: print(sv)
            input("\n[Enter] để tiếp tục...")

        elif chon == "4":
            m = input("\nNhập MSSV cần xóa: ").strip()
            if ql.xoa_sinh_vien(m): print(" >> Đã xóa thành công.")
            else: print(" !! Không tìm thấy mã sinh viên này.")
            input("\n[Enter] để tiếp tục...")

        elif chon == "0":
            print(" Đang lưu dữ liệu... Tạm biệt!")
            break
        else:
            input(" Lựa chọn sai. Nhấn Enter để thử lại...")

if __name__ == "__main__":
    main()