#cloud-config
chpasswd:
  list: |
    root:nutanix/4u
  expire: False
disable_root: false
ssh_pwauth:   true
write_files:
-   content: |
        BOOTPROTO=static
        DEVICE=eth0
        IPADDR=10.48.68.90
        GATEWAY=10.48.68.1
        NETMASK=255.255.254.0
        ONBOOT=yes
        TYPE=Ethernet
        USERCTL=no
    path: /etc/sysconfig/network-scripts/ifcfg-eth0
runcmd:
  - sudo ifup /etc/sysconfig/network-scripts/ifcfg-eth0
