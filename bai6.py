so_xe = input("Nhập số xe (4 chữ số): ")
tong = sum(int(c) for c in so_xe)
print(f"Số nút xe: {tong % 10}")
