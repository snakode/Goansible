import random
import string
import os
from register import registerObj
import writer

class azure_rm_trafficmanagerendpoint:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    profile_name = ''
    resource_group = ''
    type = ''
    ad_user = ''
    adfs_authority_url = ''
    api_profile = ''
    auth_source = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    enabled = ''
    geo_mapping = ''
    location = ''
    min_child_endpoints = ''
    password = ''
    priority = ''
    profile = ''
    secret = ''
    state = ''
    subscription_id = ''
    target = ''
    target_resource_id = ''
    tenant = ''
    weight = ''
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

