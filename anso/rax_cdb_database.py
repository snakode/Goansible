import random
import string
import os
from register import registerObj
import writer

class rax_cdb_database:
    playbook_name = ''
    hosts=[]
    register=[]
    api_key = ''
    auth_endpoint = ''
    cdb_id = ''
    character_set = ''
    collate = ''
    credentials = ''
    env = ''
    identity_type = ''
    name = ''
    region = ''
    state = ''
    tenant_id = ''
    tenant_name = ''
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

