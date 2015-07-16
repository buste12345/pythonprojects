from test1.models import entry
from mongoengine import queryset

def returno():
    itemss = entry.objects.all()
    return itemss
    
def returnosp(slugg):
    itemss = entry.objects.get(slug=slugg)
    return itemss