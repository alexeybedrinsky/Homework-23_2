from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')


class ProductListView(ListView):
    model = Product
    template_name = 'includes/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'includes/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(Product, pk=pk)
        obj.views_counter += 1
        obj.save()
        return obj


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image_preview")
    template_name = 'includes/product_form.html'
    success_url = reverse_lazy('catalog:catalog_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "image_preview")
    template_name = 'includes/product_form.html'

    def get_success_url(self):
        return reverse('catalog:catalog_detail', args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'includes/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog_list')



