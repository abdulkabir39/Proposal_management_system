from django.shortcuts import render,HttpResponse,redirect
from .forms import ProposalForm
from django.contrib import messages
def index(request):
    return render(request,'user.html')

def submit(request):
    form_= ProposalForm()
    data= {"form":form_}
    return render(request,'submit_prop.html',data)

def submit_proposal(request):
    if request.method == 'POST':
        form = ProposalForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()  # Saves the form data to the database
            messages.success(request, 'Proposal submitted successfully!')
            return HttpResponse('submit_proposal')  # Redirect to a success page or the same page
        else:
            messages.error(request, 'There was an error submitting the proposal.')
    else:
        form = ProposalForm()

    return render(request, 'submit_prop.html', {'form': form})

# Create your views here.
