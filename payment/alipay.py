import os
from alipay import AliPay

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print (BASE_DIR)


app_private_key_string = open(BASE_DIR+"/payment/ali_key/rsa_private_key.pem").read()
alipay_public_key_string = open(BASE_DIR+"/payment/ali_key/rsa_public_key.pem").read()



alipay = AliPay(
    appid="2018060560276696",
    app_notify_url='http://tianyi.zhongkakeji.com/payment/notify/',  # 默认回调url
    app_private_key_string=app_private_key_string,
    alipay_public_key_string=alipay_public_key_string,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    sign_type="RSA2", # RSA 或者 RSA2
    debug=False,  # 默认False
)



def market_alipay(out_trade_no,total_amount,subject):
    order_string = alipay.api_alipay_trade_wap_pay(
        out_trade_no=out_trade_no,
        total_amount=total_amount,
        subject=subject,
        return_url="http://www.baidu.com",
        notify_url="http://tianyi.zhongkakeji.com/payment/notify/"  # 可选, 不填则使用默认notify url
    )
    pay_url = 'https://openapi.alipay.com/gateway.do?' + order_string
    return pay_url


# 手机网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
