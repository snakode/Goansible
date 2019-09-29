import random
import string
import os
from register import registerObj
import writer

class fmgr_secprof_ssl_ssh:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    caname = ''
    comment = ''
    ftps = ''
    ftps_allow_invalid_server_cert = ''
    ftps_client_cert_request = ''
    ftps_ports = ''
    ftps_status = ''
    ftps_unsupported_ssl = ''
    ftps_untrusted_cert = ''
    https = ''
    https_allow_invalid_server_cert = ''
    https_client_cert_request = ''
    https_ports = ''
    https_status = ''
    https_unsupported_ssl = ''
    https_untrusted_cert = ''
    imaps = ''
    imaps_allow_invalid_server_cert = ''
    imaps_client_cert_request = ''
    imaps_ports = ''
    imaps_status = ''
    imaps_unsupported_ssl = ''
    imaps_untrusted_cert = ''
    mapi_over_https = ''
    mode = ''
    name = ''
    pop3s = ''
    pop3s_allow_invalid_server_cert = ''
    pop3s_client_cert_request = ''
    pop3s_ports = ''
    pop3s_status = ''
    pop3s_unsupported_ssl = ''
    pop3s_untrusted_cert = ''
    rpc_over_https = ''
    server_cert = ''
    server_cert_mode = ''
    smtps = ''
    smtps_allow_invalid_server_cert = ''
    smtps_client_cert_request = ''
    smtps_ports = ''
    smtps_status = ''
    smtps_unsupported_ssl = ''
    smtps_untrusted_cert = ''
    ssh = ''
    ssh_inspect_all = ''
    ssh_ports = ''
    ssh_ssh_algorithm = ''
    ssh_ssh_policy_check = ''
    ssh_ssh_tun_policy_check = ''
    ssh_status = ''
    ssh_unsupported_version = ''
    ssl = ''
    ssl_allow_invalid_server_cert = ''
    ssl_anomalies_log = ''
    ssl_client_cert_request = ''
    ssl_exempt = ''
    ssl_exempt_address = ''
    ssl_exempt_address6 = ''
    ssl_exempt_fortiguard_category = ''
    ssl_exempt_regex = ''
    ssl_exempt_type = ''
    ssl_exempt_wildcard_fqdn = ''
    ssl_exemptions_log = ''
    ssl_inspect_all = ''
    ssl_server = ''
    ssl_server_ftps_client_cert_request = ''
    ssl_server_https_client_cert_request = ''
    ssl_server_imaps_client_cert_request = ''
    ssl_server_ip = ''
    ssl_server_pop3s_client_cert_request = ''
    ssl_server_smtps_client_cert_request = ''
    ssl_server_ssl_other_client_cert_request = ''
    ssl_unsupported_ssl = ''
    ssl_untrusted_cert = ''
    untrusted_caname = ''
    use_ssl_server = ''
    whitelist = ''
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

