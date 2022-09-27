import sys


def cal(oprd1, oprt, oprd2):
    oprd1 = float(oprd1.rstrip())
    oprd2 = float(oprd2.rstrip())
    oprt = oprt.rstrip()
    if oprt == '+':
        return oprd1 + oprd2
    elif oprt == '-':
        return oprd1 - oprd2
    elif oprt == '*':
        return oprd1 * oprd2
    elif oprt == '/':
        return oprd1 / oprd2


if __name__ == "__main__":
    answer = cal(sys.argv[1], sys.argv[2], sys.argv[3])
    # answer = cal("123", "+", "456")
    # print(answer)
    body = f'''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>
            Calculator
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
            .container {{
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
            .container form {{
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
        <div class = "container"><div class="tit"> 计算器</div>
        <form method="post" enctype="text/plain" name="myForm" action="/cgi-bin/calculator.py">
            <input type="text" name="oped1" placeholder="数字1">
            <input type="text" name="opt" placeholder="运算符">
            <input type="text" name="oped2" placeholder="数字2">
            <button type="submit">计算</button>
        </form>
        <form name="output">
            <p>结果</p>
            <textarea type="text" name="text_output" id="text3">{answer}</textarea>
        </form>
      </div>
    </body>
</html>'''
    print(body)
