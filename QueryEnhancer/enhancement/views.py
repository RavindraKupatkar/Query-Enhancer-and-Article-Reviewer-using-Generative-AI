from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .query_enhancement import enhance_query
from .article_retrieval import get_articles_and_images
import requests
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

def enhance_query_view(request):
    if request.method == 'POST':
        user_query = request.POST.get('query')
        original_query, enhanced_query = enhance_query(user_query)
        response_data = {
            'original_query': original_query,
            'enhanced_query': enhanced_query
        }
        return JsonResponse(response_data)
    return HttpResponse("Invalid request", status=400)

@csrf_exempt
def proxy_newsapi(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        articles = get_articles_and_images(query)
        return JsonResponse({'articles': articles})
    return HttpResponse("Invalid request", status=400)

# If you need the get_articles view function
def get_articles(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        articles = get_articles_and_images(query)
        return JsonResponse({'articles': articles})
    return HttpResponse("Invalid request", status=400)
