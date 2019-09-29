import random
import string
import os
from register import registerObj
import writer

class vmware_vmotion:
    playbook_name = ''
    hosts=[]
    register=[]
    destination_datastore = ''
    destination_host = ''
    hostname = ''
    password = ''
    port = ''
    use_instance_uuid = ''
    username = ''
    validate_certs = ''
    vm_name = ''
    vm_uuid = ''
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

