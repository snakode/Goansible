import random
import string
import os
from register import registerObj
import writer

class ec2_ami:
    playbook_name = ''
    hosts=[]
    register=[]
    architecture = ''
    aws_access_key = ''
    aws_secret_key = ''
    billing_products = ''
    debug_botocore_endpoint_logs = ''
    delete_snapshot = ''
    description = ''
    device_mapping = ''
    ec2_url = ''
    enhanced_networking = ''
    image_id = ''
    image_location = ''
    instance_id = ''
    kernel_id = ''
    launch_permissions = ''
    name = ''
    no_reboot = ''
    profile = ''
    purge_tags = ''
    ramdisk_id = ''
    region = ''
    root_device_name = ''
    security_token = ''
    sriov_net_support = ''
    state = ''
    tags = ''
    validate_certs = ''
    virtualization_type = ''
    wait = ''
    wait_timeout = ''
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

