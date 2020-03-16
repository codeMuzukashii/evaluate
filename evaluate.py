# coding=utf-8
import re
import sys


def check_expression(string):
    result = True
    if not string.count("(") == string.count(")"):
        result = False
    if re.findall('[a-pr-z]+', string.lower()):
        result = False
    return result


def check_extra_balnk(string):
    s_list = string.split(' ')
    s_list_len = len(s_list)
    for i in xrange(s_list_len):
        if i != s_list_len - 1:
            if s_list[i].isdigit() is True:
                if s_list[i+1] not in ('+', '-', '*', '/', ')'):
                    print('Invalid expression!')
                    return False
            else:
                if s_list[i+1].isdigit() is False and s_list != '(':
                    print('Invalid expression!')
                    return False
    return True


def add_and_sub(string):
    string = string.replace(" ", "")
    add_reg = r'[\-]?\d+\d*\+[\-]?\d+\d*'
    sub_reg = r'[\-]?\d+\d*\-[\-]?\d+\d*'

    while re.findall(add_reg, string):
        add_list = re.findall(add_reg, string)
        for add_stars in add_list:
            num_1, num_2 = add_stars.split('+')
            add_result = str(int(num_1.strip()) + int(num_2.strip()))
            string = string.replace(add_stars, add_result)
    while re.findall(sub_reg, string):
        sub_list = re.findall(sub_reg, string)
        for sub_stars in sub_list:
            num_1, num_2 = sub_stars.split('-')
            sub_result = str(int(num_1.strip()) - int(num_2.strip()))
            string = string.replace(sub_stars, sub_result)
    return string


def multi_and_divi(string):
    string = string.replace(" ", "")
    regular = r'[\-]?\d+\.?\d*[*/][\-]?\d+\.?\d*'

    while re.findall(regular, string):
        expression = re.search(regular, string).group()

        if expression.count('*') == 1:
            num_1, num_2 = expression.split('*')
            mul_result = str(int(num_1) * int(num_2))
            string = string.replace(expression, mul_result)

        if expression.count('/') == 1:
            num_1, num_2 = expression.split('/')
            div_result = str(int(num_1) / int(num_2))
            string = string.replace(expression, div_result)
    return string


if __name__ == '__main__':
    source = sys.argv[1]
    if check_expression(source):
        if source.count("(") > 0:
            stars = re.search(r'\([^()]*\)', source).group()[1:-1]
            if check_extra_balnk(stars):
                replace_stars = multi_and_divi(stars)
                replace_stars = add_and_sub(replace_stars)
                source = source.replace(stars, replace_stars)
                source = source.replace('(', '').replace(')', '')
                if check_extra_balnk(source):
                    replace_stars = multi_and_divi(source)
                    replace_stars = add_and_sub(replace_stars)
                    source = source.replace(source, replace_stars)
                    print(source)

        else:
            if check_extra_balnk(source):
                replace_stars = multi_and_divi(source)
                replace_stars = add_and_sub(replace_stars)
                source = source.replace(source, replace_stars)
                print(source)
    else:
		print('Invalid expression!')