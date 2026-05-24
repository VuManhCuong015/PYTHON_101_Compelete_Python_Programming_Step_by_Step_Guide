#flask framework
from flask import Flask

app = Flask(__name__)#tao mot ung dung ưeb(app),__name__ giup xac dinh vi tri file

@app.route('/')#neu nguoi dung truy cap trang chu duong dan '/' se chay ham o duoi
def hello_world():
    return 'Hello, World!'#tra ve dong chu nay tren man hinh trinh duyet cua khach

if __name__ == '__main__':#kiem tra file main py nay duoc chay truc tiep
    app.run(debug=True)#debug = true tu dong cap nhat web hoac sua doi khi ban sua code