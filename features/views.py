from django.shortcuts import render
from .forms import  *
from .models import *
from main.models import PropertyType
from django.views.generic import ListView,UpdateView
# Create your views here.

class allCtagory(ListView):
    model=PropertyType
    template_name="features/ptype.html"

    def get_context_data(self,*args,**kwargs):
        # Call the base implementation first to get a context
        context=super(allCtagory,self).get_context_data(*args,**kwargs)
        # add all features quary to context
        context['features_list']=Features.objects.all()
        return context



def featureFormsView(request,pk):
    # ptypeId=5

    form=featureFrom(ptypeId=pk)
    if request.method=='POST':
        form=featureFrom(request.POST,ptypeId=pk)

        if form.is_valid():
            types=form.cleaned_data.get('types')
            print(types)
            form.save()

    ctx={
    'form':form,
    }
    return render(request,'features/featureform.html',ctx)

class updateFeature(UpdateView):
    form_class=featureFrom
    template_name='features/updateFeatureform.html'
    queryset=Features.objects.all()
    def get_initial(self):
        # get_initial is used to pre-populate a form with initial values before the form
        pass
        # TODO: for now stop here, after we marge this feature model with property from
         # only then we going to update the feature with particular type
         
