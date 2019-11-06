from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Customers, CustomersPrice, Book
from .utils import ReadClass, CreateClass, UpdateClass, DeleteClass
from .forms import BookForm, BookModelFormset
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# CRUD on Customer Price
class CustomersRead(ReadClass):
    model = CustomersPrice

class CustomersCreate(CreateClass):
    model = CustomersPrice

class CustomersUpdate(UpdateClass):
    model = CustomersPrice

class CustomersDelete(DeleteClass):
    model = CustomersPrice

class CreateBookClass(SuccessMessageMixin, CreateView):
    # fields = '__all__'
    template_name = 'book.html'
    form_class = BookForm
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super(CreateBookClass, self).get_context_data(**kwargs)
        context['formset'] = BookModelFormset(queryset=Book.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        formset = BookModelFormset(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        formset.save()
        return HttpResponseRedirect(reverse('bookid', kwargs={'pk': self.pk}))


    # def form_valid(self, form):
    #     self.object = form.save()
    #     return super().form_valid(form)

# def create_book_with_authors(request):
#     template_name = 'book.html'
#     bookform = BookModelForm(request.POST)
#     formset = AuthorFormset(request.POST)
#     # if request.method == 'GET':
#         # bookform = BookModelForm(request.GET or None)
#         # formset = AuthorFormset(queryset=Author.objects.none())
#     if request.method == 'POST':
#
#         if bookform.is_valid() and formset.is_valid():
#             # first save this book, as its reference will be used in `Author`
#             book = bookform.save()
#             for form in formset:
#                 # so that `book` instance can be attached.
#                 author = form.save(commit=False)
#                 author.book = book
#                 author.save()
#             return redirect('store:book_list')
#     return render(request, template_name, {
#         'bookform': bookform,
#         'formset': formset,
#     })
