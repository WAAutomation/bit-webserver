import sys
from DataBase import DataBase


def query(student_id):
    db = DataBase()
    # db.create_table()
    value = db.select_stu(student_id)

    if value:
        return value[1]
    else:
        return "No one was found"


if __name__ == '__main__':
    student_id = sys.argv[1].rstrip()
    # student_id = "108"
    answer = query(student_id)
    body = f'''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>
            Query Student
        </title>
        <style>
             * {{
                margin: 0;
                padding: 0;
            }}
            body {{
                /*窗口高度100%*/
                height: 100vh;
                /*布局：居中*/
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(-200deg,#e3b9d9,#aac2ee);
            }}
            .container form{{
                position: relative;
                z-index: 1;
                background-color: #fff;
                border-radius: 15px;
                /*垂直排列*/
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                width: 350px;
                height: 500px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            }}
            .container .tit {{
                font-size: 26px;
                margin: 50px auto 40px auto;
            }}
            .container input {{
                width: 200px;
                height: 40px;
                text-indent: 8px;
                border: none;
                border-bottom: 1px solid #ddd;
                outline: none;
                margin: 12px auto;
            }}
            .container button {{
                width: 200px;
                height: 40px;
                margin: 35px auto 40px auto;
                border: none;
                background: linear-gradient(-200deg,#e3b9d9,#aac2ee);
                color: #fff;
                font-weight: bold;
                letter-spacing: 8px;
                border-radius: 10px;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
      <div class = "container">
          <form method="post" enctype="text/plain" name="myForm" action="/cgi-bin/query.py">
              <div class="tit"> 查询学生信息</div>
              <input type="text" name="student_id" placeholder="学号" value="{student_id}">
              <button>查询</button>
              <p>结果</p>
              <h1>{answer}</h1>
          </form>
      </div>  
    </body>
</html>'''
    print(body)
