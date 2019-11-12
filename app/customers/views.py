from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *
from .utils import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

def test(request, pk):
    if request.method == 'GET':
        # obj = CustomersPrice.objects.filter(customer_id=pk)
        customerform = CustomersForm(instance=Customers.objects.get(pk=pk))
        formset = ServiceModelFormset(queryset=CustomersPrice.objects.filter(customer_id=pk))
    elif request.method == 'POST':
        formset = ServiceModelFormset(request.POST)
        # obj= get_object_or_404(Customers, pk=pk)
        customerform = CustomersForm(request.POST or None, instance=Customers.objects.get(pk=pk))

        if formset.is_valid() and customerform.is_valid():
            obj= customerform.save(commit= False)
            obj.save()

            for item in formset.save(commit=False):
                item.customer_id = pk
                item.save()
            return redirect('bookid', pk=pk)
    return render(request, 'test.html', {
        'formset': formset,
        'customer_form': customerform,
        })


# CRUD on Customer Price
class CustomersRead(ReadClass):
    model = CustomersPrice

class CustomersCreate(CreateClass):
    model = CustomersPrice

class CustomersUpdate(UpdateClass):
    model = CustomersPrice

class CustomersDelete(DeleteClass):
    model = CustomersPrice

class CreateServiceClass(SuccessMessageMixin, CreateView):
    template_name = 'book.html'
    form_class = CustomersPriceForm
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super(CreateServiceClass, self).get_context_data(**kwargs)
        customerprice = ServiceModelFormset(queryset=CustomersPrice.objects.none())
        context['formset'] = customerprice
        context['customer_form'] = CustomersForm()
        return context

    def post(self, request, *args, **kwargs):
        formset = ServiceModelFormset(request.POST)
        customerform = CustomersForm(request.POST)
        if formset.is_valid() and customerform.is_valid():
            return self.form_valid(formset, customerform)

    def form_valid(self, formset, customerform):
        response = customerform.save()
        for item in formset.save(commit=False):
            item.customer_id = response.pk
            item.save()
        return HttpResponseRedirect(reverse('bookid', kwargs={'pk': response.pk}))


# class UpdateServiceClass(SuccessMessageMixin, UpdateView):
#         template_name = 'add.html'
#         form_class = CustomersPriceForm
#         success_message = "%(price)s was updated successfully"
#         # get_queryset = CustomersPrice.objects.none()

#         def get_queryset(self):
#             self.customer_form = get_object_or_404(Publisher, name=self.kwargs['publisher'])
#         return Book.objects.filter(publisher=self.publisher)
#             # return CustomersPrice.objects.all()

#         def get_context_data(self, **kwargs):
#             context = super(UpdateServiceClass, self).get_context_data(**kwargs)
#             customer = Customers.objects.get(pk=self.kwargs['pk'])
#             customerprice = ServiceModelFormset(queryset=CustomersPrice.objects.filter(customer_id=self.kwargs['pk']))
#             context['formset'] = customerprice
#             context['customer_form'] = CustomersForm(instance=customer)
#             # return self.get_queryset(context)
#             return context




#         def post(self, request, *args, **kwargs):
#             super(UpdateServiceClass, self).post(request, *args, **kwargs)
#             formset = ServiceModelFormset(request.POST)
#             customerform = CustomersForm(request.POST)
#             if formset.is_valid() and customerform.is_valid():
#                 # return super(UpdateServiceClass, self).form_valid(formset, customerform)
#                 return self.form_valid(formset, customerform)

#         def form_valid(self, formset, customerform):
#             response = customerform.save()
#             for form in formset.save(commit=False):
#                 form.customer_id = response.pk
#                 form.save()
#             return HttpResponseRedirect(reverse_lazy('bookid', kwargs={'pk': response.pk}))


class CreateBookClass(SuccessMessageMixin, CreateView):
    # fields = '__all__'
    template_name = 'book.html'
    form_class = BookForm
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super(CreateBookClass, self).get_context_data(**kwargs)
        context['formset'] = BookModelFormset(queryset=Books.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        formset = BookModelFormset(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        formset.save()
        return HttpResponseRedirect(reverse('book'))
