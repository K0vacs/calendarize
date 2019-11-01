from django.core.paginator import Paginator


def table(request, model):
    metas       = model._meta.fields
    results     = model.objects.all().values_list()
    per_page    = request.GET.get('results') or 1
    paginator   = Paginator(results, per_page)
    page = request.GET.get('page')
    pages = paginator.get_page(page)
    context     = {
                'metas': metas,
                'results': results,
                'pages': pages
                }
    return context
