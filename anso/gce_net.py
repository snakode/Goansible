import random
import string
import os
from register import registerObj
import writer

class gce_net:
    playbook_name = ''
    hosts=[]
    register=[]
    allowed = ''
    credentials_file = ''
    fwname = ''
    ipv4_range = ''
    mode = ''
    name = ''
    pem_file = ''
    project_id = ''
    service_account_email = ''
    src_range = ''
    src_tags = ''
    state = ''
    subnet_desc = ''
    subnet_name = ''
    subnet_region = ''
    target_tags = ''
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

