# requests 

## import

```python
import requests
```

## 基本 Get 请求

- 向网页发送请求：`requests.get(url)`

- 获取网页的响应信息：`response = requests.get(url)`

- 对网页响应信息解析
    - `response.text`
    - `response.content`
    - `response.status_code`
    - `response.requst.headers`
    - `response.headers`，基本只关注 Set-Cookie 字段
    
- 示例代码
  
    ```python
    # 发送请求
    response = requests.get("http://www.baidu.com")
    
    # 打印响应信息
    print(response.status_code)
    print(response.requests.url)
    print(response.request.headers)  # 默认请求头一眼可看出是爬虫
    print(response.request.content.decode()) # 被识别为爬虫，返回信息很少
    ```
    

## Get 带参请求

### 带请求头 header 参数

携带 header 信息，用于模拟浏览器，避免被识别为爬虫【反反爬】

```python
# 定义请求头参数
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}  # 字典

# 发送请求时, 带上请求头
response = requests.get(url, headers = headers)

# 打印响应信息
print(response.content.decode())
```

### 带请求参数

http发送请求时，相关参数作为明文发送

```python
# 百度搜索框输入 “甄嬛传”, 可看到请求的网址为
# https://www.baidu.com/s?wd=甄嬛传

# 定义请求网址
url = "https://www.baidu.com/s"

# 定义请求参数
params = {"wd": "甄嬛传"}  # 字典

# 请求网址也可定义为
# url = "https://www.baidu.com/s?wd={}".format("甄嬛传")

# 发送请求, 带请求头信息、请求参数信息
requests.get(url, headers = headers, params = params)
```

### [实战：爬取贴吧](../src/04_requests_tiebaSpider/TiebaSpider.py)

## POST 请求

> 场景
>
> - 登陆注册，POST 安全
> - 涉及到大文本，POST 请求对数据长度无要求

### data

```python
import requests

# 定义发送 post 请求时的 data 参数
formdata = {
    "type":"AUTO",
    "i":"i love python",
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}

# 请求网址
url = "http://fanyi.youdao.com/translatesmartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

# 请求头
headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

# 发送请求, 获取响应
response = requests.post(url, data = formdata, headers = headers)

# 打印响应信息
print (response.text)
# print (response.json())  # 如果是json文件可以直接显示
```

## 代理

> 背景：反反爬
>
> - 让请求的服务器以为请求来自不同的客户端
> - 防止真实地址泄漏

```python
# 准备一堆 IP 地址，随机选择一个 IP 使用
proxies = {
    "http": "http://12.34.56.79:9527",
    "https": "http://12.34.56.79:9527",
}
url = "http://www.baidu.com"
requests.get(url, params=proxies)
```

### 私密代理

```python
import requests

# 如果代理需要使用HTTP Basic Auth，可以使用下面这种格式：
proxy = { "http": "mr_mao_hacker:sffqry9r@61.158.163.130:16816" }

response = requests.get("http://www.baidu.com", proxies = proxy)

print (response.text)
```

### web 客户端验证

```python
import requests

# auth = ('用户名', '密码') 
auth = ('test', '123456')

response = requests.get('http://192.168.199.107', auth = auth)

print (response.text)
```

## cookies & session

### 作用

用于请求登陆之后的页面

### 区别

- cookies 存放在客户端浏览器，session 存放在服务器端
- cookies 不安全

### 获取 response 中的 cookie

```python
import requests

response = requests.get("http://www.baidu.com/")

# 返回 CookieJar 对象:
cookiejar = response.cookies

# 将 CookieJar 转为字典：
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

print (cookiejar)
print (cookiedict)
```

### requests 实现客户端和服务器端的会话保持

```python
# 实例化 session 对象
session = requests.session()

# 登陆
post_url = ""
post_data = {"email": "xxx", "password": "xxx"}
headers = {}
session.post(post_url, data = post_data, headers = headers)

# session 发送请求
response = session.get(url, headers = headers)
```

### requests 使用 cookie 访问登陆后页面

适用于：

- cookie 过期时间很长的网站
- cookie 过期前能拿到数据
- 其他程序获取cookie，当前程序利用 cookie 发送请求

```python
# 方法一：在 headers 中添加 cookie

# 方法二：request 请求添加 cookie
```

### session 实现人人网登录

```python
import requests

# 创建  session对象, 可以保存Cookie值
session = requests.session()

# 定义请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# 登录用户名、密码
data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}  

# 携带用户名、密码发送请求, 获取登录后的 Cookie 值, 保存在 session
session.post("http://www.renren.com/PLogin.do", data = data)

# session包含用户登录后的 Cookie 值, 可直接访问登录后才可以访问的页面
response = session.get("http://www.renren.com/410043129/profile")

# 打印响应内容
print (response.text)
```
