import random
import string
import os
from register import registerObj
import writer

class azure_rm_devtestlabvirtualmachine:
    playbook_name = ''
    hosts=[]
    register=[]
    lab_name = ''
    name = ''
    resource_group = ''
    ad_user = ''
    adfs_authority_url = ''
    allow_claim = ''
    api_profile = ''
    append_tags = ''
    artifacts = ''
    auth_source = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    disallow_public_ip_address = ''
    expiration_date = ''
    image = ''
    lab_subnet = ''
    notes = ''
    os_type = ''
    password = ''
    profile = ''
    secret = ''
    ssh_key = ''
    state = ''
    storage_type = ''
    subscription_id = ''
    tags = ''
    tenant = ''
    user_name = ''
    vm_size = ''
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

