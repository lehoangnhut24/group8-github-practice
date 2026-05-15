# manager.py

# Khởi tạo danh sách sinh viên rỗng để lưu trữ
danh_sach_sv = []

def them_sinh_vien(mssv, ten):
    """Hàm thêm sinh viên mới vào danh sách"""
    sinh_vien = {"mssv": mssv, "ten": ten}
    danh_sach_sv.append(sinh_vien)
    print(f"Đã thêm sinh viên: {ten} (MSSV: {mssv})")

def hien_thi_sinh_vien():
    """Hàm hiển thị toàn bộ danh sách sinh viên"""
    if len(danh_sach_sv) == 0:
        print("Danh sách hiện đang trống!")
        return
    
    print("\n--- DANH SÁCH SINH VIÊN ---")
    for sv in danh_sach_sv:
        print(f"MSSV: {sv['mssv']} | Tên: {sv['ten']}")
    print("---------------------------\n")

def tim_kiem_sinh_vien(tu_khoa):
    """Hàm tìm kiếm sinh viên theo tên hoặc MSSV"""
    print(f"\nKẾT QUẢ TÌM KIẾM CHO '{tu_khoa}' ")
    tim_thay = False
    
    for sv in danh_sach_sv:
        # Chuyển về chữ thường để tìm kiếm không phân biệt hoa thường
        if tu_khoa.lower() in sv['mssv'].lower() or tu_khoa.lower() in sv['ten'].lower():
            print(f"MSSV: {sv['mssv']} | Tên: {sv['ten']}")
            tim_thay = True
            
    if not tim_thay:
        print("Không tìm thấy sinh viên nào phù hợp!")

