from django_cron import CronJobBase, Schedule
from datetime import datetime
from django.contrib.auth.models import User
from base.views.send_mail import send_mail
from tourist.views.crm_function import send_recommended_mail
from tourist.models import Tourist
# from jdatetime.jalali import GregorianToJalali
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'tourist.views.task_recommended_email' # a unique code
    def do(self):
        tourists = Tourist.objects.all()
        for tourist in tourists:
            recommendations = send_recommended_mail(tourist.primary_user.id)
            recommendations.sort(key=lambda x: x.sold_number)
            send_mail('پیشنهادات سپاس ایران', 'b.i.sepasiran@gmail.com', [tourist.primary_user.email], 'tourist/mail_birthday.txt',
                      'tourist/recommendation.html', {'recommendations': recommendations,'tourist':tourist}, True)
