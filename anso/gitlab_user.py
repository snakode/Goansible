import random
import string
import os
from register import registerObj
import writer

class gitlab_user:
    playbook_name = ''
    hosts=[]
    register=[]
    email = ''
    name = ''
    password = ''
    server_url = ''
    username = ''
    access_level = ''
    api_password = ''
    api_token = ''
    api_url = ''
    api_username = ''
    confirm = ''
    external = ''
    group = ''
    isadmin = ''
    login_password = ''
    login_user = ''
    sshkey_file = ''
    sshkey_name = ''
    state = ''
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

