import random
import string
import os
from register import registerObj
import writer

class rabbitmq_user:
    playbook_name = ''
    hosts=[]
    register=[]
    user = ''
    configure_priv = ''
    force = ''
    node = ''
    password = ''
    permissions = ''
    read_priv = ''
    state = ''
    tags = ''
    update_password = ''
    vhost = ''
    write_priv = ''
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

