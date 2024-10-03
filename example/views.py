# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel! nothing changed</h1>
            <p>The current time is { now }.</p> wah yar
        </body>
    </html>
    '''
    return HttpResponse(html)