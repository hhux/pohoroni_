from django.shortcuts import render
from django.views.generic import DeleteView
from django import forms
from .models import Coffin, Urn, Info


def test_view(request):
    """"Путь к главной странице"""
    return render(request, 'base.html', {})


def info_view(request):
    """"Путь к странице инфо"""
    return render(request, 'info.html')


def items_view(request):
    """"Путь к странице с товарами"""
    return render(request, 'items.html')


def services_view(request):
    """"Путь к странице с товарами"""
    return render(request, 'services.html')




class ProductDetailView(DeleteView):
    """"Дать урлы товарам"""

    CT_MODEL_MODEL_CLASS = {
        'coffin': Coffin,
        'urn': Urn,
        'info': Info
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'


class ProductDetailViewForInfo(DeleteView):
    """"Еще один продукт детейл вью для страницы ИНФО"""

    CT_MODEL_MODEL_CLASS = {
        'coffin': Coffin,
        'urn': Urn,
        'info': Info
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'info.html'
    slug_url_kwarg = 'slug'


class ContactForm(forms.Form):
    """Форма обратной связи"""

    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField()
    copy = forms.BooleanField(required=False)
