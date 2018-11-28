from try_logging import logging_files
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.DEBUG,
    filename='./Python/try_test/need_another.log',
    format=
    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(__name__+'.log') 
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler() 
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter) 
ch.setFormatter(formatter) 

logger.addHandler(fh) 
logger.addHandler(ch) 

logging_files()

logging.info('Calling Now!!!')

logger.info('It\'s logger')
logger.info('It\'s fh.logger')


logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
rHandler = RotatingFileHandler("log.txt",maxBytes = 100*1024*1024,backupCount = 999)
rHandler.setLevel(logging.INFO)
rHandler.setFormatter(formatter)
 
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
 
logger.addHandler(rHandler)
logger.addHandler(console)
 
logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")