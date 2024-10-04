from django.views.generic import ListView,DetailView
from .models import Content
from django.http import JsonResponse

class ContentDetailListView(DetailView):
    model = Content
    template_name = "content.html"
    context_object_name = 'content'

def save_link(request):
    if request.method == 'POST':
        current_url = request.POST.get('current_url')
        # Збережіть посилання (можливо, у базі даних)
        return JsonResponse({'message': 'Link saved!'})
    return JsonResponse({'error': 'Invalid request'}, status=400)