from models import *

def templates(request):
    return {
        'templates': Template.objects.all()
    }