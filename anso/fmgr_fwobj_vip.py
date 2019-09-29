import random
import string
import os
from register import registerObj
import writer

class fmgr_fwobj_vip:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    arp_reply = ''
    color = ''
    comment = ''
    dns_mapping_ttl = ''
    dynamic_mapping = ''
    dynamic_mapping_arp_reply = ''
    dynamic_mapping_color = ''
    dynamic_mapping_comment = ''
    dynamic_mapping_dns_mapping_ttl = ''
    dynamic_mapping_extaddr = ''
    dynamic_mapping_extintf = ''
    dynamic_mapping_extip = ''
    dynamic_mapping_extport = ''
    dynamic_mapping_gratuitous_arp_interval = ''
    dynamic_mapping_http_cookie_age = ''
    dynamic_mapping_http_cookie_domain = ''
    dynamic_mapping_http_cookie_domain_from_host = ''
    dynamic_mapping_http_cookie_generation = ''
    dynamic_mapping_http_cookie_path = ''
    dynamic_mapping_http_cookie_share = ''
    dynamic_mapping_http_ip_header = ''
    dynamic_mapping_http_ip_header_name = ''
    dynamic_mapping_http_multiplex = ''
    dynamic_mapping_https_cookie_secure = ''
    dynamic_mapping_ldb_method = ''
    dynamic_mapping_mapped_addr = ''
    dynamic_mapping_mappedip = ''
    dynamic_mapping_mappedport = ''
    dynamic_mapping_max_embryonic_connections = ''
    dynamic_mapping_monitor = ''
    dynamic_mapping_nat_source_vip = ''
    dynamic_mapping_outlook_web_access = ''
    dynamic_mapping_persistence = ''
    dynamic_mapping_portforward = ''
    dynamic_mapping_portmapping_type = ''
    dynamic_mapping_protocol = ''
    dynamic_mapping_realservers_client_ip = ''
    dynamic_mapping_realservers_healthcheck = ''
    dynamic_mapping_realservers_holddown_interval = ''
    dynamic_mapping_realservers_http_host = ''
    dynamic_mapping_realservers_ip = ''
    dynamic_mapping_realservers_max_connections = ''
    dynamic_mapping_realservers_monitor = ''
    dynamic_mapping_realservers_port = ''
    dynamic_mapping_realservers_seq = ''
    dynamic_mapping_realservers_status = ''
    dynamic_mapping_realservers_weight = ''
    dynamic_mapping_server_type = ''
    dynamic_mapping_service = ''
    dynamic_mapping_src_filter = ''
    dynamic_mapping_srcintf_filter = ''
    dynamic_mapping_ssl_algorithm = ''
    dynamic_mapping_ssl_certificate = ''
    dynamic_mapping_ssl_cipher_suites_cipher = ''
    dynamic_mapping_ssl_cipher_suites_versions = ''
    dynamic_mapping_ssl_client_fallback = ''
    dynamic_mapping_ssl_client_renegotiation = ''
    dynamic_mapping_ssl_client_session_state_max = ''
    dynamic_mapping_ssl_client_session_state_timeout = ''
    dynamic_mapping_ssl_client_session_state_type = ''
    dynamic_mapping_ssl_dh_bits = ''
    dynamic_mapping_ssl_hpkp = ''
    dynamic_mapping_ssl_hpkp_age = ''
    dynamic_mapping_ssl_hpkp_backup = ''
    dynamic_mapping_ssl_hpkp_include_subdomains = ''
    dynamic_mapping_ssl_hpkp_primary = ''
    dynamic_mapping_ssl_hpkp_report_uri = ''
    dynamic_mapping_ssl_hsts = ''
    dynamic_mapping_ssl_hsts_age = ''
    dynamic_mapping_ssl_hsts_include_subdomains = ''
    dynamic_mapping_ssl_http_location_conversion = ''
    dynamic_mapping_ssl_http_match_host = ''
    dynamic_mapping_ssl_max_version = ''
    dynamic_mapping_ssl_min_version = ''
    dynamic_mapping_ssl_mode = ''
    dynamic_mapping_ssl_pfs = ''
    dynamic_mapping_ssl_send_empty_frags = ''
    dynamic_mapping_ssl_server_algorithm = ''
    dynamic_mapping_ssl_server_max_version = ''
    dynamic_mapping_ssl_server_min_version = ''
    dynamic_mapping_ssl_server_session_state_max = ''
    dynamic_mapping_ssl_server_session_state_timeout = ''
    dynamic_mapping_ssl_server_session_state_type = ''
    dynamic_mapping_type = ''
    dynamic_mapping_weblogic_server = ''
    dynamic_mapping_websphere_server = ''
    extaddr = ''
    extintf = ''
    extip = ''
    extport = ''
    gratuitous_arp_interval = ''
    http_cookie_age = ''
    http_cookie_domain = ''
    http_cookie_domain_from_host = ''
    http_cookie_generation = ''
    http_cookie_path = ''
    http_cookie_share = ''
    http_ip_header = ''
    http_ip_header_name = ''
    http_multiplex = ''
    https_cookie_secure = ''
    ldb_method = ''
    mapped_addr = ''
    mappedip = ''
    mappedport = ''
    max_embryonic_connections = ''
    mode = ''
    monitor = ''
    name = ''
    nat_source_vip = ''
    outlook_web_access = ''
    persistence = ''
    portforward = ''
    portmapping_type = ''
    protocol = ''
    realservers = ''
    realservers_client_ip = ''
    realservers_healthcheck = ''
    realservers_holddown_interval = ''
    realservers_http_host = ''
    realservers_ip = ''
    realservers_max_connections = ''
    realservers_monitor = ''
    realservers_port = ''
    realservers_seq = ''
    realservers_status = ''
    realservers_weight = ''
    server_type = ''
    service = ''
    src_filter = ''
    srcintf_filter = ''
    ssl_algorithm = ''
    ssl_certificate = ''
    ssl_cipher_suites = ''
    ssl_cipher_suites_cipher = ''
    ssl_cipher_suites_versions = ''
    ssl_client_fallback = ''
    ssl_client_renegotiation = ''
    ssl_client_session_state_max = ''
    ssl_client_session_state_timeout = ''
    ssl_client_session_state_type = ''
    ssl_dh_bits = ''
    ssl_hpkp = ''
    ssl_hpkp_age = ''
    ssl_hpkp_backup = ''
    ssl_hpkp_include_subdomains = ''
    ssl_hpkp_primary = ''
    ssl_hpkp_report_uri = ''
    ssl_hsts = ''
    ssl_hsts_age = ''
    ssl_hsts_include_subdomains = ''
    ssl_http_location_conversion = ''
    ssl_http_match_host = ''
    ssl_max_version = ''
    ssl_min_version = ''
    ssl_mode = ''
    ssl_pfs = ''
    ssl_send_empty_frags = ''
    ssl_server_algorithm = ''
    ssl_server_cipher_suites = ''
    ssl_server_cipher_suites_cipher = ''
    ssl_server_cipher_suites_priority = ''
    ssl_server_cipher_suites_versions = ''
    ssl_server_max_version = ''
    ssl_server_min_version = ''
    ssl_server_session_state_max = ''
    ssl_server_session_state_timeout = ''
    ssl_server_session_state_type = ''
    type = ''
    weblogic_server = ''
    websphere_server = ''
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

