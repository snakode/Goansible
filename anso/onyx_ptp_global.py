import random
import string
import os
from register import registerObj
import writer

class onyx_ptp_global:
    playbook_name = ''
    hosts=[]
    register=[]
    domain = ''
    ntp_state = ''
    primary_priority = ''
    ptp_state = ''
    secondary_priority = ''
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

