
1.Save the firewall-policies file in:
~/pox/pox/forwarding
2.replace the current l2_learning file with the attached l2_learning file.

To start the controller enter:
sudo ./pox.py forwarding.l2_learning

in one terminal

To start the mininet network:

sudo ./run.sh

in another terminal