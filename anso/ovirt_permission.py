import random
import string
import os
from register import registerObj
import writer

class ovirt_permission:
    playbook_name = ''
    hosts=[]
    register=[]
    auth = ''
    authz_name = ''
    fetch_nested = ''
    group_name = ''
    namespace = ''
    nested_attributes = ''
    object_id = ''
    object_name = ''
    object_type = ''
    poll_interval = ''
    quota_name = ''
    role = ''
    state = ''
    timeout = ''
    user_name = ''
    wait = ''
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

