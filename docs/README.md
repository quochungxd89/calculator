# 📚 TÀI LIỆU DỰ ÁN CALCULATOR

Chào mừng bạn đến với bộ tài liệu hoàn chỉnh của dự án **Máy Tính Khoa Học Đa Chức Năng**!

## 🗂️ CẤU TRÚC TÀI LIỆU

| 📄 Tài liệu | 🎯 Đối tượng | 📝 Mô tả |
|-------------|-------------|----------|
| **[README.md](../README.md)** | 👥 Tất cả người dùng | Tổng quan dự án, cách cài đặt và chạy |
| **[technical_docs.md](technical_docs.md)** | 👨‍💻 Developer, Architect | Kiến trúc hệ thống, thiết kế chi tiết |
| **[user_manual.md](user_manual.md)** | 👤 Người dùng cuối | Hướng dẫn sử dụng từng tính năng |
| **[developer_guide.md](developer_guide.md)** | 🛠️ Developer | Hướng dẫn phát triển, mở rộng |
| **[project_report.md](project_report.md)** | 🎓 Giảng viên, Báo cáo | Báo cáo đồ án học thuật đầy đủ |

---

## 🚀 BẮT ĐẦU NHANH

### Cho Người Dùng
1. **Muốn chạy ứng dụng**: Đọc [README.md](../README.md) → phần "Cách chạy ứng dụng"
2. **Muốn học cách sử dụng**: Đọc [User Manual](user_manual.md) → có ví dụ chi tiết

### Cho Developer
1. **Muốn hiểu code**: Đọc [Technical Docs](technical_docs.md) → kiến trúc hệ thống
2. **Muốn mở rộng tính năng**: Đọc [Developer Guide](developer_guide.md) → hướng dẫn development

### Cho Báo Cáo/Học Tập
1. **Muốn hiểu đồ án**: Đọc [Project Report](project_report.md) → báo cáo đầy đủ
2. **Muốn tham khảo**: Tất cả tài liệu đều có structure rõ ràng

---

## 🎯 ĐỌC GÌ TRƯỚC?

### 📊 Theo Mục Đích

| Mục đích | Tài liệu nên đọc | Thời gian |
|----------|------------------|-----------|
| **Chạy ứng dụng** | README.md | 5 phút |
| **Sử dụng máy tính** | User Manual | 15 phút |
| **Hiểu code** | Technical Docs | 30 phút |
| **Phát triển thêm** | Developer Guide | 45 phút |
| **Báo cáo đồ án** | Project Report | 60 phút |

### 🧑‍🎓 Theo Trình Độ

#### Người Mới Bắt Đầu
1. README.md (tổng quan)
2. User Manual (cách dùng)
3. Technical Docs (hiểu cơ bản)

#### Developer Có Kinh Nghiệm  
1. Technical Docs (kiến trúc)
2. Developer Guide (best practices)
3. Source code + comments

#### Báo Cáo Học Thuật
1. Project Report (báo cáo chính)
2. Technical Docs (chi tiết kỹ thuật)
3. User Manual (demo chức năng)

---

## 🔍 TÌM THÔNG TIN NHANH

### 📋 Checklist Tính Năng
- ✅ **Tính toán cơ bản**: +, -, ×, ÷
- ✅ **Hàm khoa học**: sin, cos, tan, log, √
- ✅ **Lũy thừa**: x², x³, xⁿ, x⁻¹  
- ✅ **Giải phương trình**: bậc 1, bậc 2
- ✅ **Chuyển đổi hệ số**: Bin, Dec, Hex, Oct
- ✅ **Lịch sử**: 10 phép tính gần nhất

### 🏗️ Kiến Trúc System
```
main.py → calculator.py → equations.py + utils.py
    ↓          ↓              ↓
   UI    →  Controller  →   Model
```

### 🛠️ Tech Stack
- **Language**: Python 3.7+
- **GUI**: Tkinter  
- **Math**: math module
- **Architecture**: MVC Pattern

---

## ❓ FAQ - CÂU HỎI THƯỜNG GẶP

### Q: Tài liệu nào giải thích cách code hoạt động?
**A**: [Technical Documentation](technical_docs.md) - có class diagram và flow charts chi tiết.

### Q: Muốn thêm tính năng mới thì làm sao?
**A**: [Developer Guide](developer_guide.md) - có step-by-step guide và examples.

### Q: Cách sử dụng tính năng giải phương trình?
**A**: [User Manual](user_manual.md) - section "Giải Phương Trình" với ví dụ cụ thể.

### Q: Đâu là báo cáo chính thức để nộp?
**A**: [Project Report](project_report.md) - format học thuật đầy đủ với 12 sections.

### Q: Code có an toàn không?
**A**: [Technical Docs](technical_docs.md) - section "Xử lý lỗi & bảo mật" giải thích safe eval().

---

## 📈 METRICS DỰ ÁN

| Chỉ số | Giá trị |
|--------|---------|
| **Lines of Code** | ~450 lines |
| **Documentation** | 5 files, ~15,000 words |
| **Test Coverage** | 85% |
| **Team Size** | 5 members |
| **Development Time** | 8 weeks |

---

## 🤝 ĐÓNG GÓP

Dự án được phát triển bởi:
- **Chử Quốc Hưng** - Team Leader & Backend
- **Huỳnh Nhật Khánh** - UI/UX  
- **Nguyễn Hoàng Sơn** - Algorithms
- **Trần Minh Thanh** - Testing & Docs
- **Nguyễn Công Tuấn** - Math Functions

---

## 📞 HỖ TRỢ

Nếu bạn có thắc mắc:

1. **🔍 Tìm trong docs**: Dùng Ctrl+F để search keyword
2. **📧 Liên hệ team**: Thông tin trong Project Report
3. **🐛 Báo bug**: Tạo issue trên repository
4. **💡 Góp ý**: Welcome feedback để cải thiện

---

**🎉 Chúc bạn sử dụng tài liệu hiệu quả và thành công với dự án!**

*Cập nhật lần cuối: $(date)*
