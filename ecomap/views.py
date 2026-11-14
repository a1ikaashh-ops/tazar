from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import EcoPoint
import json

def ecomap_view(request):
    points = EcoPoint.objects.all()
    points_data = []
    for point in points:
        points_data.append({
            'id': point.id,
            'title': point.title,
            'description': point.description,
            'type': point.type,
            'status': point.status,
            'lat': point.latitude,
            'lng': point.longitude,
            'reported_by': point.reported_by.username,
        })
    return render(request, 'ecomap/map.html', {
        'points_json': json.dumps(points_data)
    })

@login_required
def add_point(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        EcoPoint.objects.create(
            title=data['title'],
            description=data['description'],
            type=data['type'],
            latitude=data['lat'],
            longitude=data['lng'],
            reported_by=request.user
        )
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})

@login_required
def delete_point(request, pk):
    from django.shortcuts import get_object_or_404
    point = get_object_or_404(EcoPoint, pk=pk, reported_by=request.user)
    point.delete()
    return JsonResponse({'status': 'ok'})