import json
import os
from sinh_vien import SinhVien

class QuanLySinhVien:
    def __init__(self, file_path="data_sinhvien.json"):
        self.file_path = file_path
        self.danh_sach = self.load_data()

    def load_data(self):
        """Đọc dữ liệu từ file JSON, trả về danh sách đối tượng SinhVien"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return [SinhVien.from_dict(item) for item in data]
            except (json.JSONDecodeError, Exception):
                return []
        return []

    def save_data(self):
        """Lưu danh sách hiện tại xuống file JSON"""
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([sv.to_dict() for sv in self.danh_sach], f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Lỗi khi lưu dữ liệu: {e}")

    def xoa_sinh_vien(self, mssv):
        """Xóa sinh viên theo mã số và cập nhật lại file"""
        ban_dau = len(self.danh_sach)
        self.danh_sach = [sv for sv in self.danh_sach if sv.mssv != mssv]
        if len(self.danh_sach) < ban_dau:
            self.save_data()
            return True
        return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hien_thi_menu():
    print("\n" + "="*55)
    print(f"{'CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN':^55}")
    print("="*55)
    print(" 1. Hiển thị danh sách sinh viên")
    print(" 2. Thêm mới sinh viên")
    print(" 3. Tìm kiếm sinh viên (Tên/MSSV)")
    print(" 4. Xóa sinh viên khỏi hệ thống")
    print(" 0. Lưu dữ liệu và Thoát")
    print("-" * 55)

def main():
    ql = QuanLySinhVien()
    
    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn (0-4): ").strip()
        
        if lua_chon == "1":
            print(f"\n{'--- DANH SÁCH SINH VIÊN ---':^55}")
            if not ql.danh_sach:
                print(" Hiện tại chưa có dữ liệu sinh viên.")
            else:
                # Tiêu đề bảng
                print(f"{'MSSV':<10} | {'Họ và Tên':<20} | {'Lớp':<10} | {'GPA'}")
                print("-" * 55)
                for sv in ql.danh_sach:
                    print(sv)
            input("\nNhấn Enter để tiếp tục...")

        elif lua_chon == "2":
            print("\n[THÊM SINH VIÊN MỚI]")
            mssv = input(" - Nhập MSSV: ").strip()
            if any(sv.mssv == mssv for sv in ql.danh_sach):
                print(" >> Lỗi: MSSV này đã tồn tại trong hệ thống!")
            else:
                ten = input(" - Nhập Họ và Tên: ").strip()
                lop = input(" - Nhập Lớp: ").strip()
                try:
                    diem = float(input(" - Nhập Điểm trung bình (0-10): "))
                    if 0 <= diem <= 10:
                        ql.danh_sach.append(SinhVien(mssv, ten, lop=lop, diem_tb=diem))
                        ql.save_data()
                        print(" >> Đã thêm sinh viên thành công!")
                    else:
                        print(" >> Lỗi: Điểm không hợp lệ.")
                except ValueError:
                    print(" >> Lỗi: Điểm phải là một số thực.")
            input("\nNhấn Enter để tiếp tục...")

        elif lua_chon == "3":
            tu_khoa = input("\nNhập MSSV hoặc Tên cần tìm: ")
            ket_qua = [sv for sv in ql.danh_sach if sv.matches(tu_khoa)]
            print(f" >> Tìm thấy {len(ket_qua)} kết quả phù hợp.")
            for sv in ket_qua:
                print(sv)
            input("\nNhấn Enter để tiếp tục...")

        elif lua_chon == "4":
            mssv_xoa = input("\nNhập MSSV của sinh viên cần xóa: ").strip()
            if ql.xoa_sinh_vien(mssv_xoa):
                print(f" >> Đã xóa thành công sinh viên có mã {mssv_xoa}.")
            else:
                print(" >> Lỗi: Không tìm thấy sinh viên với MSSV đã nhập.")
            input("\nNhấn Enter để tiếp tục...")

        elif lua_chon == "0":
            print(" Đang đóng chương trình. Hẹn gặp lại!")
            break
        else:
            print(" Lựa chọn không hợp lệ, vui lòng nhập từ 0 đến 4.")
            input("\nNhấn Enter để thử lại...")
        clear_screen()

if __name__ == "__main__":
    main()