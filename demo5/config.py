#encoding:utf-8
import  os
CSRF_ENABLED = True # 启用csrf
SECRET_KEY = os.urandom(24) # 加密令牌,随机字符串
MAX_CONTENT_LENGTH = 1 * 1024 * 1024
