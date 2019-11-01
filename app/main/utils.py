from django.core.paginator import Paginator


def table(request, model):
    title       = model._meta.object_name
    metas       = model._meta.fields
    per_page    = request.GET.get('results') or 10
    results     = model.objects.all().values_list()[per_page:]
    paginator   = Paginator(results, per_page)
    page = request.GET.get('page')
    pages = paginator.get_page(page)
    context     = {
                'title': title,
                'metas': metas,
                'results': results,
                'pages': pages
                }
    return context
