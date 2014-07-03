# markup for blog post
# Step 1: look for tokens
# Step 2: create a dict of tokens with HTML tags
# Step 3: replace them all
# this will be done while displaying the raw text from the
# db
import re

mu_dict = {
    '{%img' : {'args' : 1, 'header': '<img src=', 'ender': '>'},
    '{%link' : {'args': 1, 'header': '<a href=', 'ender': '>'},
    '{%br' : {'args': 0, 'header': '<br', 'ender': '>'},
}


t_dict = {
    '{%img': '<img src=',
    '{%link': '<a href=',
}


def mu_tokens(markedup_text):
    reg = '({%[^%}]*%})'
    li = re.split(reg, markedup_text)
    tokens = [x for x in li if x[0:2] == '{%']
    return tokens


def token_dict(markedup_text):
    tokens = mu_tokens(markedup_text)
    r_dict = {}
    for t in tokens:
        try:
            li = t.split(' ')
            if len(li) > 2:
                args = li[1:len(li)-1]
            else:
                args = []

            key = t.split(' ')[0]
            tg = mu_dict[key]['header']
            # work on this
            r_dict[t] = tg + '"' + ' '.join(args[0:mu_dict[key]['args']]) + '"' +  mu_dict[key]['ender']
            # r_dict[t] = tg + '"' + t.split(' ')[1] + mu_dict[key]['ender']
        except KeyError:
            print "This tag is not recognized"

    return r_dict


def replace_tokens(markedup_text):
    d = token_dict(markedup_text)
    n = markedup_text
    for key, value in d.iteritems():
        n = re.sub(key, value, n)
    return n
