toan, he_so_toan = float(input("Điểm Toán: ")), int(input("Hệ số Toán: "))
ly, he_so_ly   = float(input("Điểm Lý: ")),   int(input("Hệ số Lý: "))
hoa, he_so_hoa = float(input("Điểm Hóa: ")),  int(input("Hệ số Hóa: "))

dtb = (toan * he_so_toan + ly * he_so_ly + hoa * he_so_hoa) / (he_so_toan + he_so_ly + he_so_hoa)
print(f"Điểm trung bình: {dtb:.2f}")
