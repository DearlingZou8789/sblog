#!/usr/bin/python
#coding=utf-8
from django import template
import datetime
import re
from sblog1.models import Author,Book

register=template.Library()

@register.filter
def cut(value,arg):
    return value.replace(arg,'')

@register.filter
def lower(value):
    return value.lower()


@register.tag #主要还是Library再起作用,其中filter过滤value|cut ,tag就是标签{% %}
def do_current_time(parser,token):
    try:
        #split_contents() konws not to split quoted strings.
        tag_name,format_string=token.split_contents()
    except ValueError:
        msg='%r tag requires a single argument' % token.contents[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode2(format_string[1:-1])

class CurrentTimeNode(template.Node):#do_current_time要返回的对象,register.tag需要调用该对象的render方法
    def __init__(self,format_string):
        self.format_string=format_string
    
    def render(self,context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)

class CurrentTimeNode2(template.Node):#do_current_time要返回的对象,register.tag需要调用该对象的render方法
    def __init__(self,format_string):
        self.format_string=format_string
    
    def render(self,context):
        now = datetime.datetime.now()
        context['current_time']=now.strftime(self.format_string)
        return ''

@register.tag #主要还是Library再起作用,其中filter过滤value|cut ,tag就是标签{% %}
def do_current_time2(parser,token):
    try:
        #split_contents() konws not to split quoted strings.
        tag_name,arg=token.contents.split(None,1)
    except ValueError:
        msg='%r tag requires argument' % token.contents[0]
        raise template.TemplateSyntaxError(msg)
    m=re.search(r'(.*?) as (\w+)',arg)
    if m:
        fmt,var_name=m.groups()
    else:
        msg='%r tag had invalid arguments' % tag_name
        raise template.TemplateSyntaxError(msg)
    if not (fmt[0]==fmt[-1] and fmt[0] in ("'",'"')):
        msg="%r tag's argument should be in quotes" % tag_name
        raise template.TemplateSyntaxtError(msg)

    return CurrentTimeNode3(fmt[1:-1],var_name)

class CurrentTimeNode3(template.Node):#do_current_time要返回的对象,register.tag需要调用该对象的render方法
   
    def __init__(self,format_string,var_name):
        self.format_string=format_string
        self.var_name=var_name
    
    def render(self,context):
        now = datetime.datetime.now()
        context[self.var_name]=now.strftime(self.format_string)
        return ''

@register.tag
def upper(parser,token):
    nodelist=parser.parse(('endupper',))
    parser.delete_first_token()
    return UpperNode(nodelist)

class UpperNode(template.Node): 
    def __init__(self,nodelist):
        self.nodelist=nodelist

    def render(self,context):
        output=self.nodelist.render(context)
        return output.upper()

@register.inclusion_tag('books/show_books_for_author.html')
def show_books_for_author(author):
    books=Book.objects.filter(author_id=author.id)
    return {'books':books}
#in "datetimenow.html":{% show_books_for_author author %} 我有个疑问是关于show_books_for_author author中author的赋值问题,怎么赋值,怎么知道这个author有id属性呢! 
