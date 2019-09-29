import random
import string
import os
from register import registerObj
import writer

class fortios_user_adgrp:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    username = ''
    https = ''
    password = ''
    user_adgrp = ''
    vdom = ''
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

