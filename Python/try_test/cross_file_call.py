from get_json_value_test import get_json_value

obj = {
    'foo': {
        'anArray': [{
            'prop': 44
        }],
        'another prop': {
            'baz': 'A string'
        }
    },
    'a%20b': 1,
    'c d': 2
}
obj = str(obj)
print(type(obj))

obj_json = get_json_value(obj, '/foo')
print(obj_json)

obj_data = get_json_value('None', '/user')
print(obj_data)