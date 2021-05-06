from django.shortcuts import render
from django.core.mail import send_mail
from .models import * #WhatImGoodAt, MyWork


def index(request):
    if request.method == 'POST':
        sender_name = request.POST['name']
        sender_email = request.POST['email']
        sender_message = request.POST['message']

        send_mail(
            sender_name,
            sender_message,
            sender_email,  # from email
            ['ugwujahswill@gmail.com'],  # to email
        )

        # WhatI'mGoodAt context
        HTML5_CSS3 = WhatImGoodAt.objects.get(id=1)
        creative_ideas = WhatImGoodAt.objects.get(id=2)
        easy_customize = WhatImGoodAt.objects.get(id=3)
        admin_dashboard = WhatImGoodAt.objects.get(id=4)

        # MyWork context
        first_title = MyWork.objects.get(id=1)
        second_title = MyWork.objects.get(id=2)
        item_third = MyWork.objects.get(id=3)
        item_forth = MyWork.objects.get(id=4)
        fifth_awesome = MyWork.objects.get(pk=5)
        awesome_sixth = MyWork.objects.get(id=6)


        context = dict(sender_name=sender_name, HTML5_CSS3=HTML5_CSS3,
                       creative_ideas=creative_ideas, easy_customize=easy_customize,
                       admin_dashboard=admin_dashboard, first_title=first_title,
                       second_title=second_title, item_third=item_third,
                       item_forth=item_forth,fifth_awesome=fifth_awesome,
                       awesome_sixth=awesome_sixth)

        return render(request, 'index.html', context)

    else:
        return render(request, 'index.html', {})
