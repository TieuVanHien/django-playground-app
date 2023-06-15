from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  allmembers = Member.objects.all().values()
  active_members = allmembers.filter(active=1)
  template = loader.get_template('members.html')
  context = {
    'members': allmembers,
    'activemembers': active_members
  }
  return HttpResponse(template.render(context, request))