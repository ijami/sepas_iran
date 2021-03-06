from django_cron import CronJobBase, Schedule
from datetime import datetime
from django.contrib.auth.models import User
from base.views.send_mail import send_mail
from tourist.models import Tourist
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'tourist.views.task_birthday_email' # a unique code
    def do(self):
        # users = User.objects.all()
        tourists = Tourist.objects.all()

        for tourist in tourists:
            # print(tourist.birth_day.day ==)
            # print(str(datetime.now().day)+"/"+str(datetime.now().month)+"  "+str(tourist.birth_day.day)+"/"+str(tourist.birth_day.mounth))
            if (datetime.now().day==tourist.birth_day.day)and(datetime.now().month==tourist.birth_day.month):
                send_mail('تبریک تولد', 'b.i.sepasiran@gmail.com', [tourist.primary_user.email], 'tourist/mail_birthday.txt',
                        'tourist/mail_birthday.html', {'user': tourist}, True)
