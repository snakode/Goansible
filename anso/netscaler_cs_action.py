import random
import string
import os
from register import registerObj
import writer

class netscaler_cs_action:
    playbook_name = ''
    hosts=[]
    register=[]
    nitro_pass = ''
    nitro_user = ''
    nsip = ''
    comment = ''
    name = ''
    nitro_protocol = ''
    nitro_timeout = ''
    save_config = ''
    state = ''
    targetlbvserver = ''
    targetvserver = ''
    targetvserverexpr = ''
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

