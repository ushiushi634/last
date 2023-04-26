from django.shortcuts import render
from .models import BlogPost

def index_view(request):
    records = BlogPost.objects.order_by('-posted_at')
    return render(
        request, 'index.html', {'orderby_records': records}
    )
