import Constant
import basic

b = basic.Basic()
print isinstance(b,basic.Basic)
basic.Basic().__real_get_access_token(b)
print b.get_access_token()
print Constant.APPID
