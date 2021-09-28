import threading
from django.conf import settings
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from django.contrib.sites.shortcuts import get_current_site
from django.http import request
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from threading import Thread
from django.core.mail import EmailMessage

class MailCls:
    def _send(self,request,to:list[str],subject:str,templateName:str,context:dir):
        message = get_template(templateName).render(context )
        mail = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=to,
        reply_to=[settings.EMAIL_HOST_USER],
        )
        mail.content_subtype = "html"
        mail.send()
        
    def run(self,request,to:str,subject:str,templateName:str,context:dir):
        self.current_site = get_current_site(request)
        th=Thread(target=self._send,daemon=True,args=[request,to,subject,templateName,{**context,'site_name':self.current_site}],name='mail_seandingThread')
        th.start()
        # th.join()












    

