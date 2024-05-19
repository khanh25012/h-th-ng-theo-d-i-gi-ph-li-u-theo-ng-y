from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get('/test')
def test():
    return {"name": "Rong do", "value": 500}

@app.get('/')
def get_data():
    try:
        url = 'https://muaphelieuthinhphat.com/bang-gia-thu-mua-phe-lieu-hom-nay/'
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra xem yêu cầu có thành công không
        soup = BeautifulSoup(response.content, 'html.parser')

        # Trích xuất dữ liệu từ trang web
        table = soup.find('table')  # Giả sử bảng đầu tiên chứa dữ liệu mong muốn
        if not table:
            raise ValueError("Không tìm thấy bảng nào trong trang web.")

        data = []
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:  # Kiểm tra nếu hàng có ít nhất 2 cột
                # Kiểm tra xem cột đầu tiên có hợp lệ không (phải có dữ liệu và không rỗng)
                if cols[0].get_text(strip=True) and cols[1].get_text(strip=True):
                    item = {
                        "name": cols[0].get_text(strip=True),
                        "value": cols[1].get_text(strip=True)
                    }
                    data.append(item)
                    if len(data) >= 45:  # Chỉ lấy 45 dòng
                        break

        if len(data) < 45:
            raise ValueError("Không tìm thấy đủ 45 dòng dữ liệu.")

        # Tên các mục cần lấy, đã loại bỏ các mục không mong muốn
        items_to_keep = [
            "Đồng đỏ",
            "Đồng vàng",
            "Mạt đồng vàng",
            "Đồng cháy",
            "Sắt vụn",
            "Sắt gỉ sét",
            "Bazo sắt",
            "Bã sắt",
            "Sắt công trình",
            "Dây sắt thép",
            "Chì dẻo",
            "Bao nhựa",
            "PP",
            "PVC",
            "HI",
            "Ống nhựa",
            "Giấy báo",
            "Giấy photo",
            "Inox 304, Inox 316",
            "Inox 410, Inox 420, Inox 430",
            "Ba dớ Inox",
            "Nhôm loại 2 (hợp kim nhôm)",
            "Nhôm loại 3 (vụn nhôm, mạt nhôm)",
            "Bột nhôm",
            "Nhôm dẻo",
            "Nhôm máy",
            "Thiếc",
            "Nilon dẻo",
            "Nilon xốp",
            "Nhựa"
        ]

        # Chỉ giữ lại các mục được liệt kê trong danh sách items_to_keep
        filtered_data = [item for item in data if item["name"] in items_to_keep]

        return {"ok": True, "msg": "Done", "data": filtered_data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Đã xảy ra lỗi khi truy cập dữ liệu: {str(e)}")
#uvicorn main:app --port=8888