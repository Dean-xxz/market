#__author__ = "Dean"
#__email__ = "1220543004@qq.com"

"""
此处提供天易商城个人中心模块所需公共api
"""
import random,string,json
from django.core.cache import cache
from utils.view_tools import ok_json, fail_json,get_args
from utils.abstract_api import AbstractAPI
from utils.paginator import json_pagination_response, dict_pagination_response

from .models import User_profile
from .utils import send_message_new

"""
descp:手机发送验证码接口
input:phone
output:successful or faild

"""

class CodeSendAPI(AbstractAPI):
    def config_args(self):
        self.args = {
            'phone':'r',
        }

    def access_db(self, kwarg):
        phone = kwarg['phone']
        code = ""
        for i in range(6):
            code += random.choice(string.digits)

        cache_key = "DYNAMIC_CODE" + str(phone)
        cache.set(cache_key, code, 60 * 6)
        content = "您的验证码为%s，%s分钟内有效。如需帮助，请联系400-998-1190【天易商城】" % (str(code), str(6))
        send_message_new(phone, content, is_code=True)
        return 'send successful'

    def format_data(self, data):
        return ok_json(data = data)


send_code_api = CodeSendAPI().wrap_func()



"""
descp:验证码验证接口，验证成功则返回用户登录成功信息，验证不成功，则返回失败
input:code
"""

class CodeVerifyAPI(AbstractAPI):
    def config_args(self):
        self.args = {
            'phone':'r',
            'code':'r',
        }


    def access_db(self, kwarg):
        phone = kwarg['phone']
        code = kwarg['code']

        cache_key = "DYNAMIC_CODE" + str(phone)
        cache_code = cache.get(cache_key)
        if cache_code == str(code):
            try:
                user = User_profile.objects.get(phone = phone)
                user = user.get_json()
                user.pop('is_active')
                user.pop('update_time')
                user.pop('create_time')
                user['user_id'] = user['id']
                user.pop('id')
                return user
            except User_profile.DoesNotExist:
                user = User_profile(phone = phone)
                user.save()
                user = user.get_json()
                user.pop('is_active')
                user.pop('update_time')
                user.pop('create_time')
                user['user_id'] = user['id']
                user.pop('id')
                return user
        else:
            return None

    def format_data(self, data):
        if data is not None:
            return ok_json(data = data)
        return fail_json('Verification failure')


verify_code_api = CodeVerifyAPI().wrap_func()


"""
descp:创建或更新收货人地址
input:address,re_phone,receiver,user_id
output:successful or faild
"""

class UserProfileUpdateAPI(AbstractAPI):
    def config_args(self):
        self.args = {
            'user_id':'r',
            'address':('o',None),
            're_phone':('o',None),
            'receiver':('o',None)
        }

    def access_db(self, kwarg):
        user_id = kwarg['user_id']
        address = kwarg['address']
        re_phone = kwarg['re_phone']
        receiver = kwarg['receiver']

        if address:
            r = User_profile.objects.filter(pk = user_id).update(address = address)
        if re_phone:
            r = User_profile.objects.filter(pk = user_id).update(re_phone = re_phone)
        if receiver:
            r = User_profile.objects.filter(pk = user_id).update(receiver = receiver)

        return 'update successful'


    def format_data(self, data):
        return ok_json(data = data)


update_userprofile_api = UserProfileUpdateAPI().wrap_func()
