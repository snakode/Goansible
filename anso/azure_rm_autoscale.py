import random
import string
import os
from register import registerObj
import writer

class azure_rm_autoscale:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    resource_group = ''
    ad_user = ''
    adfs_authority_url = ''
    api_profile = ''
    append_tags = ''
    auth_source = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    enabled = ''
    location = ''
    notifications = ''
    password = ''
    profile = ''
    profiles = ''
    secret = ''
    state = ''
    subscription_id = ''
    tags = ''
    target = ''
    tenant = ''
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

