import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='./Python/try_test/need.log',
    format=
    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logging.info('In the Original document')

def logging_files():
    logging.info('In the Function of the Original document')