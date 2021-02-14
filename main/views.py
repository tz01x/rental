from django.shortcuts import render,get_object_or_404,redirect
from django.urls import  reverse
from django.http import HttpResponse,HttpResponseBadRequest

from .forms import PropertyForm,PropertyFormPart2,PropertyImgForm
from .models import Property
from imguploading.models import  Images
from django.views.generic import  CreateView,UpdateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test,login_required
from user.forms import MessageForm

# decorators
def checkPropertyPermission(callBackFunction):
    '''
    check an user has permission over a particular obj
    '''
    def innerFunction(request,slug):
        try:
            obj=Property.objects.get(slug=slug)
        except :
            return HttpResponseBadRequest()

        if request.user!=obj.user:
            return HttpResponseBadRequest()
        return callBackFunction(request,slug)
    return innerFunction

class  adPost(LoginRequiredMixin,CreateView):
    form_class=PropertyForm
    template_name="main/adpost.html"
    # queryset=Property.objects.all()
    def get_initial(self):
        # to initial the form
        init=super(adPost,self).get_initial()

        # initial the user to current user
        init['user']=self.request.user
        init['city']=self.request.user.profile.city
        init['contact_person']=self.request.user.profile.phone
        return init

    def form_valid(self,form):
        # print('in valid from')
        # print(form.cleaned_data)
        form.cleaned_data.pop('mymap')
        print(form.cleaned_data)

        return super().form_valid(form)

    def get_success_url(self):
        # this function get call when form save the data into db
        # which view we want to send it to user
        return reverse('main:createAndupdate_adpost_p2',kwargs={'slug':self.object.slug})
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
    
        context['submit_btn_value'] = "Create"
        context['progress_step']=1
        return context

class  PostUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    form_class=PropertyForm
    template_name='main/adpost.html'
    queryset=Property.objects.all()
    def form_valid(self,form):
        # print('in valid from')
        form.cleaned_data.pop('mymap')
        # print(form.cleaned_data)
        return super().form_valid(form)
    def get_success_url(self):
        # this function get call when form save the data into db
        # which view we want to send it to user
        return reverse('main:createAndupdate_adpost_p2',kwargs={'slug':self.object.slug})
    def test_func(self):

        instance=self.get_object()
        return instance.user==self.request.user
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['submit_btn_value'] = "Update"
        context['progress_step']=1
        context['is_updatable']=True
        context['myslug']=self.kwargs['slug']
        return context


@login_required
@checkPropertyPermission
def  adPostDelete(request,slug):
    '''
    delete property ad's
    '''
    if request.method=='POST':
        if request.POST.get('delete',None)=="true":
            try:
                slug=int(request.POST.get('slug',None))
                object=get_object_or_404(Property,slug=slug)
                object.delete()
                return HttpResponse('item been deleted')
            except :
                pass

    return HttpResponseBadRequest()

@login_required
@checkPropertyPermission
def adPostpart2(request,slug):
    '''
    create or update 2nd part of the AD post of property
    '''
    obj=get_object_or_404(Property,slug=slug)
    form=PropertyFormPart2(instance=obj,property_type_id=obj.property_types.id)
    if request.method=="POST":
        form=PropertyFormPart2(request.POST,instance=obj,property_type_id=obj.property_types.id)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            # return HttpResponse('well done')
            # return reverse('main:createAndupdate_adpost_images',kwargs={'slug':slug})
            return redirect('main:createAndupdate_adpost_images',slug=slug)
    ctx={
    'form':form,
    'submit_btn_value':"Update/Next",
    'progress_step':2,
    'is_updatable':True,
    'myslug':slug,
    }

    return render(request,'main/adpost.html',ctx)

@login_required
@checkPropertyPermission
def imageUpload(request,slug):
    obj=get_object_or_404(Property,slug=slug)
    form=PropertyImgForm()

    if request.method=='POST':
        form=PropertyImgForm(request.POST,request.FILES)
        files=request.FILES.getlist('images')#from field name 'Images'
        # print(files)
        if form.is_valid():
            # obj.youtube_link=form.cleaned_data['youtube_link']
            for file in files:
                imgobj=Images(baseimage=file)
                imgobj.save()
                obj.img.add(imgobj)
            obj.save()
            return redirect('main:createAndupdate_adpost_images',slug=(slug))

    return render(request,'main/adpostImgupload.html',{'form':form,'obj':obj,'progress_step':3,'is_updatable':True,'myslug':slug})




class  PropertyListView(ListView):
    model=Property


class PropertyDetailsView(DetailView):
    model=Property
    queryset=Property.objects.all()
    # template_name="main/property_detail.html"
    def get_context_data(self,*args,**kwargs):
        ctx=super(PropertyDetailsView,self).get_context_data(*args,**kwargs)
        ctx['msgform']=MessageForm(initial={"user":self.get_object().user})

        return ctx

def homeView(request):

    # print(dir(request))
    # request.get_full_path_info
    context={
        'property_list':Property.objects.all()
    }
    return render(request,"home.html",context=context)

def ContactView(request):
    return render(request,"contact.html")
