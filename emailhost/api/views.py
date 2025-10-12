from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import EmailMessage

@api_view(['POST'])
def sendEmail(request):
    try:
        data = request.data
        name = data['name']
        cmpname = data['cmpname']
        email = data['email']
        mobile = data['mobile']
        subject = data['subject']
        content = data['content']
        body = f"""
        📩 New message from your portfolio site:

        Mail from {email}
         
        👤  Name: {name}

        🏢 Company: {cmpname}

        📧 Email: {email}

        📱  Mobile: {mobile}

        💬 Message:
        {content}
        """
        response = EmailMessage(
            subject=f'[Contact Form]  {subject}',body=body,from_email=email,to=['naveenpyit@gmail.com'],reply_to= [email])
        response.send(fail_silently=False)
        return Response({'status':1,'message':'Email Sent Successfully!'})
        
    except Exception as e:
        return Response({'status':0,'message':str(e)})
