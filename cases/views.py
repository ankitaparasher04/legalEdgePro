from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Case, CaseNote

@login_required
def case_detail(request, case_id):

    case = get_object_or_404(Case, id=case_id)

    if request.user != case.lawyer:
        return redirect('home')

    # Add note
    if request.method == "POST":
        content = request.POST.get('content')

        if content:
            CaseNote.objects.create(
                case=case,
                content=content
            )

        return redirect('case_detail', case_id=case.id)

    return render(request, 'cases/case_detail.html', {
        'case': case
    })




@login_required
def case_detail(request, case_id):

    case = get_object_or_404(Case, id=case_id)

    # Only assigned lawyer can access
    if request.user != case.lawyer:
        return redirect('home')

    if request.method == "POST":
        new_status = request.POST.get('status')
        case.status = new_status
        case.save()
        return redirect('lawyer_cases')

    return render(request, 'cases/case_detail.html', {
        'case': case
    })



@login_required
def client_cases(request):

    # Only allow client
    if request.user.role != 'client':
        return render(request, 'base.html')

    cases = Case.objects.filter(client=request.user).order_by('-created_at')

    return render(request, 'cases/client_cases.html', {
        'cases': cases
    })

@login_required
def lawyer_cases(request):

    # Only lawyer access
    if request.user.role != 'lawyer':
        return redirect('home')

    cases = Case.objects.filter(lawyer=request.user).order_by('-created_at')

    return render(request, 'cases/lawyer_cases.html', {
        'cases': cases
    })