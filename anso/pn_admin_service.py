import random
import string
import os
from register import registerObj
import writer

class pn_admin_service:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    pn__if = ''
    pn_cliswitch = ''
    pn_icmp = ''
    pn_net_api = ''
    pn_nfs = ''
    pn_snmp = ''
    pn_ssh = ''
    pn_web = ''
    pn_web_log = ''
    pn_web_port = ''
    pn_web_ssl = ''
    pn_web_ssl_port = ''
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

