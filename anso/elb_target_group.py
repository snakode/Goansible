import random
import string
import os
from register import registerObj
import writer

class elb_target_group:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    state = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    deregistration_delay_timeout = ''
    ec2_url = ''
    health_check_interval = ''
    health_check_path = ''
    health_check_port = ''
    health_check_protocol = ''
    health_check_timeout = ''
    healthy_threshold_count = ''
    modify_targets = ''
    port = ''
    profile = ''
    protocol = ''
    purge_tags = ''
    region = ''
    security_token = ''
    stickiness_enabled = ''
    stickiness_lb_cookie_duration = ''
    stickiness_type = ''
    successful_response_codes = ''
    tags = ''
    target_type = ''
    targets = ''
    unhealthy_threshold_count = ''
    validate_certs = ''
    vpc_id = ''
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

