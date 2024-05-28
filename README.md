HỌ TÊN : HÀ VĂN KHÁNH

LỚP :    56KMT

MSSV :   K205480106041

MÔN HỌC: LẬP TRÌNH PYTHON

GVHD : TS.ĐỖ DUY CỐP

XÂY DỰNG HỆ THỐNG THEO DÕI GIÁ PHẾ LIỆU 🔄

YÊU CẦU : 

1. api : chứa code get data từ web data https://muaphelieuthinhphat.com/bang-gia-thu-mua-phe-lieu-hom-nay/.rồi in data lấy được lên api dưới dạng json
   

   ![main](https://github.com/khanh25012/he-thong-theo-doi-gia-phe-lieu/assets/129476200/183162f3-09f6-4c5b-a83b-7e94f82ab812)



2.node red: gọi API ,dùng bulk insert lưu cả mảng  và đẩy data thu được vào mssql.


  ![bulk insert save mảng](https://github.com/khanh25012/he-thong-theo-doi-gia-phe-lieu/assets/129476200/55b93e7a-70e2-4b77-afb5-3047798f7f3b)


  ![sqlnode](https://github.com/khanh25012/he-thong-theo-doi-gia-phe-lieu/assets/129476200/33f0111a-5e73-499e-92a8-fe47d681894d)



3.MSSQL :tạo db PhelieuDatabase ,table sat_vun để lưu id,tên sắt vụn và đơn giá.


tạo producer InsertSatVun để lấy data từ node truyền về và tạo procedure selectdata để lấy data đã lưu dùng cho web view


  ![datasql](https://github.com/khanh25012/he-thong-theo-doi-gia-phe-lieu/assets/129476200/7ab49e0a-a9bf-4118-94dc-17b2c0fd742a)

    
4.api select data lấy data lưu trong mssql hiện ra api


   ![selectdata](https://github.com/khanh25012/he-thong-theo-doi-gia-phe-lieu/assets/129476200/6fa24f03-1c59-4ed0-9528-315e7f4b1e69)



5.web hiển thị ( HTML,css,js ) :call ajax api select data ,lấy data từ api select data và show lên web ,data lúc này đang lỗi stt nên dùng var idCounter = 1;để gán cho stt tăng dần từ 1

   ![ketqua](https://github.com/khanh25012/he-thong-theo-doi-gia-phe-lieu/assets/129476200/a2a59a20-08f7-4db2-b1b7-5def63ac857a)


( đã đóng gói project python (api) thành service với NSSM thành công,click vào là ra project.)


   ![mnnm](https://github.com/khanh25012/he-thong-theo-doi-gia-phe-lieu/assets/129476200/e782938f-1d86-4f84-ba9f-b87dfe16824a)


                                                    Sơ đồ hoạt động


  ![sodo](https://github.com/khanh25012/he-thong-theo-doi-gia-phe-lieu/assets/129476200/342e2437-41c5-4c45-8a2a-602c8f385c3d)


