from django_cron import CronJobBase, Schedule
from datetime import datetime
from django.contrib.auth.models import User
from base.views.send_mail import send_mail

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'base.views' # a unique code
    def do(self):
        users = User.objects.all()
        #  tourists = Tourist.objects.all()
        for tourist in users:
            send_mail('happy birthday', 'samanasoftware@gmail.com', [tourist.email], 'tourist/mail_birthday.txt',
                      'tourist/mail_birthday.html', {'user': tourist,'date': datetime.now()}, True)








# from celery import task
# from datetime import datetime
# from django.contrib.auth.models import User
# from celery.schedules import crontab
# from celery.task import periodic_task
# # @periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
# @task
# def add():
#     print("\nfiring test task\n")
#     # users = User.objects.all()
#     # for tourist in users:
#     #     tourist.email=str(datetime.now())+"abarshah@leader.com"
#     #     tourist.save()
#     # print("\n"+str(5+4)+"   boo0o0o0o0o0o0ZzZzzzzzzzZz    "+str(datetime.now())+"\n")
#     # return datetime.now()
