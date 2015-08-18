from django_cron import CronJobBase, Schedule
from datetime import datetime
from django.contrib.auth.models import User
from base.views.send_mail import send_mail
from tourist.models import Tourist
import urllib.parse
import urllib.request

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'tourist.view.task_birthday_sms' # a unique code
    def do(self):
        tourists = Tourist.objects.all()
        receptors =""
        for tourist in tourists:
            if (datetime.now().day==tourist.birth_day.day)&(datetime.now().month==tourist.birth_day.mounth):
                receptors = receptors+tourist.telephone



        api_key = '724F4F72774A6F384751442F504F6F724447734D4B413D3D'
        url = 'http://api.kavenegar.com/v1/' + api_key + '/sms/send.json'

        values = {
            'receptor': receptors,
            'sender': '30006703323323',
            'type': '1',
            'message': "”·«„. ”«„«‰Â ”Å«” «?—«‰ »Â ‘„« „—”? „?êÊ?œ »Â Œ«ÿ— «?‰òÂ Â” ?œ. «—”«· ‘œÂ «“ ÿ—?ﬁ òœ. „”∆Ê· »Œ‘  Õﬁ?ﬁ Ê  Ê”⁄Â :|"
        }

        data = urllib.parse.urlencode(values)
        binary_data = data.encode('utf-8')
        sms_req = urllib.request.Request(url, binary_data)
