from bs4 import BeautifulSoup

def validate_html(html_code):
    try:
        soup = BeautifulSoup(html_code, 'html.parser')
        # 如果解析成功，则HTML代码是有效的
        return True
    except Exception as e:
        print('HTML validation error:', e)
        return False
        
# 要验证的HTML代码
html_code = '<html><head><title>Example</title></head><body><h1>Hello, world!</h1></body></html>'

# 验证HTML代码
is_valid = validate_html(html_code)
print('Is HTML valid?', is_valid)