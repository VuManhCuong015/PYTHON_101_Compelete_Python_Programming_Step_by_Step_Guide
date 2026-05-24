from django.urls import path
import View

# Danh sách định tuyến các đường dẫn của trang web
urlpatterns = [
    path('', View.hello_world),
]

if __name__ == '__main__':
    import sys
    from django.conf import settings
    from django.core.management import execute_from_command_line
    from django import setup

    if not settings.configured:
        settings.configure(
            DEBUG=True,
            ROOT_URLCONF=__name__,  # Chạy định tuyến tại chính file này
            SECRET_KEY='key_chay_truc_tiep',
            ALLOWED_HOSTS=['*'],
        )
        setup()

    args = [sys.argv[0], 'runserver']
    execute_from_command_line(args)