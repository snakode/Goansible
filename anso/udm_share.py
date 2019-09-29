import random
import string
import os
from register import registerObj
import writer

class udm_share:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    ou = ''
    directorymode = ''
    group = ''
    host = ''
    nfs_custom_settings = ''
    nfs_hosts = ''
    owner = ''
    path = ''
    root_squash = ''
    samba_block_size = ''
    samba_blocking_locks = ''
    samba_browseable = ''
    samba_create_mode = ''
    samba_csc_policy = ''
    samba_custom_settings = ''
    samba_directory_mode = ''
    samba_directory_security_mode = ''
    samba_dos_filemode = ''
    samba_fake_oplocks = ''
    samba_force_create_mode = ''
    samba_force_directory_mode = ''
    samba_force_directory_security_mode = ''
    samba_force_group = ''
    samba_force_security_mode = ''
    samba_force_user = ''
    samba_hide_files = ''
    samba_hide_unreadable = ''
    samba_hosts_allow = ''
    samba_hosts_deny = ''
    samba_inherit_acls = ''
    samba_inherit_owner = ''
    samba_inherit_permissions = ''
    samba_invalid_users = ''
    samba_level_2_oplocks = ''
    samba_locking = ''
    samba_msdfs_root = ''
    samba_name = ''
    samba_nt_acl_support = ''
    samba_oplocks = ''
    samba_postexec = ''
    samba_preexec = ''
    samba_public = ''
    samba_security_mode = ''
    samba_strict_locking = ''
    samba_valid_users = ''
    samba_vfs_objects = ''
    samba_write_list = ''
    samba_writeable = ''
    state = ''
    subtree_checking = ''
    sync = ''
    writeable = ''
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

