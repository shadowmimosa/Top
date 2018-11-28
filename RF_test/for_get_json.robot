# *** Settings ***
# Library     MyLib                                          #导入自定义的库
# Library     SeleniumLibrary
*** Settings ***
# Library    ../Python/try_test/get_json_value_test.py
# Library     C:\Users\ShadowMimosa\Documents\STU\Top\Python\try_test\get_json_value_test.py
Library     ../Python/try_test/get_json_value_test.py
# Library     jsonpointer


*** Variable ***
${content}      {'foo': {'anArray': [ {'prop': 44}], 'another prop': {'baz': 'A string' }}, 'a%20b': 1, 'c d': 2}
${abc}      9
# ${content}        {"food": 123}
*** Test Cases ***
                                                            #第一行为固定格式，标识
                                                            #建议同python一致，使用tab缩进对齐(pycharm中设置tab=4空格)，否则可能报执行失败，报 "Test case contains no keywords"
case1 helloworld                                            #案例名
    log     chenyuebai first rfw case   

case2 path
    log     ../try_test/get_json_value_test

case3 runkeywordif
    Run Keyword If      ${abc}==9       log    right

case4 getjsonvalue
    get json value      ${content}      /foo

case5 getjsonvalue2
    get json value      ${content}      /c d

# case5 pointer_json
#     Run Keyword If      ${abc}==9       resolve pointer      ${content}      /another prop
    
# case6 log_data    
#     log                 ${content}



# *** Test Cases ***

# case1    getjsonvalue

# *** Variable ***
# ${content}    {'foo': {'anArray': [ {'prop': 44}], 'another prop': {'baz': 'A string' }}, 'a%20b': 1, 'c d': 2}


# *** Test Cases ***    expected_code
# Class1    [Documentation]    yi

# *** Keywords ***
#     ${json_data}    get json value    ${content}    'foo'
#     Run Keyword If    ${expected_code}=="0"    get json value    ${content}    'foo'
#     log    ------------------------ It is OK!!!!-------------------------------------