from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import sib_api_v3_sdk
from django.contrib import messages
from pprint import pprint
from sib_api_v3_sdk.rest import ApiException
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import send_mail, BadHeaderError
def index(request):
    return render(request,"index.html")
def service(request):
    return render(request,"service.html")
def contect(request):
    return render(request,"contect.html")
def sendmail(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Brevo configuration
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = 'YOUR_API_V3_KEY'
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

        # Email content
        subject = f"New Contact Form Submission from {name}"
        html_content = f"""
        <h3>New Contact Form Submission</h3>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Phone:</strong> {phone}</p>
        <p><strong>Message:</strong><br>{message}</p>
        """

        # Sender & receiver
        sender = {"name": "Website Contact", "email": "rishavparihar81@gmail.com"}  # verified in Brevo
        to = [{"email": "rishavparihar81@gmail.com", "name": "Rishav Parihar"}]                 # website owner

        # Prepare email
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=to,
            html_content=html_content,
            sender=sender,
            subject=subject
        )

        try:
                api_response = api_instance.send_transac_email(send_smtp_email)
                print("✅ Email API Response:", api_response)
                messages.success(request, "Email sent successfully!")
        except ApiException as e:
                print(" Exception when calling API:", e)
    messages.error(request, "Something went wrong. Try again later.")


    return render(request, 'contect.html')
     # contact form template
def blog(request):
    return render(request,"blog.html")
def aboutmore(request):
    return render(request,"aboutmore.html")
def certifications(request):
    return render(request,"certifications.html")
def aboutmore(request):
    return render(request, 'aboutmore.html')
def Skills(request):
    return render(request, 'Skills.html')
def projects(request):
    return render(request, 'projects.html') 
def hobbies(request):
    return render(request, 'hobbies.html') 
def childhood(request):
    return render(request, 'childhood.html') 
from django.http import FileResponse, HttpResponse
def download_resume(request):
    from django.http import FileResponse
from django.conf import settings
import os

def download_resume(request):
    # Static folder ke andar path
    file_path = os.path.join(settings.BASE_DIR, 'C:/Users/Rishav Parihar/Desktop/port/portfolio/static/files/Brajmohan.pdf')
    file_name = 'Brajmohan.pdf'  # Browser me jo naam dikhana hai

    # Seedha file serve karenge
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response
