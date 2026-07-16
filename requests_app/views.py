from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LegalRequest

from django.contrib.auth.decorators import login_required


from cases.models import Case

@login_required
def accept_request(request, request_id):

    if request.user.role != 'lawyer':
        return redirect('home')

    req = LegalRequest.objects.get(id=request_id)

    # Create case
    Case.objects.create(
        client=req.client,
        lawyer=request.user,
        title=req.title,
        description=req.description
    )

    # Update request status
    req.status = 'accepted'
    req.save()

    return redirect('lawyer_requests')


@login_required
def lawyer_requests(request):
    
    # Only allow lawyers
    if request.user.role != 'lawyer':
        return redirect('home')

    requests = LegalRequest.objects.all().order_by('-created_at')

    return render(request, 'requests_app/lawyer_requests.html', {
        'requests': requests
    })

@login_required
def create_request(request):

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        LegalRequest.objects.create(
            client=request.user,
            title=title,
            description=description
        )

        return redirect('client_dashboard')

    return render(request, 'requests_app/create_request.html')