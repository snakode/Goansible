import random
import string
import os
from register import registerObj
import writer

class postgresql_owner:
    playbook_name = ''
    hosts=[]
    register=[]
    new_owner = ''
    obj_type = ''
    ca_cert = ''
    db = ''
    fail_on_role = ''
    login_host = ''
    login_password = ''
    login_unix_socket = ''
    login_user = ''
    obj_name = ''
    port = ''
    reassign_owned_by = ''
    session_role = ''
    ssl_mode = ''
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

