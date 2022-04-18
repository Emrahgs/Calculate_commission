import csv

# ** Django Imports **
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.messages import success, error
from django.shortcuts import render

# ** App Imports **
from core.models import Commission
from core.utils import GUEST_READY

# File upload View

def index(request):
    if request.method == 'POST':
        if request.FILES.get('myfile'):
            upload_file = request.FILES.get('myfile').read().decode(
                'utf-8').splitlines()
            reader = csv.DictReader(upload_file)
            for row in reader:
                if not Commission.objects.filter(reservation=row.get('Reservation')).exists():
                    Commission.objects.create(
                        reservation=row.get('Reservation'),
                        check_in=row.get('Checkin'),
                        checkout=row.get('Checkout'),
                        flat=row.get('Flat'),
                        city=row.get('City'),
                        net_incoming=row.get('Net income, EUR'),
                    )
                    success(request, 'File uploaded successfully')    
                
                else:
                    error(request, 'Reservation already exists')
                    break
        else:
            message = 'Please select a file'
            error(request, message)
    return render(request, 'index.html',)

def download_csv_data(request):
    with open('Reservations.csv') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Reservations.csv'
        return response

def reservation(request):
    month = request.GET.get('month')
    total = 0

    if month:
        commissions = Commission.objects.filter(
            checkout__startswith=month, is_active=True)
    else:
        commissions = Commission.objects.filter(is_active=True)

    for commission in commissions:
        total = float(commission.net_incoming) * GUEST_READY[commission.city]
        
    context = {
        'commissions': commissions,
        'total': total,
    }
    return render(request, 'reservations.html', context=context)

def commissions(request):
    city = request.GET.get('city')
    context = {}
    total = 0

    if city:
        commissions = Commission.objects.filter(is_active=True, city=city)

        for commission in commissions:
            total += float(commission.net_incoming) * \
                GUEST_READY[commission.city]

        context = {
            'commissions': commissions,
            'total': total,
            'city': city,
        }
    return render(request, 'commissions.html', context=context)
