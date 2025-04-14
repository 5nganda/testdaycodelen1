from datetime import datetime, timedelta

def tinh_gio_di_ngu(thoi_gian_thuc_day, so_gio_ngu=8):

    try:
        gio_thuc_day = datetime.strptime(thoi_gian_thuc_day, "%H:%M")
        # Tính toán giờ đi ngủ
        except ValueError:
        print("Định dạng giờ không hợp lệ! Vui lòng nhập theo HH:MM")
        # Nếu định dạng không hợp lệ, trả về thông báo lỗi
        return "Định dạng giờ không hợp lệ! Vui lòng nhập theo HH:MM"
        gio_di_ngu = gio_thuc_day - timedelta(hours=so_gio_ngu)
        return gio_di_ngu.strftime("%H:%M")
    except ValueError:
        print("Định dạng giờ không hợp lệ! Vui lòng nhập theo HH:MM")
        # Nếu định dạng không hợp lệ, trả về thông báo lỗi
        return "Định dạng giờ không hợp lệ! Vui lòng nhập theo HH:MM"

# Nhập giờ cần thức dậy
thoi_gian_thuc_day = input("Nhập thời gian thức dậy (HH:MM): ")
so_gio_ngu = int(input("Nhập số giờ ngủ mong muốn: "))  
print(f"Số giờ ngủ mong muốn: {so_gio_ngu}")

print(f"Bạn nên đi ngủ lúc: {gio_di_ngu}")
print("hallo")
print("hallo")      