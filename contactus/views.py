from django.shortcuts import render, redirect
from contactus.forms import ContactUsForm

def contact_us(request):
    success_message = None

    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            # ریدایرکت به همان صفحه با anchor #contact
            return redirect('/#contact?success=1')
    else:
        form = ContactUsForm()

    # بررسی query param برای نمایش پیام موفقیت
    if request.GET.get('success'):
        success_message = "پیام شما با موفقیت ثبت شد."

    return render(request, 'index.html', {'contact_form': form, 'success_message': success_message})
