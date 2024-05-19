$(document).ready(function() {
    // Ẩn bảng ban đầu
    $("#show_data").hide();

    $('#btn_click').click(function() {
        // Sử dụng phương thức $.get() để tải dữ liệu từ URL
        $.get('http://127.0.0.1:1234/data', function(data) {
            var element = $("#show_data");
            var table = "<table><tr><th>ID</th><th>Tên Phế liệu</th><th>Đơn Giá</th></tr>";
            var idCounter = 1; // Biến đếm id

            $.each(data, function(index, item) {
                table += "<tr id='row_" + idCounter + "'><td>" + idCounter + "</td><td>" + item.ten_sat + "</td><td>" + item.don_gia + "</td></tr>";
                idCounter++; // Tăng biến đếm id sau mỗi hàng được thêm vào bảng
            });
            table += "</table>";
            // Thay đổi nội dung của div bằng bảng đã tạo và hiển thị bảng
            element.html(table).show();
        });
    });
});
