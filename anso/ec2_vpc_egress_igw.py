import random
import string
import os
from register import registerObj
import writer

class ec2_vpc_egress_igw:
    playbook_name = ''
    hosts=[]
    register=[]
    vpc_id = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    profile = ''
    region = ''
    security_token = ''
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

