
Bu loyiha test API bilan ishlashni ko‘rsatadi:  
- POST request yuborish → birinchi qism kodni olish  
- Webhook orqali ikkinchi qism kodni qabul qilish  
- Kodlarni birlashtirish (`full_code`)  
- GET request orqali yakuniy xabarni olish

---

git clone https://github.com/Misandifov/test_task.git

cd test_task


# Activate the virtual environment:
# On Linux / Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate

pip install -r requirements.txt

# Ngrok ishga tushurish va URL olish

ngrok http 8000
Shu bilan sizga public URL beriladi, masalan:
- https://cc5fb6c1a609.ngrok-free.app

Bu URL’ni views.py ichidagi NGROK_URL ga yozing:
- NGROK_URL = "https://cc5fb6c1a609.ngrok-free.app"

Shu bilan API webhook sizning lokal serveringizga ulanishi mumkin bo‘ladi.
python manage.py runserver


http://127.0.0.1:8000/run/

Console’da quyidagilar chiqadi:

- Birinchi qism kodi (part1)
- Ikkinchi qism kodi (part2) webhook orqali keladi
- Birlashtirilgan kod (full_code)
- Yakuniy xabar (msg)
