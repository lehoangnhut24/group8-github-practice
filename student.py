def kiem_tra_mssv_trung(ds_sinh_vien, mssv):
    for sv in ds_sinh_vien:
        if sv.mssv == mssv:
            return True
    return False
