from django.http import JsonResponse
import json

from .migrations import main as bot


def telegram(request):
    request_data = request.body
    messages = json.loads(request_data.decode("utf-8"))
    print(messages)
    print('\n')
    remess = bot.main(messages)
    return JsonResponse(remess)
