from django.shortcuts import render
from django.http import JsonResponse
from celery.result import AsyncResult
from .tasks import scrape_coin_data
import uuid

def start_scraping(request):
    if request.method == 'POST':
        coin_list = request.POST.getlist('coins')
        job_id = str(uuid.uuid4())
        results = []
        for coin in coin_list:
            result = scrape_coin_data.apply_async((coin,))
            results.append({'coin': coin, 'task_id': result.id})

        response = {
            'job_id': job_id,
            'tasks': results
        }
        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'POST request required'}, status=400)

def scraping_status(request, job_id):
    if request.method == 'GET':
        task_ids = request.GET.getlist('task_ids')
        task_status = []
        for task_id in task_ids:
            result = AsyncResult(task_id)
            status = {
                'task_id': task_id,
                'state': result.state,
                'result': result.result
            }
            task_status.append(status)
        return JsonResponse({'job_id': job_id, 'tasks': task_status})
    else:
        return JsonResponse({'error': 'GET request required'}, status=400)
