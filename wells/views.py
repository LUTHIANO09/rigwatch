from django.http import HttpResponse
from django.shortcuts import render

# the differences between a project and an app in django is that project is the entire work while the app is created inside the project, which means we can have multiple app in one project

# Create your views here.

def well_list(request):
    wells = [
        {'id': 1, 'name': 'Bonga-01', 'pressure': 3850, 'status': 'NORMAL'},
        {'id': 2, 'name': 'Erha-02', 'pressure': 820, 'status': 'CRITICAL'},
        {'id': 3, 'name': 'Agbami-05', 'pressure': 4600, 'status': 'NORMAL'},
    ]
    return render( request,'wells/well_list.html', {'wells': wells})

def well_detail(request, well_id):
    wells = [
        {'id': 1, 'name': 'Bonga-01',  'pressure': 3850, 'status': 'NORMAL'},
        {'id': 2, 'name': 'Erha-02',   'pressure': 820,  'status': 'CRITICAL'},
        {'id': 3, 'name': 'Agbami-05', 'pressure': 4600, 'status': 'NORMAL'},
    ]
    well = next((w for w in wells if w['id'] == well_id), None)
    return render(request,'wells/well_detail.html', {'well': well})

def well_status(request,well_id):
    well = {
        1 : 'NORMAL',
        2 : 'CRITICAL',
        3 : 'OFFLINE',
    }
    status = well.get(well_id, 'UNKNOWN')
    return HttpResponse(f"Status for Well-{well_id:02d}: {status}")
