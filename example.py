#!/usr/bin/env python

import loadbalance

if __name__ == "__main__":
    
    command_list = []
    for x in xrange(100):
        command_list.append('sleep 2')

    # Load balance the bash scripts
    lb = loadbalance.LoadBalance(ppn=4)
    lb.run_commands(command_list)









