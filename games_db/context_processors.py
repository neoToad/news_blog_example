from .models import EmailList, Article
from .forms import EmailListForm
from django.db.models import Q


def email_processor(request):

    form = EmailListForm()
    message = None
    alert = 'success'

    if request.method == 'POST':
        if EmailList.objects.filter(email=request.POST['email']).exists():
            message = "That email is already subscribed to the list."
            alert = 'danger'
            form = EmailListForm()
        else:
            sub = EmailList(email=request.POST['email'])
            sub.save()
            message = "You have successfully subscribed to the email list."
            form = EmailListForm()

    return {'form': form, 'message': message, 'alert': alert}