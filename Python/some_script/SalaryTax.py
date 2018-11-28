import sys
import os
import re


def TaxRate(salary: float, total: float = None) -> float:
    '''Calculate the tax according to the corresponding tax rate.

    ``salary`` is the total salary before pay taxes. Required parameters.  
    ``total`` is the sum of bonus and salary. The default is ``None``.  
    ``return`` is 'tax'.
    '''

    if total == None:
        total = salary

    if salary <= 1500:
        tax = total * 0.03
    elif salary > 1500 and salary <= 4500:
        tax = total * 0.1 - 105
    elif salary > 4500 and salary <= 9000:
        tax = total * 0.2 - 555
    elif salary > 9000 and salary <= 35000:
        tax = total * 0.25 - 1005
    elif salary > 35000 and salary <= 55000:
        tax = total * 0.3 - 2755
    elif salary > 55000 and salary <= 80000:
        tax = total * 0.35 - 5505
    elif salary > 80000:
        tax = total * 0.45 - 13505
    return tax


def TaxSalary(salary: float, fund_level: float = 5,
              bonus: float = None) -> float:
    '''Reducing Social Insurace, Threshold and get tax.

    Reducing Social Insurace and Personal income tax threshold.  
    Invoking the function of ``TaxRate()``, and get parameber of ``tax``  
    ``salary`` is the total salary before paying taxes. Required parameters.  
    ``fund_level`` is the level of paying Accumulation Fund. The default is ``5``.  
    ``bonus`` is total bonus before paying taxes. The default is ``None``. 
    '''

    # 起征点
    threshold = 3500
    # 五险一金
    socialInsurance_fund = SocialInsurance(salary, fund_level)
    salary_after_fund = salary - socialInsurance_fund

    # 判断是否有奖金
    if bonus == None:
        # 无奖金时, 月工资小于起征点则应缴税为0
        if salary >= threshold:
            salary_tax = TaxRate(salary_after_fund - threshold)
            print('Salary tax payable is : %.2f' % salary_tax)
            return salary_tax, socialInsurance_fund
        else:
            return 0, socialInsurance_fund

    elif bonus != None:
        # 有奖金并且 缴五险一金后月工资大于起征点
        if salary >= threshold:
            salary_tax = TaxRate(salary_after_fund - threshold)
            bonus_tax = TaxRate(bonus / 12, bonus)
            print('Salary tax payable is: %.2f \nBonus tax payable is: %.2f' %
                  (salary_tax, bonus_tax))
            return salary_tax + bonus_tax, socialInsurance_fund

        # 有奖金并且 缴五险一金后月工资小于起征点
        elif salary < threshold and salary > 0:
            salary_tax = 0
            bonus_needed = bonus + salary - threshold
            bonus_tax = TaxRate(bonus_needed / 12, bonus_needed)
            print('Salary is below the threshold.Bonus tax payable is : %.2f' %
                  bonus_tax)
            return bonus_tax, socialInsurance_fund
    else:
        print('error')


def SocialInsurance(salary: float, fund_level: float = 5) -> float:
    '''

    ``salary`` is total salary before paying taxes. Required parameters.  
    ``fund_level` is the level of paying Accmulation Fund. The default is ``5``.   
    If ``fund_level`` is ``0``, performing normal standards of Accmulation Fund.  
    If ``fund_level`` is ``x``, performing minimum standards of Accmulation, 
    and according ``x%``.（ ``x`` only can be 5,8,10,12）；
    '''
    # 公积金缴纳等级不合法
    if fund_level not in [0, 5, 8, 10, 12]:
        print('Please input right Fund Level! Such as 5,8,10,12.')
        # exit(1)
        # os._exit(1)
        sys.exit(0)

    # 公积金最低额度为2100
    accumulation_fund_base = 2100

    # rate_staff
    endowment_insurance_staff = 0.08
    medical_insurance_staff = 0.02
    unemployment_insurance_staff = 0.002

    # # rate_company
    # endowment_insurance_company = 0.14
    # medical_insurance_company = 0.07
    # unemployment_insurance_company = 0.64
    # maternity_insurance_company = 0.0085
    # medical_assistance = 0.0026
    # employment_injury_insurance = 0.002

    # insurance_base for 2018
    endowment_insurance_base = 3469
    medical_insurance_base = 4931
    unemployment_insurance_base = 2100
    maternity_insurance_base = 4931
    medical_assistance_base = 8218
    employment_injury_insurance_base = 2100

    # 个人应缴五险（暂时按广州市2018年最低标准）
    endowment_insurance = endowment_insurance_base * endowment_insurance_staff
    medical_insurance = medical_insurance_base * medical_insurance_staff
    unemployment_insurance = unemployment_insurance_base * unemployment_insurance_staff
    social_insurance = endowment_insurance + medical_insurance + unemployment_insurance

    # 公积金计算（暂时按广州市2018年最低标准）
    if fund_level == 0:
        return 105 + social_insurance  # 当level=0时，使用正常五险一金流程，待增加
    elif fund_level == 5:
        accumulation_fund = accumulation_fund_base * fund_level / 100
    elif fund_level == 8:
        accumulation_fund = accumulation_fund_base * fund_level / 100
    elif fund_level == 10:
        accumulation_fund = accumulation_fund_base * fund_level / 100
    elif fund_level == 12:
        accumulation_fund = accumulation_fund_base * fund_level / 100

    print(
        'The Accumulation Fund payable is: %.2f \nThe Social Insurance payable is: %.2f'
        % (accumulation_fund, social_insurance))
    return (accumulation_fund + social_insurance)


def SalaryAfterTax(salary: float = None, level: float = 5,
                   bonus: float = None) -> float:
    '''Calculate after tax wages(including Social Insurance)

    If ``salary`` is ``None`` and ``bonus`` isn't ``None``, invoking the 
    function of ``TaxRate()`` and directly calculation of bonus tax rate.  
    Else taxes on bonus and salary will be calculated.  
    ``salary`` is the total salary before paying taxes. The default is ``None``.
    ``level`` is the level of paying Accmulation Fund. The default is ``5``.
    ``bonus`` is total bonus before paying taxes. The default is ``None``.
    '''

    if level == None:
        level = 5

    # 只计算奖金缴税的情况，则无需考虑起征点、五险一金等
    if salary == None and bonus != None:
        bonus_tax = TaxRate(bonus / 12, bonus)
        print('Bonus after tax is : %.2f' % (bonus - bonus_tax))
        return

    # 应缴税、五险一金
    elif salary != None and bonus != None:
        # 有奖金时，一并处理
        tax, socialInsurance_fund = TaxSalary(salary, level, bonus)

        # 扣除五险一金、税后
        total = salary + bonus - tax - socialInsurance_fund
        print('Salary and bonus after tax is : %.2f' % total)
        return
    elif salary != None and bonus == None:
        # 无奖金、只计算月工资
        tax, socialInsurance_fund = TaxSalary(salary, level)

        # 扣除五险一金、税后
        salary_after_SocialInsurance = salary - socialInsurance_fund
        salary_after_tax = salary_after_SocialInsurance - tax
        print('Salary after tax is : %.2f' % salary_after_tax)
        return
    else:
        print('Please input legally!')
        return


def is_number(number: 'any type') -> bool:
    '''判断float类型数字'''

    if number == '':
        return None
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(number)
    if result:
        return True
    else:
        return False


def judge_number(number):
    if number == '':
        return None
    elif is_number(number):
        return eval(number)
    else:
        print('Please input right Number!')
        sys.exit()


def verify_input(input_type: str):
    '''Get input according to ``input_type``
    
    ``input_type`` is 'income before tax' OR 'take-home pay'
    '''

    if input_type is 'income before tax':
        # 税前工资
        salary_before_tax = judge_number(
            input('Please input your Salary before tax:'))

        # 得到公积金等级
        fund_level = judge_number(
            input("Please input your Accumulation Fund Level:"))

        # 得到奖金
        bonus_before_tax = judge_number(
            input("Please input your your Bonus before tax:"))

    elif input_type is 'take-home pay':
        # 税后工资
        salary_after_tax = judge_number(
            input('Please input your Salary before tax:'))

        # 得到公积金等级
        fund_level = judge_number(
            input("Please input your Accumulation Fund Level:"))

        # 得到奖金
        bonus_after_tax = judge_number(
            input("Please input your your Bonus before tax:"))

    SalaryAfterTax(
        salary=salary_before_tax, level=fund_level, bonus=bonus_before_tax)


if __name__ == '__main__':
    # 税前工资
    salary_before_tax = judge_number(
        input('Please input your Salary before tax:'))

    # 得到公积金等级
    fund_level = judge_number(
        input("Please input your Accumulation Fund Level:"))

    # 得到奖金
    bonus_before_tax = judge_number(
        input("Please input your your Bonus before tax:"))

    SalaryAfterTax(
        salary=salary_before_tax, level=fund_level, bonus=bonus_before_tax)
'''
import inspect
def get_variable_name(variable):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is variable]

def delete_list(parameber):
    if parameber == '':
        return False
    else:
        return True
def filter_dict(data):
    return {k: v for k, v in data.items() if v != ''}
    # 判断是否为空
    needed_list = list(
        filter(delete_list, [salary_before_tax, fund_level, bonus_before_tax]))
    needed_dict = {
        'salary_before_tax': salary_before_tax,
        'fund_level': fund_level,
        'bonus_before_tax': bonus_before_tax
    }
    new_dict=filter_dict(needed_dict)
    # new_dict = dict(filter(filter_dict, needed_dict))

    for key in new_dict:
        if is_number(new_dict(key))==False:
            print('Please input right Number!')

    # index = new_dict.__len__()
    # if i<index:
    salary=needed_dict.keys(0)
    SalaryAfterTax(salary=needed_dict.values)

    for index in range(len(needed_list)):
        print(index)
        boolvalue = is_number(needed_list[index])
        if boolvalue == False:
            print('Please input right Number!')

    a = str(get_variable_name(needed_list[1])) + '==' + needed_list[1]
    a = a.replace('[', '').replace(']', '').replace("'", '')
    '''