from django.shortcuts import render,get_object_or_404,redirect
from django.urls import  reverse
from django.http import HttpResponse,HttpResponseBadRequest

from .forms import PropertyForm,PropertyFormPart2,PropertyImgForm
from .models import Property
from imguploading.models import  Images
from django.views.generic import  CreateView,UpdateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test,login_required


# decorators
def checkPropertyPermission(callBackFunction):
    '''
    check an user has permission over a particular obj
    '''
    def innerFunction(request,pk):
        try:
            obj=Property.objects.get(id=pk)
        except :
            return HttpResponseBadRequest()

        if request.user!=obj.user:
            return HttpResponseBadRequest()
        return callBackFunction(request,pk)
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
        print('in valid from')
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        # this function get call when form save the data into db
        # which view we want to send it to user
        return reverse('main:createAndupdate_adpost_p2',kwargs={'pk':self.object.pk})
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['submit_btn_value'] = "Create"
        context['progress_step']=1
        return context

class  PostUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    form_class=PropertyForm
    template_name='main/adpost.html'
    queryset=Property.objects.all()
    def get_success_url(self):
        # this function get call when form save the data into db
        # which view we want to send it to user
        return reverse('main:createAndupdate_adpost_p2',kwargs={'pk':self.object.pk})
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
        context['mypk']=self.kwargs['pk']
        return context


@login_required
@checkPropertyPermission
def  adPostDelete(request,pk):
    '''
    delete property ad's
    '''
    if request.method=='POST':
        if request.POST.get('delete',None)=="true":
            try:
                pk=int(request.POST.get('pk',None))
                object=get_object_or_404(Property,pk=pk)
                object.delete()
                return HttpResponse('item been deleted')
            except :
                pass

    return HttpResponseBadRequest()

@login_required
@checkPropertyPermission
def adPostpart2(request,pk):
    '''
    create or update 2nd part of the AD post of property
    '''
    obj=get_object_or_404(Property,pk=int(pk))
    form=PropertyFormPart2(instance=obj,property_type_id=obj.property_types.id)
    if request.method=="POST":
        form=PropertyFormPart2(request.POST,instance=obj,property_type_id=obj.property_types.id)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            # return HttpResponse('well done')
            # return reverse('main:createAndupdate_adpost_images',kwargs={'pk':pk})
            return redirect('main:createAndupdate_adpost_images',pk=pk)
    ctx={
    'form':form,
    'submit_btn_value':"Update/Next",
    'progress_step':2,
    'is_updatable':True,
    'mypk':pk,
    }

    return render(request,'main/adpost.html',ctx)

@login_required
@checkPropertyPermission
def imageUpload(request,pk):
    obj=get_object_or_404(Property,pk=pk)
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
            return redirect('main:createAndupdate_adpost_images',pk=int(pk))

    return render(request,'main/adpostImgupload.html',{'form':form,'obj':obj,'progress_step':3,'is_updatable':True,'mypk':pk})




class  PropertyListView(ListView):
    model=Property


class PropertyDetailsView(DetailView):
    model=Property
    queryset=Property.objects.all()
    # template_name="main/property_detail.html"

def homeView(request):


    context={
        'property_list':Property.objects.all()
    }
    return render(request,"home.html",context=context)

def ContactView(request):
    return render(request,"contact.html")
