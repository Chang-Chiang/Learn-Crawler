import os
import requests
import json

# 切换工作路径为当前文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

if __name__ == "__main__":

    url = "http://fanyi.baidu.com/basetrans"

    # 反反爬
    headers = {
        # "Accept":"*/*",
        # "Accept-Encoding":"gzip, deflate",
        # "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,ru;q=0.7,zh-TW;q=0.6",
        # "Connection":"keep-alive",
        # "Content-Type":"application/x-www-form-urlencoded",
        # "Host":"fanyi.baidu.com",
        # "Origin":"http://fanyi.baidu.com",
        # "Referer":"http://fanyi.baidu.com/",
        "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
        # "X-Requested-With":"XMLHttpRequest",
        # "Cookie":"BAIDUID=B27C9ABD8A5079E6D8F42D0451E1CFA2:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1515338548; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BIDUPSID=B27C9ABD8A5079E6D8F42D0451E1CFA2; PSTM=1515339233; H_PS_PSSID=1437_24565_21117_17001; PSINO=6; locale=zh; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1515340680; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1515340680; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1515340680"
    }

    # data = {
    #     "from":"en",
    #     "to":"zh",
    #     "query":"hola",
    #     "transtype":"translang",
    #     "simple_means_flag":"3",
    #     "sign":"372549.85108",
    #     "token":"e89a8f037aac1b51a86cbc82356949d"
    # }

    data = {"query":"你好啊",
            "from":"zh",
            "to":"en"}
    r = requests.post(url, headers=headers, data=data)

    # print(r.content.decode())

    dict_ret = json.loads(r.content.decode())
    ret = dict_ret["trans"][0]["dst"]
    print("result is :",ret)