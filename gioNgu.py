from datetime import datetime, timedelta
print("Tôi la nguyen quoc viet.")
def tinh_gio_di_ngu(thoi_gian_thuc_day, so_gio_ngu=8):
    # Chuyển đổi chuỗi giờ thành đối tượng datetime
    try:
        gio_thuc_day = datetime.strptime(thoi_gian_thuc_day, "%H:%M")
        gio_di_ngu = gio_thuc_day - timedelta(hours=so_gio_ngu)
        return gio_di_ngu.strftime("%H:%M")
    except ValueError:
        return "Định dạng giờ không hợp lệ! Vui lòng nhập theo HH:MM"

# Nhập giờ cần thức dậy
thoi_gian_thuc_day = input("Nhập thời gian thức dậy (HH:MM): ")
so_gio_ngu = int(input("Nhập số giờ ngủ mong muốn: "))

gio_di_ngu = tinh_gio_di_ngu(thoi_gian_thuc_day, so_gio_ngu)
print(f"Bạn nên đi ngủ lúc: {gio_di_ngu}")

print(f"Bạn nên đi ngủ lúc: 7:00")