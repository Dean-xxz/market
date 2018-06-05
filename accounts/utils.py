#接入短信服务的功能模块
from urllib import request,parse
import hashlib,json
from django.utils.timezone import now,localtime


def send_message_new(num,content,is_code = False):
    """
    漫道的接口
    暂时只能发送单条短信
    """
    error_list = ["2","4","5","6","7","8","9","10","11","12","14","17","19","20","22","23","601","602","603","604","605","606","607","608","609","610","611","623","624"]
    config = dict(
        url = "http://sdk2.entinfo.cn:8061/mdsmssend.ashx?%s",
        sn = "SDK-WSS-010-08608",
        pwd = "e-1(6e-4",
        mobile = "",
        content = content
        )
    if is_code:
        config['ext'] = 1
    url = config.pop('url')
    if isinstance(num,(int,str)):
        config['mobile'] = str(num)
    elif isinstance(num,list):
        config['mobile'] = ','.join(num)
    config['pwd'] = hashlib.md5((config['sn'] + config['pwd']).encode('utf-8')).hexdigest().upper()

    data = json.dumps(config)
    url = url%parse.urlencode(config)
    req = request.urlopen(url,data.encode('utf-8'))
    res = req.read().decode('utf-8')
    req.close()


