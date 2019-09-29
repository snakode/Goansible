import random
import string
import os
from register import registerObj
import writer

class ce_bgp_af:
    playbook_name = ''
    hosts=[]
    register=[]
    af_type = ''
    vrf_name = ''
    active_route_advertise = ''
    add_path_sel_num = ''
    allow_invalid_as = ''
    always_compare_med = ''
    as_path_neglect = ''
    auto_frr_enable = ''
    default_local_pref = ''
    default_med = ''
    default_rt_import_enable = ''
    determin_med = ''
    ebgp_ecmp_nexthop_changed = ''
    ebgp_if_sensitive = ''
    ecmp_nexthop_changed = ''
    ibgp_ecmp_nexthop_changed = ''
    igp_metric_ignore = ''
    import_process_id = ''
    import_protocol = ''
    ingress_lsp_policy_name = ''
    load_balancing_as_path_ignore = ''
    lowest_priority = ''
    mask_len = ''
    max_load_ebgp_num = ''
    max_load_ibgp_num = ''
    maximum_load_balance = ''
    med_none_as_maximum = ''
    network_address = ''
    next_hop_sel_depend_type = ''
    nexthop_third_party = ''
    nhp_relay_route_policy_name = ''
    originator_prior = ''
    policy_ext_comm_enable = ''
    policy_vpn_target = ''
    preference_external = ''
    preference_internal = ''
    preference_local = ''
    prefrence_policy_name = ''
    reflect_between_client = ''
    reflect_chg_path = ''
    reflector_cluster_id = ''
    reflector_cluster_ipv4 = ''
    relay_delay_enable = ''
    rib_only_enable = ''
    rib_only_policy_name = ''
    route_sel_delay = ''
    router_id = ''
    router_id_neglect = ''
    rr_filter_number = ''
    state = ''
    summary_automatic = ''
    supernet_label_adv = ''
    supernet_uni_adv = ''
    vrf_rid_auto_sel = ''
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

