from django_cron import CronJobBase, Schedule
from datetime import datetime
from django.contrib.auth.models import User
from base.views.send_mail import send_mail
from tourist.models import Tourist
import urllib.parse
import urllib.request


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # every 2 hours
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'tourist.views.task_birthday_sms'  # a unique code

    def do(self):
        tourists = Tourist.objects.all()
        # receptors = ""
        for tourist in tourists:
                msg = "سلام " + tourist.primary_user.first_name + " " + tourist.primary_user.last_name + " عزیز، سالگرد تولد شما را تبریکعرض می کنیم. سالی سرشار از موفقیت داشته باشید" + "\n" + "گروه بزرگ سپاس ایران"
            # if (datetime.now().day == tourist.birth_day.day) & (datetime.now().month == tourist.birth_day.mounth):
                api_key = '724F4F72774A6F384751442F504F6F724447734D4B413D3D'
                url = 'http://api.kavenegar.com/v1/' + api_key + '/sms/send.json'

                values = {
                    'receptor': tourist.telephone+"",
                    'sender': '30006703323323',
                    'type': '1',
                    'message': msg
                }

                data = urllib.parse.urlencode(values)
                binary_data = data.encode('utf-8')
                sms_req = urllib.request.Request(url, binary_data)
                sms_response = urllib.request.urlopen(sms_req)
                # print(sms_response.read())
                # receptors = receptors+tourist.telephone

