*** Settings ***
Resource    test.txt



*** Test Cases ***

test case1
    log    hello robot framework

test case2
    ${a}=   Set variable    python
    log    ${a}
    ${b}=   Set variable    it's variable
    