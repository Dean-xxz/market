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

from .models import User_profile,Info
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
        cache.set(cache_key,code,60*5)
        print (code)
        content = "您的验证码为%s，5分钟内有效。如需帮助，请联系400-998-1190【天易商城】" % (str(code))
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
        data = User_profile.objects.get(pk = user_id)
        data = data.get_json()
        data.pop('is_active')
        data.pop('create_time')
        data.pop('update_time')
        return data


    def format_data(self, data):
        return ok_json(data = data)


update_userprofile_api = UserProfileUpdateAPI().wrap_func()



class UserQueryAPI(AbstractAPI):
    def config_args(self):
        self.args = {
            'user_id':'r',
        }

    def access_db(self, kwarg):
        user_id = kwarg['user_id']
        try:
            user = User_profile.objects.get(pk=user_id)
            user = user.get_json()
            user.pop('create_time')
            user.pop('update_time')
            user.pop('is_active')
            user['user_id'] = user['id']
            user.pop('id')
            return user
        except User_profile.DoesNotExist:
            return None

    def format_data(self, data):
        if data is not None:
            return ok_json(data = data)
        return fail_json('user is not exist')


query_user_api = UserQueryAPI().wrap_func()


#宽带信息创建接口
class InfoCreateAPI(AbstractAPI):
    def config_args(self):
        self.args = {
            'phone':'r',
            'id_card':'r',
            'address':'r',
            'date':'r',
            'user_id':'r',
            'name':'r',
        }

    def access_db(self, kwarg):
        user_id = kwarg['user_id']
        phone = kwarg['phone']
        id_card = kwarg['id_card']
        address = kwarg['address']
        name = kwarg['name']
        date = kwarg['date']

        try:
            info = Info.objects.get(user_id=user_id)
            info = Info.objects.filter(user_id=user_id).update(phone=phone,id_card=id_card,address=address,nick=name,date=date)
            data = Info.objects.get(user_id=user_id)
            data = data.get_json()
            data.pop('is_active')
            data.pop('create_time')
            data.pop('update_time')
            data['user_id'] = data['user']
            data.pop('user')
            return data
        except Info.DoesNotExist:
            info = Info(user_id=user_id,phone=phone,id_card=id_card,address=address,nick=name,date=date)
            info.save()
            if info:
                data = info.get_json()
                data.pop('is_active')
                data.pop('create_time')
                data.pop('update_time')
                data['user_id'] = data['user']
                data.pop('user')
                return data
            else:
                return None

    def format_data(self, data):
        if data is not None:
            return ok_json(data = data)
        return fail_json('save faild')


create_info_api = InfoCreateAPI().wrap_func()


#宽带信息查询接口
class InfoQueryAPI(AbstractAPI):
    def config_args(self):
        self.args = {
            'user_id':'r',
        }

    def access_db(self, kwarg):
        user_id = kwarg['user_id']
        info = Info.objects.filter(user_id=user_id).first()
        if info is not None:
            info = info.get_json()
            info.pop('is_active')
            info.pop('update_time')
            info.pop('create_time')
            return info
        else:
            info = {}
            return info
        return 'send successful'

    def format_data(self, data):
        return ok_json(data = data)


query_info_api = InfoQueryAPI().wrap_func()

