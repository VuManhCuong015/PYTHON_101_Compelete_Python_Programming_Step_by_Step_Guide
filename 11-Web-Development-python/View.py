from django.http import HttpResponse

# Hàm xử lý logic nhận vào một Request (Yêu cầu) từ khách
def hello_world(request):
    # Trả về một Response (Phản hồi) chứa dữ liệu dạng chữ đơn thuần
    return HttpResponse('Hello, World!')
