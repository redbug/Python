'''
Created on Mar 29, 2011

@author: redbug
'''
import re

st = r'test1234 "http://www.google.com.tw (abc) http://redbug.twbbs.org eee'

http_url_re = r'(?#Protocol)(?:(?:ht|f)tp(?:s?)\:\/\/|~\/|\/)?(?#Username:Password)(?:\w+:\w+@)?(?#Subdomains)(?:(?:[-\w]+\.)+(?#TopLevel Domains)(?:com|org|net|gov|mil|biz|info|mobi|name|aero|jobs|museum|travel|[a-z]{2}))(?#Port)(?::[\d]{1,5})?(?#Directories)(?:(?:(?:\/(?:[-\w~!$+|.,=]|%[a-f\d]{2})+)+|\/)+|\?|#)?(?#Query)(?:(?:\?(?:[-\w~!$+|.,*:]|%[a-f\d{2}])+=?(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)(?:&(?:[-\w~!$+|.,*:]|%[a-f\d{2}])+=?(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)*)*(?#Anchor)(?:#(?:[-\w~!$+|.,*:=]|%[a-f\d]{2})*)?'
#rule = re.compile( http_url_re )

highlight = r'(\s\([\w\s]+\))?'
#a-zA-Z0-9_ \'
http_url_re += highlight
rule = re.compile(http_url_re)


def decorator(matchObj):
    result = "<a href='" + matchObj.group(0) + "'>" + matchObj.group(0) + "</a>"
    return result

def decorator_hightlight(matchObj):
    
    print matchObj.group(0)
    
    tokens = matchObj.group(0).split(' ')
    
    if len(tokens) == 1:
        target = tokens[0]
    else:
        target = tokens[1].strip('()') 
               
#    print matchObj.group(0)
    return "<a href='" + tokens[0] + "'>" + target + "</a>"
#print rule.sub( decorator, st )

print rule.sub( decorator_hightlight, st)
