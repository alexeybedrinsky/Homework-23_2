from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import render, get_object_or_404
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'includes/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'includes/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image_preview")
    template_name = 'includes/product_form.html'
    success_url = reverse_lazy('products:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "image_preview")
    template_name = 'includes/product_form.html'
    success_url = reverse_lazy('products:products_list')

    def get_success_url(self):
        return reverse('products:products_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'includes/product_confirm_delete.html'
    success_url = reverse_lazy('products:products_list')