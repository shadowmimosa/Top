## Convert python2 to python3  

### Need import `jsonpointer`  

### Please read Script changes in [README.MD](./Public/Lib/README.pdf)  

### Unified modification  

+ Replace `Library           HttpLibrary.HTTP` with `# Library           HttpLibrary.HTTP`  
+ Replace `Evaluate    reload(sys)    sys` with `# Evaluate    reload(sys)    sys`  
+ Replace `Evaluate    sys.setdefaultencoding( "UTF-8" )    sys` with `# Evaluate    sys.setdefaultencoding( "UTF-8" )    sys`  
+ Replace `iteritems()` with `items()`
+ Abandon library HttpLibrary, and Keyword `Get Json Value` use custom library  
+ Replace `urllib.urlencode()` with `urllib.parse.urlencode()`  
+ Replace `!=` with `!=`  
+ Add annotation to `log json`

### In thejoyrun.txt & http_request.txt & public_lib.txt

+ Add annotation for  
```robotframework
    Run Keyword If   ${login_ret}==0   # # log json  ${login_content}       
    ...    ELSE   log    哈哈，在登录就出错了！！！！！失败原因:${login_error}
```
+ Add line `${SrcListstr}    Evaluate          str(${SrcListstr})`
+ Replace `${field3Value}'=='null` with `${field3Value}'=='None`  
+ `null = None`   
+ Notes this line  
```python
${signparam}=    Evaluate    '${signparam}'.decode('unicode_escape')    #对中文做处理，将unicode字符解码成对应的中文字符
```
+ `Get Count` need a string at first parameter  
+ `Get Count` can use function `To Str` in the get_json_value.py  before use `${resp.content}`  
+ Replace `long()` whit `int()`, python3 don't has `long()`  
+ ~~Veriables need add `""` when veriable~~
+ Replace the `Quotation` in the FilterList of the thejoyrun  
+ Change the Function `arraytostring` in the thejoyrun  

+ Replace "700000" with "41006" in the Test Master 5 Min.Walletapi.Wallet Bind Post, on the Test Environment
+ Replace `${province1}>0` & `${city1}>0` with `${province1}!=''` & `${city1}!=''` in the Test Master 5 Min.Integrate.updata Run record.Class_01 and Test Master 5 Min.Integrate.updata Run record  

