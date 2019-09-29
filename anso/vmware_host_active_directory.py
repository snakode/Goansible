import random
import string
import os
from register import registerObj
import writer

class vmware_host_active_directory:
    playbook_name = ''
    hosts=[]
    register=[]
    ad_domain = ''
    ad_password = ''
    ad_state = ''
    ad_user = ''
    cluster_name = ''
    esxi_hostname = ''
    hostname = ''
    password = ''
    port = ''
    username = ''
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

