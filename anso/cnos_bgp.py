import random
import string
import os
from register import registerObj
import writer

class cnos_bgp:
    playbook_name = ''
    hosts=[]
    register=[]
    asNum = ''
    bgpArg1 = ''
    deviceType = ''
    host = ''
    outputfile = ''
    password = ''
    username = ''
    bgpArg2 = ''
    bgpArg3 = ''
    bgpArg4 = ''
    bgpArg5 = ''
    bgpArg6 = ''
    bgpArg7 = ''
    bgpArg8 = ''
    enablePassword = ''
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

