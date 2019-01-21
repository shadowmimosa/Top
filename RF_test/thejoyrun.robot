*** Settings ***

Library           RequestsLibrary
Library           ../Lib/method_private_forPy3.py
Library           ../Lib/tool_reptile.py
Library           ../Lib/tools_library.py
Resource          ../OtherMethod/cookie_operation.txt
Resource          ../Public/http_request.txt
Resource          jrtool.txt

*** Variables ***
${signOnline}     A4729E62-3701-48C3-A15D-7391838FA186    #可以放置一些公共参数；
${signTest}       a9ff6970eb814e6894389ca8b12f3030    #可以放置一些公共参数；
${signBeta}       A9FF6970EB814E6894389CA8B12F3030    #可以放置一些公共参数；
${mapp_sginTest}    MAPP-MASTER-SECRET-TEST
${mapp_sginBeta}    MAPP-MASTER-SECRET-TEST
${mapp_sginOnline}   27509554-6861-4394-9B84-9D5698A4DD1A
${pwd}            67889911    #可以放置一些公共参数；
${usersinfo_dict}    &{EMPTY}
${RetryInti}      ${3}    #设置重试次数

*** Keywords ***

thejoyrun_postd
    [Arguments]    ${path}    ${maps}    ${userName}    ${Base_URL}    ${pwds}=None    ${Retry}=None
    [Documentation]    *用于APP内部需要登录和签名Post场景：post请求data方式关键字*
    ...    ${userName}  中传uid/sid 模式时用的是sid访问，${pwds}不启作用
	...    ${pwds}  中传None时，密码为使用默认密码67889911
	...    ${Retry}  中传None时，默认重试3次，否则为传的次数；
    ...    参数以data方法提交，不出现Url中，而只在body中带公共参数（sign、timestamp）；
    [Timeout]    30 seconds
    log    thejoyrun_postd Start ......
    ${Retry}    Run Keyword If    '${Retry}'=='None'    set variable    ${RetryInti}
    ...    ELSE    set variable    ${Retry}
    #log    Retry=======================${Retry}
    ${pwd}    Run Keyword If    '${pwds}'=='None'    set variable    ${pwd}
    ...    ELSE    set variable    ${pwds}
    ${env}    Env_URL    ${Base_URL}
    ${userslist}    Get Dictionary Keys    ${usersinfo_dict}
    ${user_is}    Get Count    ${userslist}    ${env}${userName}
	${sid_and_uid}   Get Lines Matching Pattern    ${userName}    */*
	${sid_uidlist}    Run Keyword If  '${sid_and_uid}'!='${EMPTY}'   split string   ${userName}   /
	${sid_input}   Run Keyword If  '${sid_and_uid}'!='${EMPTY}'   Get From List  ${sid_uidlist}   -1
	${uid_input}   Run Keyword If  '${sid_and_uid}'!='${EMPTY}'   Get From List  ${sid_uidlist}   0
	${ypcookie_input}   Run Keyword If  '${sid_and_uid}'!='${EMPTY}'  set variable  uid=${uid_input}\&sid=${sid_input}
	${uid_sid_input}   Run Keyword If  '${sid_and_uid}'!='${EMPTY}'  create dictionary   uid=${uid_input}   sid=${sid_input}   ypcookie=${ypcookie_input}
    ${heards}    Run Keyword If    ${user_is}<=0 and '${sid_and_uid}'=='${EMPTY}'  joyrun_POST_heardsession    ${userName}    ${pwd}    ${Base_URL}
	...    ELSE IF   ${user_is}<=0 and '${sid_and_uid}'!='${EMPTY}'   set variable      ${uid_sid_input}
    ...    ELSE    Get From Dictionary    ${usersinfo_dict}    ${env}${userName}
    #从字典里取出相应key的值
    ${uid}=    Get From Dictionary    ${heards}    uid
    ${sid}=    Get From Dictionary    ${heards}    sid
    ${timestamp}    GetServertime    ${login_URL}
    ${ypcookie}=    Get From Dictionary    ${heards}    ypcookie
    ${heards_dict}=    create dictionary    ypcookie=${ypcookie}
    ##将ypcookie转为url编码
    ${ypcookie1}=    urlencode    ${ypcookie}
    ${cookies}=    create dictionary
    set to dictionary    ${cookies}    ypcookie=${ypcookie1}
    set to dictionary    ${cookies}    app_version=${appversion}
    #log    uid ===${uid}
    #log    sid ===${sid}
    #log    heards_dict ===${heards_dict}
    ${URL}=    set variable    ${Base_URL}
    ${sign_dict}=    create dictionary    timestamp=${timestamp}
    ${post_dict}=    create dictionary    timestamp=${timestamp}
    @{mapstolist_sign}=    evaluate    sorted(${maps}.items())
    : FOR    ${map}    IN    @{mapstolist_sign}
    \    set to dictionary    ${sign_dict}    ${map[0]}=${map[1]}
    @{mapstolist}=    evaluate    sorted(${maps}.items())
    : FOR    ${map}    IN    @{mapstolist}
    \    set to dictionary    ${post_dict}    ${map[0]}=${map[1]}
    ${sign_dict_tolist}=    evaluate    sorted(${sign_dict}.items())
    ${len}=    evaluate    len(${sign_dict_tolist})
    ${signparam} =    set variable    ${EMPTY}
    : FOR    ${index}    IN RANGE    0    ${len}
    \    ${signparamkey}    set variable    ${sign_dict_tolist[${index}][0]}
    \    ${signparamValue}    set variable    ${sign_dict_tolist[${index}][1]}
    \    ${signparamsting}    set variable    ${signparamkey}${signparamValue}
    \    ${signparam} =    set variable    ${signparam}${signparamsting}
    log    signparam=======${signparam}
    #排序及格式处理
    ${signkey1}    set variable    ${signparam}${appkey1}${uid}${sid}
    ${signkey2}    set variable    ${signparam}${appkey2}${uid}${sid}
    #${signkey1}=    Replace String    ${signkey1}    "    ${EMPTY}
    #${signkey2}=    Replace String    ${signkey2}    "    ${EMPTY}
    log    signkey1=====${signkey1}
    log    signkey2=====${signkey2}
    #排序及格式处理
    ${sign1}=    encrypt    ${signkey1}    md5    32
    ${sign2}=    encrypt    ${signkey2}    md5    32
    	${method_env}    Env_URL   ${Base_URL}
	log    运行环境是${method_env}:${Base_URL}
	${sign1}   Run Keyword IF    '${method_env}'=='Test'   Set Variable    ${signTest} 
	...		ELSE IF   '${method_env}'=='Online'   Set Variable    ${signOnline} 
	...		ELSE   Set Variable    ${signBeta}
	${_sign} =    Convert To Uppercase    ${sign1}	
    log    通用签名:${_sign}
    ${signature} =    Convert To Uppercase    ${sign2}
    log    业务签名：${signature}
    #处理设备ID
	${APPDEVINFO}   Replace String    ${APPDEVINFO}    DeveiceId    AutoTest_Joyrun_${username}
	${APPDEVINFO}	Replace String    ${APPDEVINFO}    UserID    ${uid}
    set to dictionary    ${heards_dict}    _sign=${_sign}
    set to dictionary    ${heards_dict}    APPVERSION=${APPVERSION}
    set to dictionary    ${heards_dict}    Content-Type=${ContentType}
    set to dictionary    ${heards_dict}    User-Agent=${UserAgent}
    set to dictionary    ${heards_dict}    APP_DEV_INFO=${APPDEVINFO}
    set to dictionary    ${heards_dict}    SYSVERSION=${SYSVERSION}
    set to dictionary    ${heards_dict}    MODELTYPE=${MODELTYPE}
    #log    _sign====${_sign}
    #log    signature====${signature}
    set to dictionary    ${post_dict}    signature=${signature}
    ${post_dict_tolist1}=    evaluate    sorted(${post_dict}.items())
    log    参数编码前：${post_dict}
    ${post_param}    Evaluate    urllib.parse.urlencode(${post_dict})    urllib
    log    参数编码后：${post_param}
    Create Session    run    ${URL}    headers=${heards_dict}    cookies=${cookies}
    ${resp}=    Post Request    run    uri=${path}    data=${post_param}
    ${ret_result}    charconver    ${resp.content}
    ${get_count}    Get Count    ${ret_result}    ret\":"401"
    ${ret0_count}    Get Count    ${ret_result}    ret\":"0"    #:FOR    ${index}    IN RANGE
    ...    # 0    ${RetryInti}    #\    Exit For Loop If    ${get_count} == 0    #\
    ...    # thejoyrun_postd    #\    ...    ${path}    ${maps}    ${userName}
    ...    # ${Base_URL}    ${pwds}    # ${Retry}
    Run Keyword If    ${get_count}==1    log    ${userName}的SID过期而登录失败
    Run Keyword If    ${get_count}==1    Pop From Dictionary    ${usersinfo_dict}    ${env}${userName}
    #Run Keyword If    ${ret0_count}==1    Set_Global_Var    ${path}    ${ret_result}    ${userName}    ${Base_URL}
    ${Retry}    Run Keyword If    ${get_count}==1    Evaluate    ${Retry}-1
    ...    ELSE    Set Variable    ${-1}
    ${resp}    Run Keyword If    ${get_count}==1 and ${Retry}>=0    thejoyrun_postd    ${path}    ${maps}    ${userName}
    ...    ${Base_URL}    ${pwds}    ${Retry}
    ...    ELSE    set variable    ${resp}
    log    thejoyrun_postd End ...
    [Return]    ${resp}

thejoyrun_postnl
    [Arguments]    ${path}    ${maps}    ${Base_URL}    ${Retry}=None
    [Documentation]    *用于APP内部不需登录的Post场景：post请求data方式关键字——无需登录*
    ...
    ...    用于app的用户注册方面，无需用户信息；参数以data方法提交，不出现Url中，而只在body中带公共参数（sign、timestamp）；
    [Timeout]    30 seconds
    log    thejoyrun_postnl Start ......
    ${Retry}    Run Keyword If    '${Retry}'=='None'    set variable    ${RetryInti}
    ...    ELSE    set variable    ${Retry}
    ${heards}=    create dictionary
    #从字典里取出相应key的值
    ##通过服务器获取timestamp
    ${heards_dict}=    create dictionary
    ${timestamp}    GetServertime    ${login_URL}
    ${cookies}=    create dictionary
    log    code加密处理
    log dictionary    ${maps}
    log    maps=====${maps}
    ${mapskey}    Get Dictionary Keys    ${maps}
    ${codeone}    Count Values In List    ${mapskey}    code
    ${cellone}    Count Values In List    ${mapskey}    cellNumber
    ${cellNumber}    Run Keyword If    ${codeone}>0 and ${cellone}>0    Get From Dictionary    ${maps}    cellNumber
    ${codekey}    Run Keyword If    ${codeone}>0 and ${cellone}>0    set variable    joy${timestamp}the${cellNumber}run
    ${code}    Run Keyword If    ${codeone}>0 and ${cellone}>0    encrypt    ${codekey}    md5    32
    ${code}    Convert To String    ${code}
    Run Keyword If    ${codeone}>0 and ${cellone}>0    set to dictionary    ${maps}    code=${code}
    log Dictionary    ${maps}
    log    maps=====${maps}
    set to dictionary    ${cookies}    app_version=${appversion}
    ${URL}=    set variable    ${Base_URL}
    ${sign_dict}=    create dictionary    timestamp=${timestamp}
    log dictionary    ${sign_dict}
    ${post_dict}=    create dictionary    timestamp=${timestamp}
    @{mapstolist_sign}=    evaluate    sorted(${maps}.items())
    : FOR    ${map}    IN    @{mapstolist_sign}
    \    set to dictionary    ${sign_dict}    ${map[0]}=${map[1]}
    \    log dictionary    ${sign_dict}
    @{mapstolist}=    evaluate    sorted(${maps}.items())
    : FOR    ${map}    IN    @{mapstolist}
    \    set to dictionary    ${post_dict}    ${map[0]}=${map[1]}
    \    log dictionary    ${post_dict}
    ${sign_dict_tolist}=    evaluate    sorted(${sign_dict}.items())
    ${len}=    evaluate    len(${sign_dict_tolist})
    ${signparam} =    set variable    ${EMPTY}
    : FOR    ${index}    IN RANGE    0    ${len}
    \    ${signparamkey}    set variable    ${sign_dict_tolist[${index}][0]}
    \    ${signparamValue}    set variable    ${sign_dict_tolist[${index}][1]}
    \    ${signparamsting}    set variable    ${signparamkey}${signparamValue}
    \    ${signparam} =    set variable    ${signparam}${signparamsting}
    log    signparam=======${signparam}
    #排序及格式处理
    ${signkey1}    set variable    ${signparam}${appkey1}
    ${signkey2}    set variable    ${signparam}${appkey2}
    log    signkey1=====${signkey1}
    log    signkey2=====${signkey2}
    #排序及格式处理
    ${sign1}=    encrypt    ${signkey1}    md5    32
    ${sign2}=    encrypt    ${signkey2}    md5    32
    #通用签名
    ${method_env}    Env_URL   ${Base_URL}
	log    运行环境是${method_env}:${Base_URL}
	${sign1}   Run Keyword IF    '${method_env}'=='Test'   Set Variable    ${signTest} 
	...		ELSE IF   '${method_env}'=='Online'   Set Variable    ${signOnline} 
	...		ELSE   Set Variable    ${signBeta}
	${_sign} =    Convert To Uppercase    ${sign1}
    log    通用签名:${_sign}
    ${signature} =    Convert To Uppercase    ${sign2}
    log    业务签名：${signature}
    #处理设备ID
	${APPDEVINFO}   Replace String    ${APPDEVINFO}    DeveiceId    AutoTest_Joyrun_${username}
	${APPDEVINFO}	Replace String    ${APPDEVINFO}    UserID    -1
    set to dictionary    ${heards_dict}    _sign=${_sign}
    set to dictionary    ${heards_dict}    APPVERSION=${APPVERSION}
    set to dictionary    ${heards_dict}    Content-Type=${ContentType}
    set to dictionary    ${heards_dict}    User-Agent=${UserAgent}
    set to dictionary    ${heards_dict}    APP_DEV_INFO=${APPDEVINFO}
    set to dictionary    ${heards_dict}    SYSVERSION=${SYSVERSION}
    set to dictionary    ${heards_dict}    MODELTYPE=${MODELTYPE}
    #log    _sign====${_sign}
    #log    signature====${signature}
    set to dictionary    ${post_dict}    signature=${signature}
    ${post_dict_tolist1}=    evaluate    sorted(${post_dict}.items())
    log    参数编码前：${post_dict}
    ${post_param}    Evaluate    urllib.parse.urlencode(${post_dict})    urllib
    log    参数编码后：${post_param}
    #${post_param}=    Evaluate    '${post_param}'.decode('unicode_escape')    #对中文做处理，将unicode字符解码成对应的中文字符
    Create Session    run    ${URL}    headers=${heards_dict}    cookies=${cookies}
    ${resp}=    Post Request    run    uri=${path}    data=${post_param}
    ${get_count}    Run Keyword If    ${resp.status_code}==200    Set Variable    ${0}
    ...    ELSE    Set Variable    ${1}
    ${Retry}    Run Keyword If    ${get_count}==1    Evaluate    ${Retry}-1
    ...    ELSE    Set Variable    ${-1}
    ${resp}    Run Keyword If    ${get_count}==1 and ${Retry}>=0    thejoyrun_postnl    ${path}    ${maps}    ${Base_URL}
    ...    ${Retry}
    ...    ELSE    set variable    ${resp}
    Run Keyword If    ${get_count} == 0    Return From Keyword    ${resp}
    log    thejoyrun_postnl End ......
    [Return]    ${resp}

thejoyrun_post_nosign
    [Arguments]    ${path}    ${maps}    ${userName}    ${Base_URL}    ${pwds}=None    ${Retry}=None
    [Documentation]    *用于非APP的页面请求不需签名的场景：joyrun中post请求URL方式关键字*
    ...
    ...    没有加密的用于非APP的页面请求，参数以data方法提交；
    [Timeout]    30 seconds
    log    thejoyrun_post_nosign Start ......
    ${Retry}    Run Keyword If    '${Retry}'=='None'    set variable    ${RetryInti}
    ...    ELSE    set variable    ${Retry}
    ${pwd}    Run Keyword If    '${pwds}'=='None'    set variable    ${pwd}
    ...    ELSE    set variable    ${pwds}
    ${env}    Env_URL    ${Base_URL}
    ${userslist}    Get Dictionary Keys    ${usersinfo_dict}
    ${user_is}    Get Count    ${userslist}    ${env}${userName}
    ${heards}    Run Keyword If    ${user_is}<=0    joyrun_POST_heardsession    ${userName}    ${pwd}    ${Base_URL}
    ...    ELSE    Get From Dictionary    ${usersinfo_dict}    ${env}${userName}
    #从字典里取出相应key的值
    ${uid}=    Get From Dictionary    ${heards}    uid
    ${sid}=    Get From Dictionary    ${heards}    sid
    ${timestamp}    GetServertime    ${login_URL}
    ${ypcookie}=    Get From Dictionary    ${heards}    ypcookie
    ${heards_dict}=    create dictionary    ypcookie=${ypcookie}
    ${URL}=    set variable    ${Base_URL}
    ##将ypcookie转为url编码
    ${ypcookie1}=    urlencode    ${ypcookie}
    ${cookies}=    create dictionary
    set to dictionary    ${cookies}    ypcookie=${ypcookie1}
    set to dictionary    ${cookies}    app_version=${APPVERSION}
    log    uid ===${uid}
    log    sid ===${sid}
    log    heards_dict ===${heards_dict}
    ${post_dict}=    create dictionary
    @{mapstolist}=    evaluate    sorted(${maps}.items())
    : FOR    ${map}    IN    @{mapstolist}
    \    set to dictionary    ${post_dict}    ${map[0]}=${map[1]}
    #处理设备ID
	${APPDEVINFO}   Replace String    ${APPDEVINFO}    DeveiceId    AutoTest_Joyrun_${username}
	${APPDEVINFO}	Replace String    ${APPDEVINFO}    UserID    ${uid}
    set to dictionary    ${heards_dict}    APPVERSION=${APPVERSION}
    set to dictionary    ${heards_dict}    Content-Type=${ContentType}
    set to dictionary    ${heards_dict}    User-Agent=${UserAgent}
    set to dictionary    ${heards_dict}    APP_DEV_INFO=${APPDEVINFO}
    set to dictionary    ${heards_dict}    SYSVERSION=${SYSVERSION}
    set to dictionary    ${heards_dict}    MODELTYPE=${MODELTYPE}
    log    参数编码前：${post_dict}
    ${post_param}    Evaluate    urllib.parse.urlencode(${post_dict})    urllib
    log    参数编码后：${post_param}
    #因后端和运维的签名方法不一致，兼容处理
    ${path}    set variable    ${path}?${post_param}
    ####
    Create Session    run    ${URL}    headers=${heards_dict}    cookies=${cookies}
    #${resp}=    Post Request    run    uri=${path}    data=${post_param}
    ${resp}=    Post Request    run    uri=${path}
    ${Temporary}     To Str       ${resp.content}
    ${get_count}    Get Count    ${Temporary}    ret\":"401"
    # ${get_count}    Get Count    ${resp.content}    ret\":"401"
    Run Keyword If    ${get_count}==1    log    ${userName}的SID过期而登录失败
    Run Keyword If    ${get_count}==1    Pop From Dictionary    ${usersinfo_dict}    ${env}${userName}
    ${Retry}    Run Keyword If    ${get_count}==1    Evaluate    ${Retry}-1
    ...    ELSE    Set Variable    ${-1}
    ${resp}    Run Keyword If    ${get_count}==1 and ${Retry}>=0    thejoyrun_post_nosign    ${path}    ${maps}    ${userName}
    ...    ${Base_URL}    ${pwds}    ${Retry}
    ...    ELSE    set variable    ${resp}
    Run Keyword If    ${get_count} == 0    Return From Keyword    ${resp}
    log    thejoyrun_post_nosign End ......
    [Return]    ${resp}

thejoyrun_postjson_wxminp
    [Arguments]    ${path}    ${maps}    ${Base_URL}    ${uid}=None
    [Documentation]    *用于微信小程序Post场景：joyrun中post请求json方式关键字*
    ...
    ...    参数以data提交，在出现Url中，也在body中带公共参数（appid、timestamp、sid主要用于小程序）；
    [Timeout]    30 seconds
    log    thejoyrun_postjson_wxminp Start ......
    ##通过本地获取timestamp
    ${ContentType}    Set Variable    application/json;charset=UTF-8
    ${wxminpnames}    Split String    ${path}    /
    ${wxminpname1}    Get From List    ${wxminpnames}    1
    ${wxminpname}    Run Keyword If    '${wxminpname1}'!='wallet'    set variable    ${wxminpname1}
    ...    ELSE    Set variable    corpcrew
    ${appid}    set variable    ${${wxminpname}appid}
    ${sid}    set variable    ${${wxminpname}sid}
    #${appkey}    set variable    ${${wxminpname}appkey}
    ${appkey}    set variable    ${mappkey}
    ${time}    GetServertime    ${login_URL}
    ${time}    evaluate    int(${time}*1000)
    ${timestamp}    set variable    ${time}
    log    timestamp=${timestamp}
    #当需要传uid时，则uid从map中取，否则uid为0
    ${mapskey}    Get Dictionary Keys    ${maps}
    ${k}    Get Count    ${mapskey}    uid
    ${uid}    Run Keyword If    ${k}==1    Get From Dictionary    ${maps}    uid
    ...    ELSE    set variable    0
    ${heards_dict}=    create dictionary
    log    sid ===${sid}
    log    heards_dict ===${heards_dict}
    ${URL}=    set variable    ${Base_URL}
    ${post_dict}=    create dictionary    &{maps}
    #公共参数timestamp、appid、sid
    set to dictionary    ${post_dict}    timestamp=${timestamp}
    set to dictionary    ${post_dict}    appid=${appid}
    set to dictionary    ${post_dict}    sid=${sid}
    log    post_dict：${post_dict}
    #${post_param}    Evaluate    urllib.parse.urlencode(${post_dict})    urllib
    #log    参数编码后：${post_param}
    #签名
    ${signkey}=    Run Keyword If    ${uid}==0    set variable    ${appid}${timestamp}${sid}${appkey}
    ...    ELSE    set variable    ${appid}${timestamp}${sid}${uid}${appkey}
    ${signkey}=    Replace String    ${signkey}    "    ${EMPTY}
    log    signkey=====${signkey}
    #排序及格式处理
    ${sign}=    encrypt    ${signkey}    md5    32
    log    使用万能签名${mapp_sgin}
    ${wxenv}    Env_URL    ${Base_URL} 
	${mapp_sgin}   Run Keyword IF   '${wxenv}'=='Test'  Set Variable  ${mapp_sginTest}
	...		ELSE IF  '${wxenv}'=='Online'   Set Variable  ${mapp_sginOnline}
	...		ELSE    Set Variable  ${mapp_sginBeta}
    ${sign}=    Set Variable    ${mapp_sgin}
    #请求头处理${UserAgent}
    set to dictionary    ${heards_dict}    sign=${sign}
    set to dictionary    ${heards_dict}    Content-Type=${ContentType}
    set to dictionary    ${heards_dict}    User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X)
    Create Session    runwx    ${URL}    headers=${heards_dict}
    ${resp}=    Post Request    runwx    uri=${path}    data=${post_dict}
    log    thejoyrun_postjson_wxminp End ......
    [Return]    ${resp}

thejoyrun_get_wxminp
    [Arguments]    ${path}    ${maps}    ${Base_URL}    ${uid}=None
    [Documentation]    *用于微信小程序Get场景：joyrun中get请求关键字*
    ...
    ...    参数以params提交，在出现Url中，带公共参数（appid、timestamp、sid主要用于跑团小程序）；
    [Timeout]    30 seconds
    log    thejoyrun_get_wxminp Start ......
    ${wxminpnames}    Split String    ${path}    /
    ${wxminpname1}    Get From List    ${wxminpnames}    1
    ${wxminpname}    Run Keyword If    '${wxminpname1}'!='wallet'    set variable    ${wxminpname1}
    ...    ELSE    Set variable    corpcrew
    ${appid}    set variable    ${${wxminpname}appid}
    ${sid}    set variable    ${${wxminpname}sid}
    #${appkey}    set variable    ${${wxminpname}appkey}
    ${appkey}    set variable    ${mappkey}
    ${timestamp}    GetServertime    ${login_URL}
    ${timestamp1}=    set variable    ${timestamp}000
    ${timestamp1}=    Replace String    ${timestamp1}    "    ${EMPTY}
    #当需要传uid时，则uid从map中取，否则uid为0
    ${mapskey}    Get Dictionary Keys    ${maps}
    ${k}    Get Count    ${mapskey}    uid
    ${uid}    Run Keyword If    ${k}==1    Get From Dictionary    ${maps}    uid
    ...    ELSE    set variable    0
    ${heards_dict}=    create dictionary
    log    sid ===${sid}
    log    heards_dict ===${heards_dict}
    ${URL}=    set variable    ${Base_URL}
    ${post_dict}=    create dictionary    &{maps}
    #公共参数timestamp、appid、sid
    set to dictionary    ${post_dict}    timestamp=${timestamp1}
    set to dictionary    ${post_dict}    appid=${appid}
    set to dictionary    ${post_dict}    sid=${sid}
    #签名
    ${signkey}=    Run Keyword If    ${uid}==0    set variable    ${appid}${timestamp1}${sid}${appkey}
    ...    ELSE    set variable    ${appid}${timestamp1}${sid}${uid}${appkey}
    ${signkey}=    Replace String    ${signkey}    "    ${EMPTY}
    log    signkey=====${signkey}
    #排序及格式处理
    ${sign}=    encrypt    ${signkey}    md5    32
    log    使用万能签名${mapp_sgin}
	${wxenv}    Env_URL    ${Base_URL} 
	${mapp_sgin}   Run Keyword IF   '${wxenv}'=='Test'  Set Variable  ${mapp_sginTest}
	...		ELSE IF  '${wxenv}'=='Online'   Set Variable  ${mapp_sginOnline}
	...		ELSE    Set Variable  ${mapp_sginBeta}
    ${sign}=    Set Variable    ${mapp_sgin}
    #请求头处理
    set to dictionary    ${heards_dict}    sign=${sign}
    set to dictionary    ${heards_dict}    Content-Type=${ContentType}
    set to dictionary    ${heards_dict}    User-Agent=${UserAgent}
    log    sign====${sign}
    log    post_dict======${post_dict}
    log    参数编码前：${post_dict}
    ${post_dict}    Evaluate    urllib.parse.urlencode(${post_dict})    urllib
    log    参数编码后：${post_dict}
    Create Session    run    ${URL}    headers=${heards_dict}
    ${resp}=    Get Request    run    uri=${path}    params=${post_dict}
    log    thejoyrun_get_wxminp End ...
    [Return]    ${resp}

thejoyrun_getp
    [Arguments]    ${path}    ${maps}    ${userName}    ${Base_URL}    ${pwds}=None    ${Retry}=None
    [Documentation]    *用于APP内需要登录和签名的Get场景：joyrun中get请求url方式关键字*
    ...    ${userName}  中传uid/sid 模式时用的是sid访问，${pwds}不启作用
	...    ${pwds}  中传None时，密码为使用默认密码67889911
	...    ${Retry}  中传None时，默认重试3次，否则为传的次数；
    ...    参数以params方法提交出现Url中，也在body带公共参数（signature、timestamp）；
    [Timeout]    30 seconds
    log    thejoyrun_getp Start ......
    ${Retry}    Run Keyword If    '${Retry}'=='None'    set variable    ${RetryInti}
    ...    ELSE    set variable    ${Retry}
    ${pwd}    Run Keyword If    '${pwds}'=='None'    set variable    ${pwd}
    ...    ELSE    set variable    ${pwds}
    ${env}    Env_URL    ${Base_URL}
    ${userslist}    Get Dictionary Keys    ${usersinfo_dict}
    ${user_is}    Get Count    ${userslist}    ${env}${userName}
	###处理直接输入sid的情况
	${sid_and_uid}   Get Lines Matching Pattern    ${userName}    */*
	${sid_uidlist}    Run Keyword If  '${sid_and_uid}'!='${EMPTY}'   split string   ${userName}   /
	${sid_input}   Run Keyword If  '${sid_and_uid}'!='${EMPTY}'   Get From List  ${sid_uidlist}   -1
	${uid_input}   Run Keyword If  '${sid_and_uid}'!='${EMPTY}'   Get From List  ${sid_uidlist}   0
	${ypcookie_input}   Run Keyword If  '${sid_and_uid}'!='${EMPTY}'  set variable  uid=${uid_input}\&sid=${sid_input}
	${uid_sid_input}   Run Keyword If  '${sid_and_uid}'!='${EMPTY}'  create dictionary   uid=${uid_input}   sid=${sid_input}   ypcookie=${ypcookie_input}
    ${heards}    Run Keyword If    ${user_is}<=0 and '${sid_and_uid}'=='${EMPTY}'  joyrun_POST_heardsession    ${userName}    ${pwd}    ${Base_URL}
	...    ELSE IF   ${user_is}<=0 and '${sid_and_uid}'!='${EMPTY}'   set variable      ${uid_sid_input}
    ...    ELSE    Get From Dictionary    ${usersinfo_dict}    ${env}${userName}
    #从字典里取出相应key的值
    ${uid}=    Get From Dictionary    ${heards}    uid
    ${sid}=    Get From Dictionary    ${heards}    sid
    ${timestamp}    GetServertime    ${login_URL}
    ${ypcookie}=    Get From Dictionary    ${heards}    ypcookie
    ${heards_dict}=    create dictionary    ypcookie=${ypcookie}
    ##将ypcookie转为url编码
    ${ypcookie1}=    urlencode    ${ypcookie}
    ${cookies}=    create dictionary
    set to dictionary    ${cookies}    ypcookie=${ypcookie1}
    set to dictionary    ${cookies}    app_version=${appversion}
    #log    uid ===${uid}
    #log    sid ===${sid}
    log    heards_dict ===${heards_dict}
    ${URL}=    set variable    ${Base_URL}
    ${sign_dict}=    create dictionary    timestamp=${timestamp}
    ${post_dict}=    create dictionary    timestamp=${timestamp}
    @{mapstolist_sign}=    evaluate    sorted(${maps}.items())
    : FOR    ${map}    IN    @{mapstolist_sign}
    \    set to dictionary    ${sign_dict}    ${map[0]}=${map[1]}
    @{mapstolist}=    evaluate    sorted(${maps}.items())
    : FOR    ${map}    IN    @{mapstolist}
    \    set to dictionary    ${post_dict}    ${map[0]}=${map[1]}
    #排序及格式处理
    ${sign_dict_tolist}=    evaluate    sorted(${sign_dict}.items())

    # ${buchongfu123}         Evaluate    type(${sign_dict_tolist})
    # log                     -------${buchongfu123}------
    # ${signparam}=    convert to string    ${sign_dict_tolist}
    # ${signparam}=    Replace String    ${signparam}    [    ${EMPTY}
    # ${signparam}=    Replace String    ${signparam}    u'    '
    # ${signparam}=    Replace String    ${signparam}    ', '    ${EMPTY}
    # ${signparam}=    Replace String    ${signparam}    ('    ${EMPTY}
    # ${signparam}=    Replace String    ${signparam}    ')    ${EMPTY}
    # ${signparam}=    Replace String    ${signparam}    ,${SPACE}    ${EMPTY}
    # ${signparam}=    Replace String    ${signparam}    ]    ${EMPTY}
    #${signparam}=    Replace String    ${signparam}    &    ${EMPTY}
    # ${signparam}=    Evaluate    '${signparam}'.decode('unicode_escape')    #对中文做处理，将unicode字符解码成对应的中文字符
    #log    ${signparam}
    ${len}=    evaluate    len(${sign_dict_tolist})
    ${signparam} =    set variable    ${EMPTY}
    : FOR    ${index}    IN RANGE    0    ${len}
    \    ${signparamkey}    set variable    ${sign_dict_tolist[${index}][0]}
    \    ${signparamValue}    set variable    ${sign_dict_tolist[${index}][1]}
    \    ${signparamsting}    set variable    ${signparamkey}${signparamValue}
    \    ${signparam} =    set variable    ${signparam}${signparamsting}
    log    signparam=======${signparam}
    #排序及格式处理
    log    signparam===${signparam}
    ${signkey1}=    set variable    ${signparam}${appkey1}${uid}${sid}
    ${signkey2}=    set variable    ${signparam}${appkey2}${uid}${sid}
    #${signkey1}=    Replace String    ${signkey1}    "    ${EMPTY}
    #${signkey2}=    Replace String    ${signkey2}    "    ${EMPTY}
    #log    signkey1=====${signkey1}
    #log    signkey2=====${signkey2}
    #排序及格式处理
    ${sign1}=    encrypt    ${signkey1}    md5    32
    ${sign2}=    encrypt    ${signkey2}    md5    32
    log    运行环境是:${Base_URL}
    #通用签名
    ${method_env}    Env_URL   ${Base_URL}
	log    运行环境是${method_env}:${Base_URL}
	${sign1}   Run Keyword IF    '${method_env}'=='Test'   Set Variable    ${signTest} 
	...		ELSE IF   '${method_env}'=='Online'   Set Variable    ${signOnline} 
	...		ELSE   Set Variable    ${signBeta}
	${_sign} =    Convert To Uppercase    ${sign1}
    log    通用签名:${_sign}
    ${signature} =    Convert To Uppercase    ${sign2}
    log    业务签名：${signature}
    #处理设备ID
	${APPDEVINFO}   Replace String    ${APPDEVINFO}    DeveiceId    AutoTest_Joyrun_${username}
	${APPDEVINFO}	Replace String    ${APPDEVINFO}    UserID    ${uid}
    set to dictionary    ${heards_dict}    _sign=${_sign}
    set to dictionary    ${heards_dict}    APPVERSION=${APPVERSION}
    set to dictionary    ${heards_dict}    Content-Type=${ContentType}
    set to dictionary    ${heards_dict}    User-Agent=${UserAgent}
    set to dictionary    ${heards_dict}    APP_DEV_INFO=${APPDEVINFO}
    set to dictionary    ${heards_dict}    SYSVERSION=${SYSVERSION}
    set to dictionary    ${heards_dict}    MODELTYPE=${MODELTYPE}
    #log    _sign====${_sign}
    #log    signature====${signature}
    set to dictionary    ${post_dict}    signature=${signature}
    log    参数编码前：${post_dict}
    ${post_param}    Evaluate    urllib.parse.urlencode(${post_dict})    urllib
    log    参数编码后：${post_param}
    Create Session    run    ${URL}    headers=${heards_dict}    cookies=${cookies}
    ${resp}=    Get Request    run    uri=${path}    params=${post_param}
    ${Temporary}     To Str       ${resp.content}
    # ${get_count}    Get Count    ${resp.content}    ret\":"401"
    ${get_count}    Get Count    ${Temporary}    ret\":"401"
    Run Keyword If    ${get_count}==1    log    ${userName}的SID过期而登录失败
    Run Keyword If    ${get_count}==1    Pop From Dictionary    ${usersinfo_dict}    ${env}${userName}
    ${Retry}    Run Keyword If    ${get_count}==1    Evaluate    ${Retry}-1
    ...    ELSE    Set Variable    ${-1}
    ${resp}    Run Keyword If    ${get_count}==1 and ${Retry}>=0    thejoyrun_getp    ${path}    ${maps}    ${userName}
    ...    ${Base_URL}    ${pwds}    ${Retry}
    ...    ELSE    set variable    ${resp}
    Run Keyword If    ${get_count} == 0    Return From Keyword    ${resp}
    log    thejoyrun_getp End ...
    [Return]    ${resp}

thejoyrun_get_nosign
    [Arguments]    ${path}    ${maps}    ${userName}    ${Base_URL}    ${pwds}=None    ${Retry}=None
    [Documentation]    *用于非APP请求不需要签名Get场景：joyrun中get请求url方式参数的关键字*
    ...
    ...    参数以params方法提交，出现Url中，也在body中，但不需要签名没有公共参数；
    [Timeout]    30 seconds
    log    thejoyrun_get_nosign Start ......
    ${Retry}    Run Keyword If    '${Retry}'=='None'    set variable    ${RetryInti}
    ...    ELSE    set variable    ${Retry}
    ${pwd}    Run Keyword If    '${pwds}'=='None'    set variable    ${pwd}
    ...    ELSE    set variable    ${pwds}
    ${env}    Env_URL    ${Base_URL}
    ${userslist}    Get Dictionary Keys    ${usersinfo_dict}
    ${user_is}    Get Count    ${userslist}    ${env}${userName}
    ${heards}    Run Keyword If    ${user_is}<=0    joyrun_POST_heardsession    ${userName}    ${pwd}    ${Base_URL}
    ...    ELSE    Get From Dictionary    ${usersinfo_dict}    ${env}${userName}
    #从字典里取出相应key的值
    ${uid}=    Get From Dictionary    ${heards}    uid
    ${sid}=    Get From Dictionary    ${heards}    sid
    ${timestamp}    GetServertime    ${login_URL}
    ${ypcookie}=    Get From Dictionary    ${heards}    ypcookie
    ${heards_dict}=    create dictionary    ypcookie=${ypcookie}
    ##将ypcookie转为url编码
    ${ypcookie1}=    urlencode    ${ypcookie}
    ${cookies}=    create dictionary
    set to dictionary    ${cookies}    ypcookie=${ypcookie1}
    set to dictionary    ${cookies}    app_version=${appversion}
    #log    uid ===${uid}
    #log    sid ===${sid}
    #log    heards_dict ===${heards_dict}
    ${URL}=    set variable    ${Base_URL}
    ${post_dict}=    create dictionary
    @{mapstolist}=    evaluate    sorted(${maps}.items())
    : FOR    ${map}    IN    @{mapstolist}
    \    set to dictionary    ${post_dict}    ${map[0]}=${map[1]}
    #处理设备ID
	${APPDEVINFO}   Replace String    ${APPDEVINFO}    DeveiceId    AutoTest_Joyrun_${username}
	${APPDEVINFO}	Replace String    ${APPDEVINFO}    UserID    ${uid}
    #排序及格式处理
    set to dictionary    ${heards_dict}    APPVERSION=${APPVERSION}
    set to dictionary    ${heards_dict}    Content-Type=${ContentType}
    set to dictionary    ${heards_dict}    User-Agent=${UserAgent}
    set to dictionary    ${heards_dict}    APP_DEV_INFO=${APPDEVINFO}
    set to dictionary    ${heards_dict}    SYSVERSION=${SYSVERSION}
    set to dictionary    ${heards_dict}    MODELTYPE=${MODELTYPE}
    log    参数编码前：${post_dict}
    ${post_param}    Evaluate    urllib.parse.urlencode(${post_dict})    urllib
    log    参数编码后：${post_param}
    Create Session    run    ${URL}    headers=${heards_dict}    cookies=${cookies}
    ${resp}=    Get Request    run    uri=${path}    params=${post_param}
    ${Temporary}     To Str       ${resp.content}
    ${get_count}    Get Count    ${Temporary}    ret\":"401"
    Run Keyword If    ${get_count}==1    log    ${userName}的SID过期而登录失败
    Run Keyword If    ${get_count}==1    Pop From Dictionary    ${usersinfo_dict}    ${env}${userName}
    ${Retry}    Run Keyword If    ${get_count}==1    Evaluate    ${Retry}-1
    ...    ELSE    Set Variable    ${-1}
    ${resp}    Run Keyword If    ${get_count}==1 and ${Retry}>=0    thejoyrun_get_nosign    ${path}    ${maps}    ${userName}
    ...    ${Base_URL}    ${pwds}    ${Retry}
    ...    ELSE    set variable    ${resp}
    Return From Keyword If    ${get_count}==0    ${resp}
    log    thejoyrun_get_nosign End ...
    [Return]    ${resp}

thejoyrun_postjson
    [Arguments]    ${path}    ${maps}    ${Base_URL}    ${uid}=None
    [Documentation]    *dubbo api 场景：joyrun dubbo api中post请求json方式关键字*
    ...    参数以json格式提交数据；
    [Timeout]    30 seconds
    log    thejoyrun_postjson Start ......
    ${ContentType}    Set Variable    application/json;charset=UTF-8
    ${heards_dict}=    create dictionary
    log    heards_dict ===${heards_dict}
    ${URL}=    set variable    ${Base_URL}
    ${post_dict}=    create dictionary    &{maps}
    log    post_dict：${post_dict}
    #请求头处理${UserAgent}
    set to dictionary    ${heards_dict}    Content-Type=${ContentType}
    set to dictionary    ${heards_dict}    User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X)
    Create Session    runwx    ${URL}    headers=${heards_dict}
    ${resp}=    Post Request    runwx    uri=${path}    data=${post_dict}
    log    thejoyrun_postjson End ......
    [Return]    ${resp}


GetServertime
    [Arguments]    ${login_URL}
    [Documentation]    获取服务端的时间
    log    GetServertime Start ......
    ${time}=    Get Time    epoch
    log    time= ${time}
    ${isend}    evaluate    int(${time})-${Goltimestamp}-280
    Run Keyword If    ${isend}>=0    Create Session    timestamp    ${login_URL}
    ${resptime}    Run Keyword If    ${isend}>=0    RequestsLibrary.Get Request    timestamp    /GetTimestamp.aspx
    ${contentime}    Run Keyword If    ${isend}>=0    charconver    ${resptime.content}
    # Run Keyword If    ${isend}>=0      # # log json    ${resptime.content}

    # ${abc}     get json value    ${contentime}    /lasttime
    # ${timestamp}    Run Keyword If    ${isend}>=0    set variable    ${abc}

    ${timestamp}    Run Keyword If    ${isend}>=0    get json value    ${contentime}    /lasttime
    ...    ELSE    set variable    ${Goltimestamp}
    set global variable    ${Goltimestamp}    ${timestamp}
    log    GetServertime End ......
    [Return]    ${timestamp}

Env_URL
    [Arguments]    ${InputURL}
    [Documentation]    根据URL判断运行环境
    log    Env_URL Start ......
    ${Testcount}    Get Lines Matching Pattern    ${InputURL}    *-test*
    ${env_out}    Run Keyword If    '${Testcount}'=='${EMPTY}'    set variable    Online
    ...    ELSE    set variable    Test
    log    Env_URL End ......
    [Return]    ${env_out}