import random
import string
import os
from register import registerObj
import writer

class mso_schema_site_anp_epg_staticleaf:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    schema = ''
    site = ''
    template = ''
    anp = ''
    epg = ''
    leaf = ''
    output_level = ''
    pod = ''
    port = ''
    state = ''
    timeout = ''
    use_proxy = ''
    use_ssl = ''
    username = ''
    validate_certs = ''
    vlan = ''
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

