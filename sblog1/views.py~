from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import datetime
from django.template import Context,Template
from django.template.loader import get_template
import MySQLdb
def current_time(request):
    now=datetime.datetime.now()
    t=get_template('datetime.html')
    html=t.render(Context({'current_date':now}))
    return HttpResponse(html)
# Create your views here.

def current_time2(request):
    current_date=datetime.datetime.now()
    return render_to_response('datetime.html',{'current_date':current_date})
#Create cureent_time2 in render_to_response

def hours_ahead(request,offset):
    hour_offset=int(offset)
    next_time=datetime.datetime.now()+datetime.timedelta(hours=hour_offset)
    #html="<html><body>In %s hour(s),it will be %s.</body></html>" % (offset,dt)
    return render_to_response('hours_ahead.html',locals())

def print_testmysql2(request):
    conn=MySQLdb.connect(user='root',passwd='tigerwith',db='testmysql',host='localhost')
    cur=conn.cursor()
    cur.execute('select * from testmysql2 order by id limit 0,100')
    table_testmysql2=[row for row in cur.fetchall()]
    conn.commit()
    conn.close()
    return render_to_response('print_testmysql2.html',{'table_testmysql2':table_testmysql2})


