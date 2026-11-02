from datetime import date

nam_sinh = int(input("Nhập năm sinh: "))
print(f"Tuổi hiện tại: {date.today().year - nam_sinh}")
