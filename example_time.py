#!/usr/bin/env python

import loadbalance
import time

def execute_command(cmd):
    """Command that the map function calls"""
    
    import subprocess, socket
    
    pro = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pro.wait()
    stdout, stderr = pro.communicate()
    returnval = pro.returncode
    
    return {'host' :socket.gethostname(), 'cmd':cmd , 'returnval': returnval}


if __name__ == "__main__":
    
    command_list = []
    for x in xrange(100):
        command_list.append('sleep 2')

    # Load balance the bash scripts
    lb = loadbalance.LoadBalance(ppn=4)
    lb.set_retries(10)
    # lb.map(execute_command, command_list)

    # More control over the arguments
    tic = time.time()
    ar = lb.lview.map(execute_command, command_list)
        
    for i,r in enumerate(ar):
        print "task: %i finished on %s, %.3f percent finished at time %.3f "%(
                               i, r['host'], 100*((i+1)/float(len(command_list))), time.time()-tic )






    









