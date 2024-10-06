from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Project
from django.contrib.auth.decorators import login_required
from django import forms

# Define forms for better structure
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'client']

@login_required
def client_project_view(request):
    clients = Client.objects.all()
    projects = Project.objects.all()

    if request.method == 'POST':
        if 'client_name' in request.POST:
            client_form = ClientForm(request.POST)
            if client_form.is_valid():
                client = client_form.save(commit=False)
                client.created_by = request.user
                client.save()
                return redirect('client_project')

        elif 'project_name' in request.POST:
            project_form = ProjectForm(request.POST)
            if project_form.is_valid():
                project = project_form.save(commit=False)
                project.created_by = request.user
                project.save()
                return redirect('client_project')

    client_form = ClientForm()
    project_form = ProjectForm()
    
    return render(request, 'api/client_project.html', {
        'clients': clients,
        'projects': projects,
        'client_form': client_form,
        'project_form': project_form
    })

@login_required
def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_project')
    else:
        form = ClientForm(instance=client)
    
    return render(request, 'api/edit_client.html', {'form': form})

@login_required
def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return redirect('client_project')

@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('client_project')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'api/edit_project.html', {'form': form})

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('client_project')
