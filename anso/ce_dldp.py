import random
import string
import os
from register import registerObj
import writer

class ce_dldp:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_mode = ''
    auth_pwd = ''
    enable = ''
    reset = ''
    time_internal = ''
    work_mode = ''
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

