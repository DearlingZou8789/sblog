#!/usr/bin/python
#coding=utf-8

from django.conf import settings
from django.template import TemplateDoesNotExist
import zipfile
def load_template_source(template_name,template_dirs=None):
    'Template loader that loads templates from a ZIP file.'
    #从settings.py配置文件中读取属性TEMPLATE_ZIP_FILES的值,默认返回空列表
    template_zipfiles=getattr(settings,"TEMPLATE_ZIP_FILES",[])
    #Try each ZIP fil in TEMPLATE_ZIP_FILES.
    for fname in template_zipfiles:
        try:
            z=zipfile.ZipFile(fname)
            source=z.read(template_name)
        except (IOError,KeyEroor):
            continue
        z.close()
        #找到一个可用的文件返回
        template_path="%s:%s" % (fname,template_name)
        return (source,template_path)

    #如果一个zip文件没找到,报错
    raise TemplateDoesNotExist(template_name)

load_template_source.is_usable=True
