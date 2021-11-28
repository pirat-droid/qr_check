from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from cms.forms import CheckTaskForm
from cms.models import TasksModel, CheckListModel, ImageModel


@login_required(login_url='login/')
def home_view(request):
    user_group = request.user.groups.all().values_list()

    if user_group[0][1] == 'manager':
        tasks = TasksModel.objects.filter().all().order_by('-date_create')
        checks = CheckListModel.objects.filter().all()
        return render(request, 'home.html', {'tasks': tasks,
                                             'checks': checks,
                                             'cab': 'Кабинет - Руководителя'})

    else:
        tasks = TasksModel.objects.filter(executor_id=request.user.id, status=None).order_by('-date_create')
        checks = CheckListModel.objects.filter().all()
        return render(request, 'home.html', {'tasks': tasks,
                                             'checks': checks,
                                             'cab': 'Кабинет - Исполнителя',
                                             'group': user_group[0][1]})


# @login_required(login_url='login/')
def edit_task_view(request, pk):
    task = TasksModel.objects.get(pk=pk)
    checks = CheckListModel.objects.filter(task=pk)
    if request.method == 'POST':
        form = CheckTaskForm(request.POST, request.FILES, checks=checks)
        if form.is_valid():
            images = request.FILES.getlist('images')
            for image in images:
                ImageModel.objects.create(task_id=int(pk),
                                          image=image)
            status = True
            for check in checks:
                if not form.cleaned_data['extra_field_' + str(check.id)]:
                    TasksModel.objects.filter(id=pk).update(status=False)
                    status = False
                CheckListModel.objects.filter(id=check.id).update(
                    check=form.cleaned_data['extra_field_' + str(check.id)])
            if not status:
                return redirect(to='not_ready')
            else:
                TasksModel.objects.filter(id=pk).update(status=True)
                return redirect(to='ready')
    else:
        form = CheckTaskForm(checks=checks)
    return render(request, 'task.html', {'task': task,
                                         'checks': checks,
                                         'form': form})


@login_required(login_url='login/')
def task_view(request, pk):
    task = TasksModel.objects.get(pk=pk)
    images = ImageModel.objects.filter(task_id=pk)
    print(len(images))
    checks = CheckListModel.objects.filter(task=pk)
    return render(request, 'detail-task.html', {'task': task,
                                                'images': images,
                                                'checks': checks})


# @login_required(login_url='login/')
def ready_view(request):
    return render(request, 'ready.html', {})


# @login_required(login_url='login/')
def not_ready_view(request):
    return render(request, 'not_ready.html', {})