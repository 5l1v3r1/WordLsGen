print """
#=======================================================================#

                        _   _ _     _                      
                       | | | (_)   | |                     
 __      _____  _ __ __| | | |_ ___| |_    __ _  ___ _ __  
 \ \ /\ / / _ \| '__/ _` | | | / __| __|  / _` |/ _ \ '_ \ 
  \ V  V / (_) | | | (_| | | | \__ \ |_  | (_| |  __/ | | |
   \_/\_/ \___/|_|  \__,_| |_|_|___/\__|  \__, |\___|_| |_|
                                           __/ |           
                                           |___/ 
         by: Oseid Aldary 


           
                              
#========================================================================#
 """ 

import random
import time
from optparse import OptionParser
from colorama import Fore
parser = OptionParser("""
usage:\n python WordGen.py -n <Enter random numbers>\n -w <Enter random characters>\n -d <Where to save the file>\n
example :- python WordGen.py -n 100 -w Oseid Aldary -d /root/Desktop/wl.txt
""")
parser.add_option("-n","--number",dest="len",type="int",help="put the value of numbers")
parser.add_option("-w","--word",dest="word",type="string",help="put the word for random")
parser.add_option("-d","--dir",dest="dir",type="string",help="put the directory of wordlist")
(options, args) = parser.parse_args()
random1 = 1
if options.len == None or options.word == None or options.dir == None:
    print (parser.usage)
    exit(0)
else:
    srand = str(options.word)
    a =int(random1)
    a2 =int(options.len)
print ("pleae wait for make wordlist for you :)....")
time.sleep(5)
file = open(options.dir,"w")
file.close()
while a < a2:
    a = a + 1
    g = random.randrange(a,a+100)
    file = open(options.dir,"a")
    r = random.randrange(1,10)
    n = ''.join(map(lambda unused: random.choice(srand),range(r)))
    file.write(str(g)+n+"\n")

    if True:
        file.close()
        file = open(options.dir,"r")
        c = file.read()
        print (c)
file.close()
if True:
    print ("done the wordlist hase been created "+str(options.dir))



