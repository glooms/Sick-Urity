import os
import sys
import re
import hashlib
from random import randint

from script_manager import Manager

#manager = Manager(description='Sick-Urity')


#@manager.command
#def hej():
#    print 'Hej'

#@manager.command
def make_new_pass(site):
    punch_dir = os.path.dirname(__file__)
    f = open(punch_dir + '.' + site + '.sick', 'a+')
    p = gen_pass()
    print p
    f.write(hashlib.sha512(p).hexdigest())

def gen_pass(*length):
    l = 10
    if length:
        l = length
    return ''.join([chr(randint(0, 93) + 33) for _ in xrange(l)])

if __name__ ==  '__main__':
    #manager.run()
    make_new_pass('hej')
