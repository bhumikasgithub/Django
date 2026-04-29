from django.shortcuts import render
from .models import chaiVarity, Store
from django.shortcuts import get_object_or_404
from .forms import chaiVarityForm   
# Create your views here.
def all_chai(request):
    chasi = chaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chasi': chasi})

def chai_detail(request, chai_id):
    chai = get_object_or_404(chaiVarity, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai})

def chai_store_view(request):
    stores = None
    selected_chai = None
    if request.method == 'POST':
        form = chaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            selected_chai = chai_variety
            stores = Store.objects.filter(chai_varities=chai_variety)
    else:
        form = chaiVarityForm()
    
    return render(request, 'chai/chai_stores.html', {'stores': stores, 'form': form, 'selected_chai': selected_chai})