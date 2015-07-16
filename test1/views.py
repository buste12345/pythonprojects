from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import DetailView
from test1.forms import CommentForm
from django.views.generic.detail import SingleObjectMixin 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from test1 import tasks
from test1.basicfunctions import returno, returnosp
class PostDetailView(DetailView):
    methods = ['get', 'post']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(object=self.object)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(object=self.object, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.object.get_absolute_url())

        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)
        
#def MainSiteView(resquest):
    #return HttpResponse("Hello, world. You're at the polls index.")
 #   render_to_response('AdmintLTE/index.html')
 
def my_view(request):
    #username = request.POST.get('username', False);
    #password = request.POST.get('password', False);
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print 'Returned1'
                return render_to_response('AdmintLTE/starter.html') 
            else:
                print 'Returned2'
                return HttpResponse("Error")
        else:
            print 'Returned3'
            return render_to_response('registration/login.html')
    else:
        print 'Returned4'
        return render_to_response('registration/login.html')
    

#def foo(request):
#    r = tasks.add.delay(2, 2)
#    return HttpResponse(r.task_id)

@login_required
def logged_in(request):
    return render_to_response('AdminLTE/starter.html',
        context_instance=RequestContext(request)
    )
    
@login_required
def entrypoint(request):
    return render_to_response('AdminLTE/subpagess/entryp.html',
    {'result': returno()},
    context_instance=RequestContext(request)
    )

@login_required
def entrypointdet(request,slug):
    return render_to_response('AdminLTE/subpagess/entrypdet.html',
    {'result': returnosp(slug)},
    context_instance=RequestContext(request)
    )    

@login_required
def test11(request):
    return HttpResponse('TEST LOGGED')
    
    