import random
import string
import os
from register import registerObj
import writer

class datadog_event:
    playbook_name = ''
    hosts=[]
    register=[]
    api_key = ''
    app_key = ''
    text = ''
    title = ''
    aggregation_key = ''
    alert_type = ''
    date_happened = ''
    host = ''
    priority = ''
    tags = ''
    validate_certs = ''
    def compile(self):
       self.playbook_name=writer.writer(self,self.playbook_name)

    def run(self):
       dump_name=''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
       os.system('{} | tee {}'.format(self.playbook_name,dump_name))
       self.register = registerObj(dump_name)
       os.remove(dump_name)

    def go(self):
       self.compile()
       self.run()

