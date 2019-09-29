import random
import string
import os
from register import registerObj
import writer

class fmgr_secprof_web:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    comment = ''
    extended_log = ''
    ftgd_wf = ''
    ftgd_wf_exempt_quota = ''
    ftgd_wf_filters_action = ''
    ftgd_wf_filters_auth_usr_grp = ''
    ftgd_wf_filters_category = ''
    ftgd_wf_filters_log = ''
    ftgd_wf_filters_override_replacemsg = ''
    ftgd_wf_filters_warn_duration = ''
    ftgd_wf_filters_warning_duration_type = ''
    ftgd_wf_filters_warning_prompt = ''
    ftgd_wf_max_quota_timeout = ''
    ftgd_wf_options = ''
    ftgd_wf_ovrd = ''
    ftgd_wf_quota_category = ''
    ftgd_wf_quota_duration = ''
    ftgd_wf_quota_override_replacemsg = ''
    ftgd_wf_quota_type = ''
    ftgd_wf_quota_unit = ''
    ftgd_wf_quota_value = ''
    ftgd_wf_rate_crl_urls = ''
    ftgd_wf_rate_css_urls = ''
    ftgd_wf_rate_image_urls = ''
    ftgd_wf_rate_javascript_urls = ''
    https_replacemsg = ''
    inspection_mode = ''
    log_all_url = ''
    mode = ''
    name = ''
    options = ''
    override = ''
    override_ovrd_cookie = ''
    override_ovrd_dur = ''
    override_ovrd_dur_mode = ''
    override_ovrd_scope = ''
    override_ovrd_user_group = ''
    override_profile = ''
    override_profile_attribute = ''
    override_profile_type = ''
    ovrd_perm = ''
    post_action = ''
    replacemsg_group = ''
    url_extraction = ''
    url_extraction_redirect_header = ''
    url_extraction_redirect_no_content = ''
    url_extraction_redirect_url = ''
    url_extraction_server_fqdn = ''
    url_extraction_status = ''
    web = ''
    web_blacklist = ''
    web_bword_table = ''
    web_bword_threshold = ''
    web_content_header_list = ''
    web_content_log = ''
    web_extended_all_action_log = ''
    web_filter_activex_log = ''
    web_filter_applet_log = ''
    web_filter_command_block_log = ''
    web_filter_cookie_log = ''
    web_filter_cookie_removal_log = ''
    web_filter_js_log = ''
    web_filter_jscript_log = ''
    web_filter_referer_log = ''
    web_filter_unknown_log = ''
    web_filter_vbs_log = ''
    web_ftgd_err_log = ''
    web_ftgd_quota_usage = ''
    web_invalid_domain_log = ''
    web_keyword_match = ''
    web_log_search = ''
    web_safe_search = ''
    web_url_log = ''
    web_urlfilter_table = ''
    web_whitelist = ''
    web_youtube_restrict = ''
    wisp = ''
    wisp_algorithm = ''
    wisp_servers = ''
    youtube_channel_filter = ''
    youtube_channel_filter_channel_id = ''
    youtube_channel_filter_comment = ''
    youtube_channel_status = ''
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

