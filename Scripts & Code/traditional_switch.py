#!/usr/bin/python       ### HashBang the path to compiler [1] 


"""Traditional Topology

Run:
sudo python traditional_switch.py

Reference: [ARP Demo](https://github.com/biplabro/SDN-hands-on_Openflow-Mininet-RYU/blob/master/Notes%20%26%20Experiments/06.%20Address%20Resolution%20(NDP%2C%20ARP).md)

Testing:
sudo ovs-vsctl show
sudo ovs-appctl fdb/show s1
sudo ovs-ofctl -O OpenFlow13 dump-flows s1

"""

from mininet.topo import Topo          ### from <Library> import <module> [2]
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController

class SingleSwitchTopo(Topo):          ### Creating a class named SingleSwitchTopo
    "Single switch connected to n hosts."
    def build(self):
        s1 = self.addSwitch('s1', failMode='standalone')
        h1 = self.addHost('h1', mac="00:00:00:00:00:01", ip="192.168.1.1/24")       ### creating virtual hosts assigning mac, ip/subnet mask
        h2 = self.addHost('h2', mac="00:00:00:00:00:02", ip="192.168.1.2/24")
        h3 = self.addHost('h3', mac="00:00:00:00:00:03", ip="192.168.1.3/24")
        h4 = self.addHost('h4', mac="00:00:00:00:00:04", ip="192.168.1.4/24")
        self.addLink(h1, s1)            ### Link node to the network
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s1)

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()           ### Start single switch Topology, no SDN controller used
    c1 = RemoteController('c1', ip='127.0.0.1')     ### Remote controller set to 'localhost'
    net = Mininet(topo=topo, controller=c1)
    net.start()
    #net.pingAll()
    CLI(net)
    net.stop()

"""
### _References_

```
[1] http://stanford.edu/~jainr/basics.py#:~:text=%23!%2Fusr%2Fbin%2Fenv%20python,also%20called%20the%20%22hashbang%22.
[2] https://stackabuse.com/creating-and-importing-modules-in-python/
[3] 
[4] 
[5] 
[6] 
[7] 
```

"""
