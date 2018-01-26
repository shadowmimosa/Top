#coding=utf-8

##==================================请求头参数（开发测试生产环境通用）=======================
#请求头参数-前端系统版本号
SYSVERSION='11.2.1'

#请求头参数-设备号
deviceToken='cb9012fd0302813461884e4a3fcc382886b73f6518c1dbe1f031a3901ee72eb4'

#请求头参数-客户端浏览器
UserAgent='joyRunner/3.1.0 (iPhone; iOS 11.2.1; Scale/3.00)'

#请求头参数-APP的开发版本号
APPDEVINFO='iOS#3.1.0.01101444'

#请求头参数-设备类型
MODELTYPE='iPhone 7 Plus'

#请求头参数-cookies中app的版本号信息
appversion='ios3.1.1'

#请求头参数Content-Type
#ContentType='application/x-www-form-urlencoded'


#===============测试环境下连接地址(Test)=======================

# 登录地址
login_URL='http://api-test.thejoyrun.com' 

#api项目地址
api_URL='http://api-test.thejoyrun.com' 

# user用户工程,与用户信息相关
user_URL='http://u-test.api.thejoyrun.com' 

# topic工程,与首页相关
topic_URL='http://topic-test.api.thejoyrun.com' 

# ec电商工程,与订单相关
ec_URL='http://ec-test.thejoyrun.com'

# advert工程,与消息广告通告相关
advert_URL='http://advert-test.api.thejoyrun.com'

# training工程,与训练相关
training_URL='http://training-test.api.thejoyrun.com'


#各版本测试（3.1）密钥
appkey1='fb1931e425f84313bfae4b93ab3ccdc4'

#业务测试密钥
appkey2='1fd6e28fd158406995f77727b35bf20a'

#前端验签名的版本号（需要与appkey1相对应，服务根据这个版本号验证appkey1）
APPVERSION='100.3.1.0'




#=======================线上发布连接地址(Online)========================

# # 登录地址
# login_URL='http://api.thejoyrun.com' 

# #api项目地址
# api_URL='http://api.thejoyrun.com' 

# # user用户信息工程,与用户相关
# user_URL='http://u.api.thejoyrun.com' 

# # ec电商相关,与php相关
# ec_URL='http://ec.thejoyrun.com'

# #各版本测试（3.1）密钥----需要更换成线上版本的密钥
# appkey1='fb1931e425f84313bfae4b93ab3ccdc4'

# #业务测试密钥----需要更换成线上版本的密钥
# appkey2='1fd6e28fd158406995f77727b35bf20a'

# #前端验签名的版本号（需要与appkey1相对应，服务根据这个版本号验证appkey1）
# APPVERSION='100.3.1.0'
