from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cart, BookOrder
from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

@receiver(post_save, sender=Cart)
def adjust_stock(sender, instance, **kwargs):
    if not instance.active:
        #Decrement stock counts
        orders = BookOrder.objects.filter(cart=instance)
        for order in orders:
            book = order.book
            book.stock -= order.quantity
            book.save()
        #Send thank you email
        subject = 'Thank you for Shopping with Mystery Books'
        from_email = 'postmaster@mysterybooks.com'
        to_email = { instance.user.email }

        email_context = Context({
            'username': instance.user.username,
            'orders': orders
        })

        text_email = render_to_string('email/purchase_email.txt', email_context)
        html_email = render_to_string('email/purchase_email.html', email_context)

        msg = EmailMultiAlternatives(subject, text_email, from_email, to_email)
        msg.attach_alternative(html_email, 'text/html')
        msg.content_subtype = 'html'
        msg.send()