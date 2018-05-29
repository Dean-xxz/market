#coding=utf-8
#accounts model error code in range (1000,19999)

ERROR_CODE_INVALID_USER_ERROR = 10000
ERROR_CODE_USERNAME_OR_PASSWORD_IS_FAILED_ERROR = 10001
ERROR_CODE_USERNAME_ALREADY_EXISTS_ERROR = 10002
ERROR_CODE_USER_CREATE_FAILED_ERROR = 10003
ERROR_CODE_DATABASE_ACCOUNTS_QUERY_ERROR = 10004
ERROR_CODE_DATABASE_ACCOUNTS_UPDATE_ERROR = 10005
ERROR_CODE_PHONE_OR_CODE_IS_FAILED_ERROR = 10006
ERROR_CODE_PHONE_VERIFICATE_FAILER_DEEOR = 10007

#learning model error code in range (30000,39999)

ERROR_CODE_DATABASE_LEARNING_QUERY_ERROR = 30000


# Client ERROR CODE in range (20000, 29999)
ERROR_CODE_UNAUTHORIZED = 20000
ERROR_CODE_INVALID_ARGS = 20001
ERROR_CODE_UNDEFINED = 20002






_error_map = {ERROR_CODE_INVALID_USER_ERROR: "%s: 无效的用户" % ERROR_CODE_INVALID_USER_ERROR,
              ERROR_CODE_USERNAME_OR_PASSWORD_IS_FAILED_ERROR:"%s: 用户名或密码错误" % ERROR_CODE_USERNAME_OR_PASSWORD_IS_FAILED_ERROR,
              ERROR_CODE_USERNAME_ALREADY_EXISTS_ERROR: "%s: 用户名已存在" % ERROR_CODE_USERNAME_ALREADY_EXISTS_ERROR,
              ERROR_CODE_USER_CREATE_FAILED_ERROR: "%s: 创建用户失败." % ERROR_CODE_USER_CREATE_FAILED_ERROR,
              ERROR_CODE_DATABASE_ACCOUNTS_QUERY_ERROR: "%s: 数据库用户查询错误" % ERROR_CODE_DATABASE_ACCOUNTS_QUERY_ERROR,
              ERROR_CODE_INVALID_ARGS: "%s: 无效的输入参数" % ERROR_CODE_INVALID_ARGS,
              ERROR_CODE_DATABASE_ACCOUNTS_UPDATE_ERROR: "%s: 用户模块数据库更新错误" % ERROR_CODE_DATABASE_ACCOUNTS_UPDATE_ERROR,
              ERROR_CODE_PHONE_OR_CODE_IS_FAILED_ERROR: "%s: 手机号或手机验证码错误" % ERROR_CODE_PHONE_OR_CODE_IS_FAILED_ERROR,
              ERROR_CODE_PHONE_VERIFICATE_FAILER_DEEOR: "%s: 手机号验证失败" % ERROR_CODE_PHONE_VERIFICATE_FAILER_DEEOR,
              ERROR_CODE_DATABASE_LEARNING_QUERY_ERROR: "%s: 学习模块数据库查询错误" % ERROR_CODE_DATABASE_LEARNING_QUERY_ERROR,
              }



def get_error_desp(code):
    """
    获取错误描述
    """
    return _error_map.get(code, "unknown error code")

