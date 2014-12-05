from django.shortcuts import HttpResponse, render

# Create your views here.
from sample_datas.models import TableData

def home(request):
    data_query_set = TableData.objects.all()
    ## return HttpResponse('hi' + str(len(data_query_set)))
    context = {'sample_table': data_query_set}
    return render(request, 'sample_datas/sample_template.html', context)

def view_afterwards(request):
    return HttpResponse('received your data')
