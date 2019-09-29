import random
import string
import os
from register import registerObj
import writer

class azure_rm_loadbalancer:
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
    backend_address_pools = ''
    backend_port = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    frontend_ip_configurations = ''
    frontend_port = ''
    idle_timeout = ''
    inbound_nat_pools = ''
    inbound_nat_rules = ''
    load_balancing_rules = ''
    load_distribution = ''
    location = ''
    natpool_backend_port = ''
    natpool_frontend_port_end = ''
    natpool_frontend_port_start = ''
    natpool_protocol = ''
    password = ''
    probe_fail_count = ''
    probe_interval = ''
    probe_port = ''
    probe_protocol = ''
    probe_request_path = ''
    probes = ''
    profile = ''
    protocol = ''
    public_ip_address_name = ''
    secret = ''
    sku = ''
    state = ''
    subscription_id = ''
    tags = ''
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

