import jsonpointer
import json
import logging
from logging.handlers import RotatingFileHandler

# ### Logging can only be defined once in multithreading
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='./Python/try_test/get_json_value.log',
#     format=
#     '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

### Independent logs in file
logger = logging.getLogger(__name__)
if not logger.handlers:
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger.setLevel(logging.DEBUG)

    # handler_name = logging.FileHandler(__name__ + '.log')
    # handler_name.setLevel(logging.DEBUG)
    # handler_name.setFormatter(formatter)

    handler_backup = RotatingFileHandler(
        'backup_for_scriptlog.log', maxBytes=5 * 1024 * 1024, backupCount=999)
    handler_backup.setLevel(logging.INFO)
    handler_backup.setFormatter(formatter)

    logger.addHandler(handler_backup)
    # logger.addHandler(handler_name)

### global variable
null = None
true = True
false = False


def use_jsonpointer(doc, pointer):

    logger.info('The doc\'s type is %s', type(doc))
    logger.info('The doc is %s', doc)
    logger.info('The pointer\'s type is %s', type(pointer))
    logger.info('The pointer is %s', pointer)

    ### jsonpointer.resolve need a dict and str
    # if type(doc) == str and json.loads(doc.replace('\'', '\"')):
    if type(doc) == str and doc != '0':
        if doc == 'None':
            print('The data is null')
            # raise ValueError
            return 'null'
        doc = eval(doc)  ### Change str to dict
    elif type(doc) == dict:
        pass
    else:
        print('The parameter is \'0\'')
        doc_code = "0"
        return doc_code

    print('The doc\'s type after change is', type(doc))
    print('The data\'s type after filtering is',
          type(jsonpointer.resolve_pointer(doc, pointer)))
    print('The data\'s type after filtering is',
          jsonpointer.resolve_pointer(doc, pointer))

    pointer_in_doc = jsonpointer.resolve_pointer(doc, pointer)

    ### If the data return from Jsonpointer  is string, Changing it.
    if type(pointer_in_doc) == str:
        print('Change Python\'s string to Robot\'s string')
        print('The pointer_in_doc is str and it\'s', pointer_in_doc)
        pointer_in_doc = '\"' + pointer_in_doc + '\"'
        print('The pointer_in_doc is str and it\'s', pointer_in_doc)

    ### If the data return from Jsonpointer is null. Returning it.
    elif pointer_in_doc == None:
        print('It\'s Right!!!')
        return 'null'
    else:
        pointer_in_doc = str(jsonpointer.resolve_pointer(doc, pointer))

    print('The data\'s type after filtering and change is',
          type(pointer_in_doc))
    print('The data finally is', pointer_in_doc.replace('\'', '\"'))

    pointer_in_doc = pointer_in_doc.replace('\'', '\"')

    logger.info('The fianl doc\'s type is %s', type(pointer_in_doc))
    logger.info('The fianl doc is %s', pointer_in_doc)

    return pointer_in_doc


def use_self_method(doc, pointer):

    return 'None'


def get_json_value(doc, pointer, change_type=None):

    print('The doc\'s type is', type(doc))
    print('The doc is', doc)
    print('The pointer\' type is', type(pointer))
    print('The pointer is', pointer)

    if change_type == None:
        filter_doc = use_jsonpointer(doc, pointer)
        return filter_doc
    elif change_type == 'self_use':
        filter_doc = use_self_method(doc, pointer)


def to_str(anything):

    print(type(anything))
    print(anything)

    if type(anything) == bytes:
        ### Change anything to str
        anything = anything.decode('utf-8')
        return anything
    elif type(anything) == dict:
        anything = str(anything)
        print(anything)
        return anything
    else:
        return 'YOU ARE WRONG!!'


def get_int(one=None, two=None, three=None, four=None, five=None):

    if two == None and type(one) == str:
        print(type(one))

        if one == '0':
            return one
        new_one = ''
        sign = False

        for word in one:
            print(type(word))
            if word == '0' and sign == False:
                continue
            elif word != '0':
                sign = True
                new_one += word
            else:
                new_one += word

        return new_one
    else:
        pass

    num_list = [one, two, three, four, five]
    # veriable_list = ['one', 'two', 'three', 'four', 'five']
    new_list = []

    for index in range(len(num_list)):
        if num_list[index] != None:
            new_list.append(int(num_list[index]))
        else:
            continue

    return new_list[0], new_list[1], new_list[2], new_list[3], new_list[4]


### For debugging
if __name__ == '__main__':

    obj = {
        'foo': {
            'anArray': [{
                'prop': 44
            }, {
                'prop1': 45
            }],
            'another prop': {
                'baz': 'A string'
            }
        },
        'a%20b': 1,
        'c d': 2
    }

    json_need = get_json_value(obj, '/foo/anArray/1')
    print(json_need)

    mm, dd, hh, mm1, ss = get_int('02', '03', '04', '05', '06')
    print(mm)

    bb = get_int(
        '00000000013200000003414000041041040000200000000000000000000000000000002321331sjdadjaldjie0219313013091920310'
    )
    cc = get_int('0')
    print(bb, cc)
