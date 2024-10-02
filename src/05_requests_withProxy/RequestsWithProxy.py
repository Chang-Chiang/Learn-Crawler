import os
import requests

# 切换工作路径为当前文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

if __name__ == "__main__":
    proxies = {"http":"http://163.177.151.23:80"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
    r = requests.get("http://www.baidu.com", proxies=proxies, headers=headers)
    print(r.status_code)