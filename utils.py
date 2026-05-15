
def kiem_tra_mssv_trung(ds_sinh_vien, mssv):
    for sv in ds_sinh_vien:
        if sv.mssv == mssv:
            return True
    return False
def chuan_hoa_ten(ten):
    return ' '.join(word.capitalize() for word in ten.strip().split())
 def sap_xep_theo_ten(ds):
    return sorted(ds, key=lambda x: x.ten)