import random
import string
import os
from register import registerObj
import writer

class avi_analyticsprofile:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    apdex_response_threshold = ''
    apdex_response_tolerated_factor = ''
    apdex_rtt_threshold = ''
    apdex_rtt_tolerated_factor = ''
    apdex_rum_threshold = ''
    apdex_rum_tolerated_factor = ''
    apdex_server_response_threshold = ''
    apdex_server_response_tolerated_factor = ''
    apdex_server_rtt_threshold = ''
    apdex_server_rtt_tolerated_factor = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    client_log_config = ''
    client_log_streaming_config = ''
    conn_lossy_ooo_threshold = ''
    conn_lossy_timeo_rexmt_threshold = ''
    conn_lossy_total_rexmt_threshold = ''
    conn_lossy_zero_win_size_event_threshold = ''
    conn_server_lossy_ooo_threshold = ''
    conn_server_lossy_timeo_rexmt_threshold = ''
    conn_server_lossy_total_rexmt_threshold = ''
    conn_server_lossy_zero_win_size_event_threshold = ''
    controller = ''
    description = ''
    disable_se_analytics = ''
    disable_server_analytics = ''
    exclude_client_close_before_request_as_error = ''
    exclude_dns_policy_drop_as_significant = ''
    exclude_gs_down_as_error = ''
    exclude_http_error_codes = ''
    exclude_invalid_dns_domain_as_error = ''
    exclude_invalid_dns_query_as_error = ''
    exclude_no_dns_record_as_error = ''
    exclude_no_valid_gs_member_as_error = ''
    exclude_persistence_change_as_error = ''
    exclude_server_dns_error_as_error = ''
    exclude_server_tcp_reset_as_error = ''
    exclude_syn_retransmit_as_error = ''
    exclude_tcp_reset_as_error = ''
    exclude_unsupported_dns_query_as_error = ''
    hs_event_throttle_window = ''
    hs_max_anomaly_penalty = ''
    hs_max_resources_penalty = ''
    hs_max_security_penalty = ''
    hs_min_dos_rate = ''
    hs_performance_boost = ''
    hs_pscore_traffic_threshold_l4_client = ''
    hs_pscore_traffic_threshold_l4_server = ''
    hs_security_certscore_expired = ''
    hs_security_certscore_gt30d = ''
    hs_security_certscore_le07d = ''
    hs_security_certscore_le30d = ''
    hs_security_chain_invalidity_penalty = ''
    hs_security_cipherscore_eq000b = ''
    hs_security_cipherscore_ge128b = ''
    hs_security_cipherscore_lt128b = ''
    hs_security_encalgo_score_none = ''
    hs_security_encalgo_score_rc4 = ''
    hs_security_hsts_penalty = ''
    hs_security_nonpfs_penalty = ''
    hs_security_selfsignedcert_penalty = ''
    hs_security_ssl30_score = ''
    hs_security_tls10_score = ''
    hs_security_tls11_score = ''
    hs_security_tls12_score = ''
    hs_security_weak_signature_algo_penalty = ''
    password = ''
    ranges = ''
    resp_code_block = ''
    state = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    url = ''
    username = ''
    uuid = ''
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

