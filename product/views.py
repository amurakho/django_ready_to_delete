from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormMixin
from django.views.generic import FormView
from product import models, forms


class ProductListView(generic.ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(FormMixin, generic.DetailView):
    model = models.Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    form_class = forms.ReviewForm

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['reviews'] = models.Review.objects.filter(product=self.get_object())
        return context

    def post(self, request, slug):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        data = form.cleaned_data
        review = models.Review(**data)

        product = self.get_object()
        author = self.request.user
        review.product = product
        review.author = author

        review.save()
        return super(ProductDetailView, self).form_valid(form)