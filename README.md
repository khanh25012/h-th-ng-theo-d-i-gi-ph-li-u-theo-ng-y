HỌ TÊN : HÀ VĂN KHÁNH

LỚP :    56KMT

MSSV :   K205480106041

MÔN HỌC: LẬP TRÌNH PYTHON

GVHD : TS.ĐỖ DUY CỐP

XÂY DỰNG HỆ THỐNG THEO DÕI GIÁ PHẾ LIỆU THEO TỪNG NGÀY🔄

YÊU CẦU : 

 1. api : Đây là file chính của web app , chứa code Python cho ứng dụng FastAPI.
   thực hiện việc gửi một yêu cầu HTTP đến một trang web (https://muaphelieuthinhphat.com/bang-gia-thu-mua-phe-lieu-hom-nay/)
   bằng cách sử dụng thư viện requests. Sau đó,  sử dụng thư viện BeautifulSoup để phân tích cú pháp HTML của trang web và trích xuất dữ liệu cần thiết.

-->Cuối cùng, trả về dữ liệu đã trích xuất dưới dạng từ điển JSON.
 
2.MSSQL :tạo db PhelieuDatabase ,table sat_vun để lưu id,tên sắt vụn và đơn giá.

3.node red: gọi API  và đẩy data thu được vào mssql.

4.web hiển thị ( HTML ) :về giá sắt vụn và các loại vật liệu phế liệu khác nhau ,lấy từ db.

( đã đóng gói project python (api) thành service với NSSM thành công,chick vào là ra project.)

                                                    Sơ đồ hoạt động
                  
 ![ab33be75-1059-4faa-b953-21ab55531d21](https://github.com/khanh25012/h-th-ng-theo-d-i-gi-ph-li-u-theo-ng-y/assets/129476200/f9101f3d-abc4-426c-9e37-5259847fec63)

