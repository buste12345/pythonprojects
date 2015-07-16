from djcelery import celery
from test1.models import celtest
from mongoengine import *

#@celery.task()
#def crawl_domain(urll):
#    from crawl import run_spider
#    return run_spider(urll)
    
@celery.task
def add(x, y):
    return x + y

@celery.task
def addcel():
    #connect('tintin')
    article = celtest(title = 'testingcel',text = 'XAXAXAXAXAXAXAXAXA')
    article.save()

@celery.task
def sleeptask(i):
    from time import sleep
    sleep(i)
    return i


@celery.task
def raisetask():
    raise KeyError("foo")
