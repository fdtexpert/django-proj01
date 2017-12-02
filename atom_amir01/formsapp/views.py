from django.shortcuts import render
from . import forms
# Create your views here.

def index1(request):
    index_data = {'strdata': 'Hello World', 'numdata': 200}
    return render(request,'formsapp/index.html', index_data)

def other(request):
    return render(request,'formsapp/other.html')

def test1(request):
    return render(request,'formsapp/TEST.html')

def relative(request):
    return render(request,'formsapp/relative_url_templates.html')

def form_name_view(request):
    form = forms.amBasicForm()

    if request.method == 'POST':
        form = forms.amBasicForm(request.POST)

        if form.is_valid():
            print('VALIDATION OK...')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request,'formsapp/form_page.html',{'form': form})


def SystemUsers(request):

    form = forms.NewSystemUserForm()
    if request.method == 'POST':

        form = forms.NewSystemUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index1(request)
        else:
            print('Error')

    return render(request,'formsapp/users.html', {'form': form})
