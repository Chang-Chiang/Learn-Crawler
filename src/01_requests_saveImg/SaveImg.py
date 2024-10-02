import os
import requests

# 切换工作路径为当前文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

if __name__ == "__main__":
    response =  requests.get("https://www.baidu.com/img/bd_logo1.png")
    with open("a.png","wb") as f:
        f.write(response.content)