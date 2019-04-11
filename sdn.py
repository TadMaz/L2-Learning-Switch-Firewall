#!/usr/bin/python

# EEE4121F-B Lab 2
# SDN
# MZRTAD001
# Tadiwanashe Mazara

# Implementing a Layer-2 Firewall using POX and Mininet


from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import Topo

class TreeTopo(Topo):
    """ The Tree Topology for the experiment"""

    def build(self):
        """overwriting build from to Topo to define own Topology"""

        #Add 8 Hosts to network
        for host_no in range(1,9):
            self.addHost('h%s'% host_no , mac = '00:00:00:00:00:0%s'% host_no)

        #Add 7 switches to network
        for switch_no in range(1,8):
           self.addSwitch('s%s'% switch_no)
        
        #Add approipriate links --> top down, left to right

        #height 1
        self.addLink('s1','s2')
        self.addLink('s1','s5')

        #height 2
        self.addLink('s2','s3')
        self.addLink('s2','s4')
        self.addLink('s5','s6')
        self.addLink('s5','s7')

        #height 3
        self.addLink('s3','h1')
        self.addLink('s3','h2')
        self.addLink('s4','h3')
        self.addLink('s4','h4')
        self.addLink('s6','h5')
        self.addLink('s6','h6')
        self.addLink('s7','h7')
        self.addLink('s7','h8')
   
        return

def treeTopo():
    
    #make Tree Topology
    tree_topo = TreeTopo()

    #Add remote controller and topology to network
    net = Mininet( topo = tree_topo, controller=RemoteController )
    
    #start network, start CLI and stop mininet network
    net.interact()

if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()
