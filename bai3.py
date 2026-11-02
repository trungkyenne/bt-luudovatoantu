ten = input("Tên sản phẩm: ")
so_luong = int(input("Số lượng: "))
don_gia = float(input("Đơn giá: "))

tien_hang = so_luong * don_gia
vat = tien_hang * 0.1
tong_tien = tien_hang + vat

print(f"Sản phẩm: {ten}")
print(f"Tiền hàng: {tien_hang:,.0f} đ")
print(f"Thuế VAT (10%): {vat:,.0f} đ")
print(f"Tổng tiền: {tong_tien:,.0f} đ")
