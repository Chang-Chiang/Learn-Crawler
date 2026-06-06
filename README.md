# Learn-Crawler
Python 爬虫学习

## 目录

- [背景](#背景)
- [环境搭建](#环境搭建)
- [内容概览](#内容概览)
- [参考](#参考)

## 背景

- 需求：想要网页上的数据，但手动去搜索下载耗时耗力
- 问题：
    - 利用 python 发送请求：请求网站域名、请求参数、请求端的信息（避免被识别为爬虫）、请求端与服务端之间建立长期连接
    - 对获取的请求进行解析
    - html 网页元素

## 环境搭建

1. 安装 VSCode

2. VSCode 安装 Python 插件

3. 创建虚拟环境，本项目中使用 Conda 虚拟环境

    - show all commands（命令面板）: Windows 快捷键【ctrl + shift + p】，macOS 快捷键【command + shift + p】
    - 命令面板输入，**Python: Create Environment**
    - 选择 Conda
    - 选择 Python 版本

4. 编写测试程序

    - 创建目录

    - HelloWorld.py

        ```python
        if __name__ == '__main__':
            print("Hello, World!")
        ```
        
    
    - 执行
    
        ```shell
        python3 HelloWorld.py
        ```

## 内容概览

主要涉及网络基本知识（http 网页请求） + python 相关包的使用（requests、selenium、scrapy）

- http 请求流程
- 使用 requests 发送请求
- 使用 selenium
- 使用 scrapy

## 参考

- 项目局部虚拟环境搭建：https://blog.csdn.net/weixin_49895216/article/details/131696960

