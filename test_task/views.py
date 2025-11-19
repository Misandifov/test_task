import json
import time
import threading
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

API_URL = "https://test.icorp.uz/interview.php"
NGROK_URL = "https://cc5fb6c1a609.ngrok-free.app"
second_part_code = None


@csrf_exempt
def webhook(request):
    global second_part_code

    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    body = json.loads(request.body)
    second_part_code = body.get("part2")
    return JsonResponse({"status": "ok"})


def run_flow():
    global second_part_code
    second_part_code = None

    payload = {
        "msg": "Salom!",
        "url": NGROK_URL + "/webhook/"
    }
    r = requests.post(API_URL, json=payload)
    first_part = r.json().get("part1")
    print(f"Birinchi qism kodi: {first_part}")

    while second_part_code is None:
        time.sleep(1)
    print(f"Ikkinchi qism kodi: {second_part_code}")

    full_code = first_part + second_part_code

    r2 = requests.get(API_URL, params={"code": full_code})
    message = r2.json().get("msg")
    print(f"Yakuniy xabar: {message}")
    print(f"Birlashtirilgan kod: {full_code}")


def run_process(request):
    threading.Thread(target=run_flow).start()
    return JsonResponse({
        "status": "started",
        "message": "API flow ishga tushdi. Konsolni tekshiring!"
    })

