Last login: Thu Jan  7 11:40:01 on ttys000
[broersebroeder@MacBook-Pro-van-Niels-2: ~]% cowsay 'hoi'                                                                                                                       [96]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) y
_arguments:comparguments:312: can only be called from completion function
[broersebroeder@MacBook-Pro-van-Niels-2: ~]% ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"                                          [97]
==> This script will install:
/usr/local/bin/brew
/usr/local/Library/...
/usr/local/share/man/man1/brew.1
==> The following directories will be made group writable:
/usr/local/.
/usr/local/bin
==> The following directories will have their owner set to broersebroeder:
/usr/local/.
/usr/local/bin
==> The following directories will have their group set to admin:
/usr/local/.
/usr/local/bin

Press RETURN to continue or any other key to abort
[broersebroeder@MacBook-Pro-van-Niels-2: ~]%                                                                                                                                    [98]
[broersebroeder@MacBook-Pro-van-Niels-2: ~]% ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"                                          [98]
==> This script will install:
/usr/local/bin/brew
/usr/local/Library/...
/usr/local/share/man/man1/brew.1
==> The following directories will be made group writable:
/usr/local/.
/usr/local/bin
==> The following directories will have their owner set to broersebroeder:
/usr/local/.
/usr/local/bin
==> The following directories will have their group set to admin:
/usr/local/.
/usr/local/bin

Press RETURN to continue or any other key to abort
==> /usr/bin/sudo /bin/chmod g+rwx /usr/local/. /usr/local/bin
Password:
==> /usr/bin/sudo /usr/sbin/chown broersebroeder /usr/local/. /usr/local/bin
==> /usr/bin/sudo /usr/bin/chgrp admin /usr/local/. /usr/local/bin
==> /usr/bin/sudo /bin/mkdir /Library/Caches/Homebrew
==> /usr/bin/sudo /bin/chmod g+rwx /Library/Caches/Homebrew
==> /usr/bin/sudo /usr/sbin/chown broersebroeder /Library/Caches/Homebrew
==> Downloading and installing Homebrew...
remote: Counting objects: 3934, done.
remote: Compressing objects: 100% (3777/3777), done.
remote: Total 3934 (delta 34), reused 2259 (delta 22), pack-reused 0
Receiving objects: 100% (3934/3934), 3.43 MiB | 1.36 MiB/s, done.
Resolving deltas: 100% (34/34), done.
From https://github.com/Homebrew/homebrew
 * [new branch]      master     -> origin/master
HEAD is now at a58b4b4 a few more diagnostic checks
==> Installation successful!
==> Next steps
Run `brew help` to get started
[broersebroeder@MacBook-Pro-van-Niels-2: ~]% cowsay "Hoi"  
 _____ 
< Hoi >
 ----- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

[broersebroeder@MacBook-Pro-van-Niels-2: ~]%  cowsay -f stegosaurus "Hoi"  

 _____ 
< Hoi >
 ----- 
\                             .       .
 \                           / `.   .' " 
  \                  .---.  <    > <    >  .---.
   \                 |    \  \ - ~ ~ - /  /    |
         _____          ..-~             ~-..-~
        |     |   \~~~\.'                    `./~~~/
       ---------   \__/                        \__/
      .'  O    \     /               /       \  " 
     (_____,    `._.'               |         }  \/~~~/
      `----.          /       }     |        /    \__/
            `-.      |       /      |       /      `. ,~~|
                ~-.__|      /_ - ~ ^|      /- _      `..-'   
                     |     /        |     /     ~-.     `-. _  _  _
                     |_____|        |_____|         ~ - . _ _ _ _ _>
[broersebroeder@MacBook-Pro-van-Niels-2: ~]%