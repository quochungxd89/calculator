# CALCULATOR - MÁY TÍNH KHOA HỌC ĐA CHỨC NĂNG

**ĐỒ ÁN "KỸ THUẬT LẬP TRÌNH PYTHON - IE221.E32.CN2.CNTT"**

**GVHD**: Thầy THS Nghi Hoàng Khoa

**Thành viên nhóm 11:**

| MSSV     | Họ tên               | 
| -------- | -------------------- | 
| 24210128 | Chử Quốc Hưng        | 
| 23410160 | Huỳnh Nhật Khánh     | 
| 23210062 | Nguyễn Hoàng Sơn     | 
| 24210175 | Trần Minh Thanh      | 
| 23210174 | Nguyễn Công Tuấn     | 

---

##  GIỚI THIỆU DỰ ÁN

Máy tính khoa học đa chức năng được phát triển bằng Python với giao diện Tkinter, cung cấp các chức năng tính toán từ cơ bản đến nâng cao, bao gồm giải phương trình và chuyển đổi hệ số.

###  MỤC TIÊU DỰ ÁN
- Phát triển ứng dụng máy tính khoa học đầy đủ chức năng
- Áp dụng kiến thức Python và lập trình hướng đối tượng
- Tạo giao diện người dùng trực quan và thân thiện
- Xây dựng hệ thống tính toán chính xác và tin cậy

## TÍNH NĂNG CHÍNH

### Tính Toán Cơ Bản
- Phép tính số học cơ bản (+, -, ×, ÷)
- Xử lý số thập phân và số nguyên
- Lịch sử phép tính với 10 phép tính gần nhất

###  Hàm Khoa Học
- **Hàm lượng giác**: sin, cos, tan, cotan (tính theo độ)
- **Hàm logarit**: log 
- **Hàm căn**: √ (căn bậc 2), ³√ (căn bậc 3), ⁿ√ (căn bậc n)
- **Hàm lũy thừa**: x², x³, xⁿ, x⁻¹
- **Hàm khoa học**: x×10ⁿ 

###  Giải Phương Trình
- **Phương trình bậc 1**: ax + b = 0
- **Phương trình bậc 2**: ax² + bx + c = 0
- Hiển thị đầy đủ các trường hợp nghiệm
- Lưu lịch sử phương trình đã giải

###  Chuyển Đổi Hệ Số
- **Binary** (hệ nhị phân)
- **Decimal** (hệ thập phân) 
- **Hexadecimal** (hệ thập lục phân)
- **Octal** (hệ bát phân)

###  Giao Diện & UX
- Giao diện màu xanh chuyên nghiệp
- Hiển thị phép tính và kết quả rõ ràng
- Lịch sử tính toán tương tác
- Xử lý lỗi thông minh

##  CÁCH CHẠY ỨNG DỤNG
python3 main.py

##  CẤU TRÚC DỰ ÁN
calculator/
├── main.py              # File chạy chính
├── logic/               # Module xử lý logic tính toán
│   ├── __init__.py
│   ├── calculator.py    # Class chính Calculator
│   ├── equations.py     # Giải phương trình
│   └── utils.py         # Hàm tiện ích
├── ui/                  # Module giao diện người dùng
│   ├── __init__.py
│   ├── display.py       # Hiển thị màn hình
│   └── buttons.py       # Tạo nút bấm
├
└── README.md            # Tài liệu hướng dẫn

##  CÔNG NGHỆ SỬ DỤNG
- **Ngôn ngữ**: Python 3
- **GUI Framework**: Tkinter
- **Modules**: math, re, tkinter
