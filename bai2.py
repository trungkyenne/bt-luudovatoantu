a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

print(f"Tổng: {a + b}")
print(f"Hiệu: {a - b}")
print(f"Tích: {a * b}")
print(f"Thương: {a / b}" if b != 0 else "Thương: Không thể chia cho 0")
