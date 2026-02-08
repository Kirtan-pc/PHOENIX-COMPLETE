import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

from .services.assistant import process_command


@ensure_csrf_cookie
def landing(request):
    return render(request, 'chatbot/landing.html')

@ensure_csrf_cookie
def chat_page(request):
    return render(request, 'chatbot/index.html')


@csrf_protect
def api_chat(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required.'}, status=405)

    try:
        payload = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON.'}, status=400)

    message = (payload.get('message') or '').strip()
    if not message:
        return JsonResponse({'reply': 'Please type a message so I can help.'})

    try:
        result = process_command(message)
        return JsonResponse(result)
    except Exception as e:
        print(f"Error processing command: {e}")
        return JsonResponse({'error': str(e)}, status=500)
