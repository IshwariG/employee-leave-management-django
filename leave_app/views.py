
from django.shortcuts import render
from .models import Employee, Leave


def dashboard(request):
    context = {
        'total_employees': Employee.objects.count(),
        'total_leaves': Leave.objects.count(),
        'pending_leaves': Leave.objects.filter(status='Pending').count(),
        'approved_leaves': Leave.objects.filter(status='Approved').count(),
        'rejected_leaves': Leave.objects.filter(status='Rejected').count(),
        'recent_leaves': Leave.objects.select_related('employee').order_by('-applied_on')[:5],
    }
    return render(request, 'leave_app/dashboard.html', context)


def employee_list(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'leave_app/employees.html', {
        'employees': employees
    })


def leave_list(request):
    leaves = Leave.objects.select_related('employee').order_by('-applied_on')
    return render(request, 'leave_app/leaves.html', {
        'leaves': leaves
    })
