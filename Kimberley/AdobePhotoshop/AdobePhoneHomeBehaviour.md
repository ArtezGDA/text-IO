```
Last login: Thu Dec  3 10:01:49 on ttys004
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% netsat -a               [28]
zsh: correct netsat to netstat ? ([Y]es/[N]o/[E]dit/[A]bort) n
zsh: command not found: netsat
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% netstat -a              [29]
Active Internet connections (including servers)
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)    
tcp4       0      0  192.168.217.104.59253  live.github.com.https  ESTABLISHED
tcp4       0      0  192.168.217.104.59204  live.github.com.https  ESTABLISHED
tcp4       0      0  192.168.217.104.59133  17.110.225.24.https    ESTABLISHED
tcp4       0      0  192.168.217.104.59010  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.217.104.59009  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.217.104.59000  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.217.104.58979  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.209.227.60364  n03.mail01.mtsvc.imaps ESTABLISHED
tcp4     143      0  192.168.209.227.59692  n03.mail01.mtsvc.imaps CLOSE_WAIT 
tcp4     143      0  192.168.209.227.57313  n03.mail01.mtsvc.imaps CLOSE_WAIT 
tcp4       0      0  *.7477                 *.*                    LISTEN     
tcp4       0      0  *.7476                 *.*                    LISTEN     
tcp4       0      0  *.7475                 *.*                    LISTEN     
tcp4       0      0  *.7474                 *.*                    LISTEN     
tcp4     143      0  192.168.0.24.59475     n03.mail01.mtsvc.imap  CLOSE_WAIT 
tcp4     143      0  192.168.0.24.62183     n03.mail01.mtsvc.imap  CLOSE_WAIT 
tcp4     143      0  192.168.0.24.59178     n03.mail01.mtsvc.imaps CLOSE_WAIT 
tcp4       0      0  192.168.214.121.59145  n03.mail01.mtsvc.imaps ESTABLISHED
tcp4       0      0  localhost.ipp          *.*                    LISTEN     
tcp6       0      0  localhost.ipp          *.*                    LISTEN     
udp6       0      0  *.52477                *.*                               
udp4       0      0  *.52477                *.*                               
udp6       0      0  *.62204                *.*                               
udp4       0      0  *.62204                *.*                               
udp4       0      0  *.64857                *.*                               
udp6       0      0  *.61257                *.*                               
udp4       0      0  *.61257                *.*                               
udp6       0      0  *.60795                *.*                               
udp4       0      0  *.60795                *.*                               
udp4       0      0  192.168.217.104.ntp    *.*                               
udp6       0      0  macbook-pro-van-.ntp   *.*                               
udp6       0      0  macbook-pro-van-.ntp   *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
netudp6       0      0  fe80::1%lo0.ntp        *.*                               
udp4       0      0  localhost.ntp          *.*                               
udp6       0      0  localhost.ntp          *.*                               
udp6       0      0  *.ntp                  *.*                               
udp4       0      0  *.ntp                  *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.53257                *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp46      0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp6       0      0  *.mdns                 *.*                               
udp4       0      0  *.mdns                 *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.netbios-ns           *.*                               
udp4       0      0  *.netbios-dgm          *.*                               
Active Multipath Internet connections
Proto/ID  Flags      Local Address          Foreign Address        (state)    
icm6       0      0  *.*                    *.*                               
Active LOCAL (UNIX) domain sockets
Address          Type   Recv-Q Send-Q            Inode             Conn             Refs          Nextref Addr
70e74ebb63faaef9 stream      0      0                0 70e74ebb5deea531                0                0 /var/run/mDNSResponder
70e74ebb5deea531 stream      0      0                0 70e74ebb63faaef9                0                0
70e74ebb53c068b1 stream      0      0                0 70e74ebb68d82021                0                0 /var/run/mDNSResponder
70e74ebb68d82021 stream      0      0                0 70e74ebb53c068b1                0                0
70e74ebb63fa9789 stream      0      0                0 70e74ebb63fa9f59                0                0 /var/run/mDNSResponder
70e74ebb63fa9f59 stream      0      0                0 70e74ebb63fa9789                0                0
70e74ebb63fab089 stream      0      0                0 70e74ebb6178e219                0                0 /var/run/mDNSResponder
70e74ebb6178e219 stream      0      0                0 70e74ebb63fab089                0                0
70e74ebb5dccedc9 stream      0      0                0 70e74ebb5deea3a1                0                0 /var/run/mDNSResponder
70e74ebb5deea3a1 stream      0      0                0 70e74ebb5dccedc9                0                0
70e74ebb63faa8b9 stream      0      0                0 70e74ebb5dcd0089                0                0 /var/run/mDNSResponder
70e74ebb5dcd0089 stream      0      0                0 70e74ebb63faa8b9                0                0
70e74ebb58420fc1 stream      0      0                0                0                0                0
70e74ebb5dccdb09 stream      0      0                0 70e74ebb5dee97e9                0                0 /var/run/mDNSResponder
70e74ebb5dee97e9 stream      0      0                0 70e74ebb5dccdb09                0                0
70e74ebb68d82e31 stream      0      0                0                0                0                0
70e74ebb6178d599 stream      0      0                0 70e74ebb63faab11                0                0 /tmp/com.adobe.csi.ctrl-CS7-Kimberleyterheerdt
70e74ebb63faab11 stream      0      0                0 70e74ebb6178d599                0                0
70e74ebb5dee9e29 stream      0      0                0 70e74ebb53c06a41                0                0 /var/run/mDNSResponder
70e74ebb53c06a41 stream      0      0                0 70e74ebb5dee9e29                0                0
70e74ebb5dcce469 stream      0      0 70e74ebb562c5b31                0                0                0 /tmp/com.cycling74.501/mfl_706
70e74ebb6178dfc1 stream      0      0                0 70e74ebb5deebef9                0                0 /var/run/mDNSResponder
70e74ebb5deebef9 stream      0      0                0 70e74ebb6178dfc1                0                0
70e74ebb5dccf021 stream      0      0                0 70e74ebb68d80bd1                0                0 /var/run/mDNSResponder
70e74ebb68d80bd1 stream      0      0                0 70e74ebb5dccf021                0                0
70e74ebb5dccd8b1 stream      0      0 70e74ebb6786ba41                0                0                0 /var/folders/wq/d1dqs3g943s4hv8h_rjgrqy00000gn/T/ics8464
70e74ebb5dccf341 stream      0      0                0 70e74ebb5dccec39                0                0 /var/run/mDNSResponder
70e74ebb5dccec39 stream      0      0                0 70e74ebb5dccf341                0                0
70e74ebb5841f789 stream      0      0                0 70e74ebb5dcce919                0                0 /var/run/mDNSResponder
70e74ebb5dcce919 stream      0      0                0 70e74ebb5841f789                0                0
70e74ebb63fab3a9 stream      0      0                0 70e74ebb58421089                0                0 /var/run/mDNSResponder
70e74ebb58421089 stream      0      0                0 70e74ebb63fab3a9                0                0
70e74ebb5deeab71 stream      0      0                0 70e74ebb5dcce211                0                0 /var/run/mDNSResponder
70e74ebb5dcce211 stream      0      0                0 70e74ebb5deeab71                0                0
70e74ebb5deea789 stream      0      0                0 70e74ebb58420729                0                0 /var/run/mDNSResponder
70e74ebb58420729 stream      0      0                0 70e74ebb5deea789                0                0
70e74ebb58420d69 stream      0      0                0 70e74ebb63fab471                0                0 /var/run/mDNSResponder
70e74ebb63fab471 stream      0      0                0 70e74ebb58420d69                0                0
70e74ebb6178e089 stream      0      0                0 70e74ebb6178e471                0                0 /var/run/mDNSResponder
70e74ebb6178e471 stream      0      0                0 70e74ebb6178e089                0                0
70e74ebb5dccdbd1 stream      0      0 70e74ebb53b172b1                0                0                0 /tmp/com.adobe.csi.ctrl-CS7-Kimberleyterheerdt
70e74ebb5dccfef9 stream      0      0                0 70e74ebb5dcd0219                0                0 /var/run/mDNSResponder
70e74ebb5dcd0219 stream      0      0                0 70e74ebb5dccfef9                0                0
70e74ebb584200e9 stream      0      0                0 70e74ebb58420021                0                0 /var/run/mDNSResponder
70e74ebb58420021 stream      0      0                0 70e74ebb584200e9                0                0
70e74ebb58420661 stream      0      0                0 70e74ebb58420599                0                0 /var/run/usbmuxd
70e74ebb58420599 stream      0      0                0 70e74ebb58420661                0                0
70e74ebb53c06591 stream      0      0 70e74ebb581eca41                0                0                0 /var/folders/wq/d1dqs3g943s4hv8h_rjgrqy00000gn/T/icssuis501
70e74ebb53c06659 stream      0      0                0 70e74ebb53c06721                0                0
70e74ebb53c06721 stream      0      0                0 70e74ebb53c06659                0                0
70e74ebb53c06d61 stream      0      0                0 70e74ebb53c06ef1                0                0 /var/run/mDNSResponder
70e74ebb53c06ef1 stream      0      0                0 70e74ebb53c06d61                0                0
70e74ebb53c07081 stream      0      0                0 70e74ebb53c07149                0                0 /var/run/mDNSResponder
70e74ebb53c07149 stream      0      0                0 70e74ebb53c07081                0                0
70e74ebb53c07211 stream      0      0                0 70e74ebb53c072d9                0                0 /var/run/mDNSResponder
70e74ebb53c072d9 stream      0      0                0 70e74ebb53c07211                0                0
70e74ebb53c073a1 stream      0      0                0 70e74ebb53c07531                0                0 /var/run/mDNSResponder
70e74ebb53c07531 stream      0      0                0 70e74ebb53c073a1                0                0
70e74ebb53c07d01 stream      0      0 70e74ebb569382b1                0                0                0 /private/tmp/com.apple.launchd.CgP1Iqx5XM/Listeners
70e74ebb53c07c39 stream      0      0 70e74ebb56938491                0                0                0 /private/tmp/com.apple.launchd.Yf5A3lTtY5/Render
70e74ebb53c07469 stream      0      0 70e74ebb564d63a1                0                0                0 /var/tmp/filesystemui.socket
70e74ebb53c08279 stream      0      0                0 70e74ebb53c08341                0                0
70e74ebb53c08341 stream      0      0                0 70e74ebb53c08279                0                0
70e74ebb53c08661 stream      0      0 70e74ebb54c381c1                0                0                0 /var/run/pppconfd
70e74ebb53c088b9 stream      0      0 70e74ebb54119771                0                0                0 /private/var/run/cupsd
70e74ebb53c08981 stream      0      0 70e74ebb5411a0d1                0                0                0 /var/run/usbmuxd
70e74ebb53c08a49 stream      0      0 70e74ebb540c0951                0                0                0 /var/run/systemkeychaincheck.socket
70e74ebb53c08b11 stream      0      0 70e74ebb54098a41                0                0                0 /var/run/portmap.socket
70e74ebb53c08bd9 stream      0      0 70e74ebb54098fe1                0                0                0 /var/run/vpncontrol.sock
70e74ebb53c08ca1 stream      0      0 70e74ebb540690d1                0                0                0 /var/rpc/ncacn_np/srvsvc
70e74ebb53c08d69 stream      0      0 70e74ebb540691c1                0                0                0 /var/rpc/ncalrpc/srvsvc
70e74ebb53c08e31 stream      0      0 70e74ebb540692b1                0                0                0 /var/rpc/ncacn_np/wkssvc
70e74ebb53c08ef9 stream      0      0 70e74ebb540693a1                0                0                0 /var/rpc/ncalrpc/wkssvc
70e74ebb53c08fc1 stream      0      0 70e74ebb5405d681                0                0                0 /var/rpc/ncalrpc/NETLOGON
70e74ebb53c09089 stream      0      0 70e74ebb5405da41                0                0                0 /var/rpc/ncacn_np/mdssvc
70e74ebb53c09151 stream      0      0 70e74ebb5405db31                0                0                0 /var/rpc/ncacn_np/lsarpc
70e74ebb53c09219 stream      0      0 70e74ebb5405dd11                0                0                0 /var/rpc/ncalrpc/lsarpc
70e74ebb53c092e1 stream      0      0 70e74ebb5403ec21                0                0                0 /var/run/mDNSResponder
70e74ebb68d82661 dgram       0      0                0 70e74ebb68d82409 70e74ebb68d82409                0
70e74ebb68d82409 dgram       0      0                0 70e74ebb68d82661 70e74ebb68d82661                0
70e74ebb5dee9bd1 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb68d81d01
70e74ebb68d83151 dgram       0      0                0 70e74ebb5deeba49 70e74ebb5deeba49                0
70e74ebb5deeba49 dgram       0      0                0 70e74ebb68d83151 70e74ebb68d83151                0
70e74ebb68d81469 dgram       0      0                0 70e74ebb5deec089 70e74ebb5deec089                0
70e74ebb5deec089 dgram       0      0                0 70e74ebb68d81469 70e74ebb68d81469                0
70e74ebb68d81d01 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5deebb11
70e74ebb5deebb11 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5841f531
70e74ebb53c06bd1 dgram       0      0                0 70e74ebb5dcce9e1 70e74ebb5dcce9e1                0
70e74ebb5dcce9e1 dgram       0      0                0 70e74ebb53c06bd1 70e74ebb53c06bd1                0
70e74ebb5deea149 dgram       0      0                0 70e74ebb5841e591 70e74ebb5841e591                0
70e74ebb5841e591 dgram       0      0                0 70e74ebb5deea149 70e74ebb5deea149                0
70e74ebb5841f531 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb68d80721
70e74ebb68d833a9 dgram       0      0                0 70e74ebb5841f469 70e74ebb5841f469                0
70e74ebb5841f469 dgram       0      0                0 70e74ebb68d833a9 70e74ebb68d833a9                0
70e74ebb5dee9b09 dgram       0      0                0 70e74ebb5841f9e1 70e74ebb5841f9e1                0
70e74ebb5841f9e1 dgram       0      0                0 70e74ebb5dee9b09 70e74ebb5dee9b09                0
70e74ebb68d80721 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb584201b1
70e74ebb5dccf4d1 dgram       0      0                0 70e74ebb5dccf729 70e74ebb5dccf729                0
70e74ebb5dccf729 dgram       0      0                0 70e74ebb5dccf4d1 70e74ebb5dccf4d1                0
70e74ebb5deea211 dgram       0      0                0 70e74ebb5deea851 70e74ebb5deea851                0
70e74ebb5deea851 dgram       0      0                0 70e74ebb5deea211 70e74ebb5deea211                0
70e74ebb584201b1 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c06e29
70e74ebb53c06e29 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dee9d61
70e74ebb5841faa9 dgram       0      0                0 70e74ebb63faaa49 70e74ebb63faaa49                0
70e74ebb63faaa49 dgram       0      0                0 70e74ebb5841faa9 70e74ebb5841faa9                0
70e74ebb5dee98b1 dgram       0      0                0 70e74ebb5dcce5f9 70e74ebb5dcce5f9                0
70e74ebb5dcce5f9 dgram       0      0                0 70e74ebb5dee98b1 70e74ebb5dee98b1                0
70e74ebb63fa99e1 dgram       0      0                0 70e74ebb5deeae91 70e74ebb5deeae91                0
70e74ebb5deeae91 dgram       0      0                0 70e74ebb63fa99e1 70e74ebb63fa99e1                0
70e74ebb584212e1 dgram       0      0                0 70e74ebb58420279 70e74ebb58420279                0
70e74ebb58420279 dgram       0      0                0 70e74ebb584212e1 70e74ebb584212e1                0
70e74ebb68d82fc1 dgram       0      0                0 70e74ebb5deebe31 70e74ebb5deebe31                0
70e74ebb5deebe31 dgram       0      0                0 70e74ebb68d82fc1 70e74ebb68d82fc1                0
70e74ebb5deeb8b9 dgram       0      0                0 70e74ebb5841efb9 70e74ebb5841efb9                0
70e74ebb5841efb9 dgram       0      0                0 70e74ebb5deeb8b9 70e74ebb5deeb8b9                0
70e74ebb5dee9d61 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb6178d729
70e74ebb6178d729 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dcd0471
70e74ebb5dcd0471 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dcce851
70e74ebb5deeadc9 dgram       0      0                0 70e74ebb6178d8b9 70e74ebb6178d8b9                0
70e74ebb6178d8b9 dgram       0      0                0 70e74ebb5deeadc9 70e74ebb5deeadc9                0
70e74ebb63faa1b1 dgram       0      0                0 70e74ebb63faa279 70e74ebb63faa279                0
70e74ebb63faa279 dgram       0      0                0 70e74ebb63faa1b1 70e74ebb63faa1b1                0
70e74ebb63fa96c1 dgram       0      0                0 70e74ebb5deea6c1 70e74ebb5deea6c1                0
70e74ebb5deea6c1 dgram       0      0                0 70e74ebb63fa96c1 70e74ebb63fa96c1                0
70e74ebb5deead01 dgram       0      0                0 70e74ebb5dee9979 70e74ebb5dee9979                0
70e74ebb5dee9979 dgram       0      0                0 70e74ebb5deead01 70e74ebb5deead01                0
70e74ebb5dee9591 dgram       0      0                0 70e74ebb5dee9fb9 70e74ebb5dee9fb9                0
70e74ebb5dee9fb9 dgram       0      0                0 70e74ebb5dee9591 70e74ebb5dee9591                0
70e74ebb5dcce3a1 dgram       0      0                0 70e74ebb5dee9c99 70e74ebb5dee9c99                0
70e74ebb5dee9c99 dgram       0      0                0 70e74ebb5dcce3a1 70e74ebb5dcce3a1                0
70e74ebb5dccf981 dgram       0      0                0 70e74ebb5dccfbd9 70e74ebb5dccfbd9                0
70e74ebb5dccfbd9 dgram       0      0                0 70e74ebb5dccf981 70e74ebb5dccf981                0
70e74ebb5deebfc1 dgram       0      0                0 70e74ebb5841eb09 70e74ebb5841eb09                0
70e74ebb5841eb09 dgram       0      0                0 70e74ebb5deebfc1 70e74ebb5deebfc1                0
70e74ebb5841e721 dgram       0      0                0 70e74ebb5841ff59 70e74ebb5841ff59                0
70e74ebb5841ff59 dgram       0      0                0 70e74ebb5841e721 70e74ebb5841e721                0
70e74ebb5dcce851 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dccee91
70e74ebb5dccee91 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c067e9
70e74ebb5dccdc99 dgram       0      0                0 70e74ebb5841fc39 70e74ebb5841fc39                0
70e74ebb5841fc39 dgram       0      0                0 70e74ebb5dccdc99 70e74ebb5dccdc99                0
70e74ebb5841ec99 dgram       0      0                0 70e74ebb5841fd01 70e74ebb5841fd01                0
70e74ebb5841fd01 dgram       0      0                0 70e74ebb5841ec99 70e74ebb5841ec99                0
70e74ebb58420e31 dgram       0      0                0 70e74ebb5841eef1 70e74ebb5841eef1                0
70e74ebb5841eef1 dgram       0      0                0 70e74ebb58420e31 70e74ebb58420e31                0
70e74ebb53c07dc9 dgram       0      0                0 70e74ebb5841f3a1 70e74ebb5841f3a1                0
70e74ebb5841f3a1 dgram       0      0                0 70e74ebb53c07dc9 70e74ebb53c07dc9                0
70e74ebb5841f851 dgram       0      0                0 70e74ebb5841ebd1 70e74ebb5841ebd1                0
70e74ebb5841ebd1 dgram       0      0                0 70e74ebb5841f851 70e74ebb5841f851                0
70e74ebb58420b11 dgram       0      0                0 70e74ebb584208b9 70e74ebb584208b9                0
70e74ebb584208b9 dgram       0      0                0 70e74ebb58420b11 70e74ebb58420b11                0
70e74ebb53c067e9 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c06b09
70e74ebb53c06b09 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c08409
70e74ebb53c07f59 dgram       0      0                0 70e74ebb53c08021 70e74ebb53c08021                0
70e74ebb53c08021 dgram       0      0                0 70e74ebb53c07f59 70e74ebb53c07f59                0
70e74ebb53c075f9 dgram       0      0                0 70e74ebb53c076c1 70e74ebb53c076c1                0
70e74ebb53c076c1 dgram       0      0                0 70e74ebb53c075f9 70e74ebb53c075f9                0
70e74ebb53c07919 dgram       0      0                0 70e74ebb53c079e1 70e74ebb53c079e1                0
70e74ebb53c079e1 dgram       0      0                0 70e74ebb53c07919 70e74ebb53c07919                0
70e74ebb53c07aa9 dgram       0      0                0 70e74ebb53c07b71 70e74ebb53c07b71                0
70e74ebb53c07b71 dgram       0      0                0 70e74ebb53c07aa9 70e74ebb53c07aa9                0
70e74ebb53c080e9 dgram       0      0                0 70e74ebb53c081b1 70e74ebb53c081b1                0
70e74ebb53c081b1 dgram       0      0                0 70e74ebb53c080e9 70e74ebb53c080e9                0
70e74ebb53c08409 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c093a9
70e74ebb53c084d1 dgram       0      0                0 70e74ebb53c08599 70e74ebb53c08599                0
70e74ebb53c08599 dgram       0      0                0 70e74ebb53c084d1 70e74ebb53c084d1                0
70e74ebb53c08729 dgram       0      0                0 70e74ebb53c087f1 70e74ebb53c087f1                0
70e74ebb53c087f1 dgram       0      0                0 70e74ebb53c08729 70e74ebb53c08729                0
70e74ebb53c093a9 dgram       0      0                0 70e74ebb53c09471                0                0
70e74ebb53c09471 dgram       0      0 70e74ebb53c01fe1                0 70e74ebb5dee9bd1                0 /private//var/run/syslog
Registered kernel control modules
id       flags    pcbcount rcvbuf   sndbuf   name 
       1        9        0   131072     8192 com.apple.flow-divert 
       2        1        0    16384     2048 com.apple.nke.sockwall 
       3        9        0   524288   524288 com.apple.content-filter 
       4        9        0     8192     2048 com.apple.packet-mangler 
       5        1        1    65536    65536 com.apple.net.necp_control 
       6        9        0   524288   524288 com.apple.net.utun_control 
       7        1        0    65536    65536 com.apple.net.ipsec_control 
       8        0       18     8192     2048 com.apple.netsrc 
       9       18        0     8192     2048 com.apple.network.statistics 
       a        5        0     8192     2048 com.apple.network.tcp_ccdebug 
Active kernel event sockets
Proto Recv-Q Send-Q vendor  class subcla
kevt       0      0      1      6      1
kevt       0      0      1      1      2
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      1      1
kevt       0      0      1      1      2
kevt       0      0      1      1      2
kevt       0      0      1      6      1
kevt       0      0      1      1      0
Active kernel control sockets
Proto Recv-Q Send-Q   unit     id name
kctl       0      0      1      5 com.apple.net.necp_control
kctl       0      0      1      8 com.apple.netsrc
kctl       0      0      2      8 com.apple.netsrc
kctl       0      0      3      8 com.apple.netsrc
kctl       0      0      4      8 com.apple.netsrc
kctl       0      0      5      8 com.apple.netsrc
kctl       0      0      6      8 com.apple.netsrc
kctl       0      0      7      8 com.apple.netsrc
kctl       0      0      8      8 com.apple.netsrc
kctl       0      0      9      8 com.apple.netsrc
kctl       0      0     10      8 com.apple.netsrc
kctl       0      0     12      8 com.apple.netsrc
kctl       0      0     16      8 com.apple.netsrc
kctl       0      0     18      8 com.apple.netsrc
kctl       0      0     21      8 com.apple.netsrc
kctl       0      0     24      8 com.apple.netsrc
kctl       0      0     25      8 com.apple.netsrc
kctl       0      0     26      8 com.apple.netsrc
kctl       0      0     29      8 com.apple.netsrc
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% netstat -a grep 'adobe'
Active Internet connections (including servers)
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)    
tcp4       0      0  192.168.217.104.59253  live.github.com.https  ESTABLISHED
tcp4       0      0  192.168.217.104.59204  live.github.com.https  ESTABLISHED
tcp4       0      0  192.168.217.104.59133  17.110.225.24.https    ESTABLISHED
tcp4       0      0  192.168.217.104.59010  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.217.104.59009  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.217.104.59000  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.217.104.58979  n03.mail01.mtsvc.imap  ESTABLISHED
tcp4       0      0  192.168.209.227.60364  n03.mail01.mtsvc.imaps ESTABLISHED
tcp4     143      0  192.168.209.227.59692  n03.mail01.mtsvc.imaps CLOSE_WAIT 
tcp4     143      0  192.168.209.227.57313  n03.mail01.mtsvc.imaps CLOSE_WAIT 
tcp4       0      0  *.7477                 *.*                    LISTEN     
tcp4       0      0  *.7476                 *.*                    LISTEN     
tcp4       0      0  *.7475                 *.*                    LISTEN     
tcp4       0      0  *.7474                 *.*                    LISTEN     
tcp4     143      0  192.168.0.24.59475     n03.mail01.mtsvc.imap  CLOSE_WAIT 
tcp4     143      0  192.168.0.24.62183     n03.mail01.mtsvc.imap  CLOSE_WAIT 
tcp4     143      0  192.168.0.24.59178     n03.mail01.mtsvc.imaps CLOSE_WAIT 
tcp4       0      0  192.168.214.121.59145  n03.mail01.mtsvc.imaps ESTABLISHED
tcp4       0      0  localhost.ipp          *.*                    LISTEN     
tcp6       0      0  localhost.ipp          *.*                    LISTEN     
udp6       0      0  *.52477                *.*                               
udp4       0      0  *.52477                *.*                               
udp6       0      0  *.62204                *.*                               
udp4       0      0  *.62204                *.*                               
udp4       0      0  *.64857                *.*                               
udp6       0      0  *.61257                *.*                               
udp4       0      0  *.61257                *.*                               
udp6       0      0  *.60795                *.*                               
udp4       0      0  *.60795                *.*                               
udp4       0      0  192.168.217.104.ntp    *.*                               
udp6       0      0  macbook-pro-van-.ntp   *.*                               
udp6       0      0  macbook-pro-van-.ntp   *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp6       0      0  fe80::1%lo0.ntp        *.*                               
udp4       0      0  localhost.ntp          *.*                               
udp6       0      0  localhost.ntp          *.*                               
udp6       0      0  *.ntp                  *.*                               
udp4       0      0  *.ntp                  *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.53257                *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp46      0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp6       0      0  *.mdns                 *.*                               
udp4       0      0  *.mdns                 *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.*                    *.*                               
udp4       0      0  *.netbios-ns           *.*                               
udp4       0      0  *.netbios-dgm          *.*                               
Active Multipath Internet connections
Proto/ID  Flags      Local Address          Foreign Address        (state)    
icm6       0      0  *.*                    *.*                               
Active LOCAL (UNIX) domain sockets
Address          Type   Recv-Q Send-Q            Inode             Conn             Refs          Nextref Addr
70e74ebb5deea531 stream      0      0                0 70e74ebb63faaef9                0                0 /var/run/mDNSResponder
70e74ebb63faaef9 stream      0      0                0 70e74ebb5deea531                0                0
70e74ebb53c068b1 stream      0      0                0 70e74ebb68d82021                0                0 /var/run/mDNSResponder
70e74ebb68d82021 stream      0      0                0 70e74ebb53c068b1                0                0
70e74ebb63fa9789 stream      0      0                0 70e74ebb63fa9f59                0                0 /var/run/mDNSResponder
70e74ebb63fa9f59 stream      0      0                0 70e74ebb63fa9789                0                0
70e74ebb63fab089 stream      0      0                0 70e74ebb6178e219                0                0 /var/run/mDNSResponder
70e74ebb6178e219 stream      0      0                0 70e74ebb63fab089                0                0
70e74ebb5dccedc9 stream      0      0                0 70e74ebb5deea3a1                0                0 /var/run/mDNSResponder
70e74ebb5deea3a1 stream      0      0                0 70e74ebb5dccedc9                0                0
70e74ebb63faa8b9 stream      0      0                0 70e74ebb5dcd0089                0                0 /var/run/mDNSResponder
70e74ebb5dcd0089 stream      0      0                0 70e74ebb63faa8b9                0                0
70e74ebb58420fc1 stream      0      0                0                0                0                0
70e74ebb5dccdb09 stream      0      0                0 70e74ebb5dee97e9                0                0 /var/run/mDNSResponder
70e74ebb5dee97e9 stream      0      0                0 70e74ebb5dccdb09                0                0
70e74ebb68d82e31 stream      0      0                0                0                0                0
70e74ebb6178d599 stream      0      0                0 70e74ebb63faab11                0                0 /tmp/com.adobe.csi.ctrl-CS7-Kimberleyterheerdt
70e74ebb63faab11 stream      0      0                0 70e74ebb6178d599                0                0
70e74ebb5dee9e29 stream      0      0                0 70e74ebb53c06a41                0                0 /var/run/mDNSResponder
70e74ebb53c06a41 stream      0      0                0 70e74ebb5dee9e29                0                0
70e74ebb5dcce469 stream      0      0 70e74ebb562c5b31                0                0                0 /tmp/com.cycling74.501/mfl_706
70e74ebb6178dfc1 stream      0      0                0 70e74ebb5deebef9                0                0 /var/run/mDNSResponder
70e74ebb5deebef9 stream      0      0                0 70e74ebb6178dfc1                0                0
70e74ebb5dccf021 stream      0      0                0 70e74ebb68d80bd1                0                0 /var/run/mDNSResponder
70e74ebb68d80bd1 stream      0      0                0 70e74ebb5dccf021                0                0
70e74ebb5dccd8b1 stream      0      0 70e74ebb6786ba41                0                0                0 /var/folders/wq/d1dqs3g943s4hv8h_rjgrqy00000gn/T/ics8464
70e74ebb5dccf341 stream      0      0                0 70e74ebb5dccec39                0                0 /var/run/mDNSResponder
70e74ebb5dccec39 stream      0      0                0 70e74ebb5dccf341                0                0
70e74ebb5841f789 stream      0      0                0 70e74ebb5dcce919                0                0 /var/run/mDNSResponder
70e74ebb5dcce919 stream      0      0                0 70e74ebb5841f789                0                0
70e74ebb63fab3a9 stream      0      0                0 70e74ebb58421089                0                0 /var/run/mDNSResponder
70e74ebb58421089 stream      0      0                0 70e74ebb63fab3a9                0                0
70e74ebb5deeab71 stream      0      0                0 70e74ebb5dcce211                0                0 /var/run/mDNSResponder
70e74ebb5dcce211 stream      0      0                0 70e74ebb5deeab71                0                0
70e74ebb5deea789 stream      0      0                0 70e74ebb58420729                0                0 /var/run/mDNSResponder
70e74ebb58420729 stream      0      0                0 70e74ebb5deea789                0                0
70e74ebb58420d69 stream      0      0                0 70e74ebb63fab471                0                0 /var/run/mDNSResponder
70e74ebb63fab471 stream      0      0                0 70e74ebb58420d69                0                0
70e74ebb6178e089 stream      0      0                0 70e74ebb6178e471                0                0 /var/run/mDNSResponder
70e74ebb6178e471 stream      0      0                0 70e74ebb6178e089                0                0
70e74ebb5dccdbd1 stream      0      0 70e74ebb53b172b1                0                0                0 /tmp/com.adobe.csi.ctrl-CS7-Kimberleyterheerdt
70e74ebb5dccfef9 stream      0      0                0 70e74ebb5dcd0219                0                0 /var/run/mDNSResponder
70e74ebb5dcd0219 stream      0      0                0 70e74ebb5dccfef9                0                0
70e74ebb584200e9 stream      0      0                0 70e74ebb58420021                0                0 /var/run/mDNSResponder
70e74ebb58420021 stream      0      0                0 70e74ebb584200e9                0                0
70e74ebb58420661 stream      0      0                0 70e74ebb58420599                0                0 /var/run/usbmuxd
70e74ebb58420599 stream      0      0                0 70e74ebb58420661                0                0
70e74ebb53c06591 stream      0      0 70e74ebb581eca41                0                0                0 /var/folders/wq/d1dqs3g943s4hv8h_rjgrqy00000gn/T/icssuis501
70e74ebb53c06659 stream      0      0                0 70e74ebb53c06721                0                0
70e74ebb53c06721 stream      0      0                0 70e74ebb53c06659                0                0
70e74ebb53c06d61 stream      0      0                0 70e74ebb53c06ef1                0                0 /var/run/mDNSResponder
70e74ebb53c06ef1 stream      0      0                0 70e74ebb53c06d61                0                0
70e74ebb53c07081 stream      0      0                0 70e74ebb53c07149                0                0 /var/run/mDNSResponder
70e74ebb53c07149 stream      0      0                0 70e74ebb53c07081                0                0
70e74ebb53c07211 stream      0      0                0 70e74ebb53c072d9                0                0 /var/run/mDNSResponder
70e74ebb53c072d9 stream      0      0                0 70e74ebb53c07211                0                0
70e74ebb53c073a1 stream      0      0                0 70e74ebb53c07531                0                0 /var/run/mDNSResponder
70e74ebb53c07531 stream      0      0                0 70e74ebb53c073a1                0                0
70e74ebb53c07d01 stream      0      0 70e74ebb569382b1                0                0                0 /private/tmp/com.apple.launchd.CgP1Iqx5XM/Listeners
70e74ebb53c07c39 stream      0      0 70e74ebb56938491                0                0                0 /private/tmp/com.apple.launchd.Yf5A3lTtY5/Render
70e74ebb53c07469 stream      0      0 70e74ebb564d63a1                0                0                0 /var/tmp/filesystemui.socket
70e74ebb53c08279 stream      0      0                0 70e74ebb53c08341                0                0
70e74ebb53c08341 stream      0      0                0 70e74ebb53c08279                0                0
70e74ebb53c08661 stream      0      0 70e74ebb54c381c1                0                0                0 /var/run/pppconfd
70e74ebb53c088b9 stream      0      0 70e74ebb54119771                0                0                0 /private/var/run/cupsd
70e74ebb53c08981 stream      0      0 70e74ebb5411a0d1                0                0                0 /var/run/usbmuxd
70e74ebb53c08a49 stream      0      0 70e74ebb540c0951                0                0                0 /var/run/systemkeychaincheck.socket
70e74ebb53c08b11 stream      0      0 70e74ebb54098a41                0                0                0 /var/run/portmap.socket
70e74ebb53c08bd9 stream      0      0 70e74ebb54098fe1                0                0                0 /var/run/vpncontrol.sock
70e74ebb53c08ca1 stream      0      0 70e74ebb540690d1                0                0                0 /var/rpc/ncacn_np/srvsvc
70e74ebb53c08d69 stream      0      0 70e74ebb540691c1                0                0                0 /var/rpc/ncalrpc/srvsvc
70e74ebb53c08e31 stream      0      0 70e74ebb540692b1                0                0                0 /var/rpc/ncacn_np/wkssvc
70e74ebb53c08ef9 stream      0      0 70e74ebb540693a1                0                0                0 /var/rpc/ncalrpc/wkssvc
70e74ebb53c08fc1 stream      0      0 70e74ebb5405d681                0                0                0 /var/rpc/ncalrpc/NETLOGON
70e74ebb53c09089 stream      0      0 70e74ebb5405da41                0                0                0 /var/rpc/ncacn_np/mdssvc
70e74ebb53c09151 stream      0      0 70e74ebb5405db31                0                0                0 /var/rpc/ncacn_np/lsarpc
70e74ebb53c09219 stream      0      0 70e74ebb5405dd11                0                0                0 /var/rpc/ncalrpc/lsarpc
70e74ebb53c092e1 stream      0      0 70e74ebb5403ec21                0                0                0 /var/run/mDNSResponder
70e74ebb68d82661 dgram       0      0                0 70e74ebb68d82409 70e74ebb68d82409                0
70e74ebb68d82409 dgram       0      0                0 70e74ebb68d82661 70e74ebb68d82661                0
70e74ebb5dee9bd1 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb68d81d01
70e74ebb68d83151 dgram       0      0                0 70e74ebb5deeba49 70e74ebb5deeba49                0
70e74ebb5deeba49 dgram       0      0                0 70e74ebb68d83151 70e74ebb68d83151                0
70e74ebb68d81469 dgram       0      0                0 70e74ebb5deec089 70e74ebb5deec089                0
70e74ebb5deec089 dgram       0      0                0 70e74ebb68d81469 70e74ebb68d81469                0
70e74ebb68d81d01 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5deebb11
70e74ebb5deebb11 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5841f531
70e74ebb53c06bd1 dgram       0      0                0 70e74ebb5dcce9e1 70e74ebb5dcce9e1                0
70e74ebb5dcce9e1 dgram       0      0                0 70e74ebb53c06bd1 70e74ebb53c06bd1                0
70e74ebb5deea149 dgram       0      0                0 70e74ebb5841e591 70e74ebb5841e591                0
70e74ebb5841e591 dgram       0      0                0 70e74ebb5deea149 70e74ebb5deea149                0
70e74ebb5841f531 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb68d80721
70e74ebb68d833a9 dgram       0      0                0 70e74ebb5841f469 70e74ebb5841f469                0
70e74ebb5841f469 dgram       0      0                0 70e74ebb68d833a9 70e74ebb68d833a9                0
70e74ebb5dee9b09 dgram       0      0                0 70e74ebb5841f9e1 70e74ebb5841f9e1                0
70e74ebb5841f9e1 dgram       0      0                0 70e74ebb5dee9b09 70e74ebb5dee9b09                0
70e74ebb68d80721 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb584201b1
70e74ebb5dccf4d1 dgram       0      0                0 70e74ebb5dccf729 70e74ebb5dccf729                0
70e74ebb5dccf729 dgram       0      0                0 70e74ebb5dccf4d1 70e74ebb5dccf4d1                0
70e74ebb5deea211 dgram       0      0                0 70e74ebb5deea851 70e74ebb5deea851                0
70e74ebb5deea851 dgram       0      0                0 70e74ebb5deea211 70e74ebb5deea211                0
70e74ebb584201b1 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c06e29
70e74ebb53c06e29 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dee9d61
70e74ebb5841faa9 dgram       0      0                0 70e74ebb63faaa49 70e74ebb63faaa49                0
70e74ebb63faaa49 dgram       0      0                0 70e74ebb5841faa9 70e74ebb5841faa9                0
70e74ebb5dee98b1 dgram       0      0                0 70e74ebb5dcce5f9 70e74ebb5dcce5f9                0
70e74ebb5dcce5f9 dgram       0      0                0 70e74ebb5dee98b1 70e74ebb5dee98b1                0
70e74ebb63fa99e1 dgram       0      0                0 70e74ebb5deeae91 70e74ebb5deeae91                0
70e74ebb5deeae91 dgram       0      0                0 70e74ebb63fa99e1 70e74ebb63fa99e1                0
70e74ebb584212e1 dgram       0      0                0 70e74ebb58420279 70e74ebb58420279                0
70e74ebb58420279 dgram       0      0                0 70e74ebb584212e1 70e74ebb584212e1                0
70e74ebb68d82fc1 dgram       0      0                0 70e74ebb5deebe31 70e74ebb5deebe31                0
70e74ebb5deebe31 dgram       0      0                0 70e74ebb68d82fc1 70e74ebb68d82fc1                0
70e74ebb5deeb8b9 dgram       0      0                0 70e74ebb5841efb9 70e74ebb5841efb9                0
70e74ebb5841efb9 dgram       0      0                0 70e74ebb5deeb8b9 70e74ebb5deeb8b9                0
70e74ebb5dee9d61 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb6178d729
70e74ebb6178d729 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dcd0471
70e74ebb5dcd0471 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dcce851
70e74ebb5deeadc9 dgram       0      0                0 70e74ebb6178d8b9 70e74ebb6178d8b9                0
70e74ebb6178d8b9 dgram       0      0                0 70e74ebb5deeadc9 70e74ebb5deeadc9                0
70e74ebb63faa1b1 dgram       0      0                0 70e74ebb63faa279 70e74ebb63faa279                0
70e74ebb63faa279 dgram       0      0                0 70e74ebb63faa1b1 70e74ebb63faa1b1                0
70e74ebb63fa96c1 dgram       0      0                0 70e74ebb5deea6c1 70e74ebb5deea6c1                0
70e74ebb5deea6c1 dgram       0      0                0 70e74ebb63fa96c1 70e74ebb63fa96c1                0
70e74ebb5deead01 dgram       0      0                0 70e74ebb5dee9979 70e74ebb5dee9979                0
70e74ebb5dee9979 dgram       0      0                0 70e74ebb5deead01 70e74ebb5deead01                0
70e74ebb5dee9591 dgram       0      0                0 70e74ebb5dee9fb9 70e74ebb5dee9fb9                0
70e74ebb5dee9fb9 dgram       0      0                0 70e74ebb5dee9591 70e74ebb5dee9591                0
70e74ebb5dcce3a1 dgram       0      0                0 70e74ebb5dee9c99 70e74ebb5dee9c99                0
70e74ebb5dee9c99 dgram       0      0                0 70e74ebb5dcce3a1 70e74ebb5dcce3a1                0
70e74ebb5dccf981 dgram       0      0                0 70e74ebb5dccfbd9 70e74ebb5dccfbd9                0
70e74ebb5dccfbd9 dgram       0      0                0 70e74ebb5dccf981 70e74ebb5dccf981                0
70e74ebb5deebfc1 dgram       0      0                0 70e74ebb5841eb09 70e74ebb5841eb09                0
70e74ebb5841eb09 dgram       0      0                0 70e74ebb5deebfc1 70e74ebb5deebfc1                0
70e74ebb5841e721 dgram       0      0                0 70e74ebb5841ff59 70e74ebb5841ff59                0
70e74ebb5841ff59 dgram       0      0                0 70e74ebb5841e721 70e74ebb5841e721                0
70e74ebb5dcce851 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb5dccee91
70e74ebb5dccee91 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c067e9
70e74ebb5dccdc99 dgram       0      0                0 70e74ebb5841fc39 70e74ebb5841fc39                0
70e74ebb5841fc39 dgram       0      0                0 70e74ebb5dccdc99 70e74ebb5dccdc99                0
70e74ebb5841ec99 dgram       0      0                0 70e74ebb5841fd01 70e74ebb5841fd01                0
70e74ebb5841fd01 dgram       0      0                0 70e74ebb5841ec99 70e74ebb5841ec99                0
70e74ebb58420e31 dgram       0      0                0 70e74ebb5841eef1 70e74ebb5841eef1                0
70e74ebb5841eef1 dgram       0      0                0 70e74ebb58420e31 70e74ebb58420e31                0
70e74ebb53c07dc9 dgram       0      0                0 70e74ebb5841f3a1 70e74ebb5841f3a1                0
70e74ebb5841f3a1 dgram       0      0                0 70e74ebb53c07dc9 70e74ebb53c07dc9                0
70e74ebb5841f851 dgram       0      0                0 70e74ebb5841ebd1 70e74ebb5841ebd1                0
70e74ebb5841ebd1 dgram       0      0                0 70e74ebb5841f851 70e74ebb5841f851                0
70e74ebb58420b11 dgram       0      0                0 70e74ebb584208b9 70e74ebb584208b9                0
70e74ebb584208b9 dgram       0      0                0 70e74ebb58420b11 70e74ebb58420b11                0
70e74ebb53c067e9 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c06b09
70e74ebb53c06b09 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c08409
70e74ebb53c07f59 dgram       0      0                0 70e74ebb53c08021 70e74ebb53c08021                0
70e74ebb53c08021 dgram       0      0                0 70e74ebb53c07f59 70e74ebb53c07f59                0
70e74ebb53c075f9 dgram       0      0                0 70e74ebb53c076c1 70e74ebb53c076c1                0
70e74ebb53c076c1 dgram       0      0                0 70e74ebb53c075f9 70e74ebb53c075f9                0
70e74ebb53c07919 dgram       0      0                0 70e74ebb53c079e1 70e74ebb53c079e1                0
70e74ebb53c079e1 dgram       0      0                0 70e74ebb53c07919 70e74ebb53c07919                0
70e74ebb53c07aa9 dgram       0      0                0 70e74ebb53c07b71 70e74ebb53c07b71                0
70e74ebb53c07b71 dgram       0      0                0 70e74ebb53c07aa9 70e74ebb53c07aa9                0
70e74ebb53c080e9 dgram       0      0                0 70e74ebb53c081b1 70e74ebb53c081b1                0
70e74ebb53c081b1 dgram       0      0                0 70e74ebb53c080e9 70e74ebb53c080e9                0
70e74ebb53c08409 dgram       0      0                0 70e74ebb53c09471                0 70e74ebb53c093a9
70e74ebb53c084d1 dgram       0      0                0 70e74ebb53c08599 70e74ebb53c08599                0
70e74ebb53c08599 dgram       0      0                0 70e74ebb53c084d1 70e74ebb53c084d1                0
70e74ebb53c08729 dgram       0      0                0 70e74ebb53c087f1 70e74ebb53c087f1                0
70e74ebb53c087f1 dgram       0      0                0 70e74ebb53c08729 70e74ebb53c08729                0
70e74ebb53c093a9 dgram       0      0                0 70e74ebb53c09471                0                0
70e74ebb53c09471 dgram       0      0 70e74ebb53c01fe1                0 70e74ebb5dee9bd1                0 /private//var/run/syslog
Registered kernel control modules
id       flags    pcbcount rcvbuf   sndbuf   name 
       1        9        0   131072     8192 com.apple.flow-divert 
       2        1        0    16384     2048 com.apple.nke.sockwall 
       3        9        0   524288   524288 com.apple.content-filter 
       4        9        0     8192     2048 com.apple.packet-mangler 
       5        1        1    65536    65536 com.apple.net.necp_control 
       6        9        0   524288   524288 com.apple.net.utun_control 
       7        1        0    65536    65536 com.apple.net.ipsec_control 
       8        0       18     8192     2048 com.apple.netsrc 
       9       18        0     8192     2048 com.apple.network.statistics 
       a        5        0     8192     2048 com.apple.network.tcp_ccdebug 
Active kernel event sockets
Proto Recv-Q Send-Q vendor  class subcla
kevt       0      0      1      6      1
kevt       0      0      1      1      2
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      6      1
kevt       0      0      1      1      1
kevt       0      0      1      1      2
kevt       0      0      1      1      2
kevt       0      0      1      6      1
kevt       0      0      1      1      0
Active kernel control sockets
Proto Recv-Q Send-Q   unit     id name
kctl       0      0      1      5 com.apple.net.necp_control
kctl       0      0      1      8 com.apple.netsrc
kctl       0      0      2      8 com.apple.netsrc
kctl       0      0      3      8 com.apple.netsrc
kctl       0      0      4      8 com.apple.netsrc
kctl       0      0      5      8 com.apple.netsrc
kctl       0      0      6      8 com.apple.netsrc
kctl       0      0      7      8 com.apple.netsrc
kctl       0      0      8      8 com.apple.netsrc
kctl       0      0      9      8 com.apple.netsrc
kctl       0      0     10      8 com.apple.netsrc
kctl       0      0     12      8 com.apple.netsrc
kctl       0      0     16      8 com.apple.netsrc
kctl       0      0     18      8 com.apple.netsrc
kctl       0      0     21      8 com.apple.netsrc
kctl       0      0     24      8 com.apple.netsrc
kctl       0      0     25      8 com.apple.netsrc
kctl       0      0     26      8 com.apple.netsrc
kctl       0      0     29      8 com.apple.netsrc
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]%                                                                                                   [31]
```