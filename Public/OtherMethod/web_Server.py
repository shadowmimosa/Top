#coding=utf-8
'''
引入turbogears轻量级web框架，http://www.turbogears.org/
安装：pip install TurboGears2
运行：在进入文件目录运行.py文件即可；比如，此文件的行时可以在此文件所在目录，运行：web_server.py; 
'''
from wsgiref.simple_server import make_server
from tg import expose, TGController, AppConfig

class RootController(TGController):
	@expose()
	def index(self):
		return  "<h1> Hi,悦跑圈的同学们，该起来跑步了！！ </h1>"
config = AppConfig(minimal=True, root_controller=RootController())
print "Serving on port 9797..."
httpd = make_server('', 9797, config.make_wsgi_app())
httpd.serve_forever()