from django.shortcuts import render, redirect
from products.forms import ProductForm

def productadd(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productadd')
    context = {'form':form}
    return render(request, 'products/add_pro.html', context)

