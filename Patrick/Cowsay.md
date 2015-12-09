```
Last login: Wed Dec  9 14:11:51 on ttys001
MacBook-Pro-van-Patrick-Sanders% ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

==> This script will install:
/usr/local/bin/brew
/usr/local/Library/...
/usr/local/share/man/man1/brew.1
==> The following directories will be made group writable:
/usr/local/.
/usr/local/bin
==> The following directories will have their owner set to PatrickSanders:
/usr/local/.
/usr/local/bin
==> The following directories will have their group set to admin:
/usr/local/.
/usr/local/bin

Press RETURN to continue or any other key to abort
==> /usr/bin/sudo /bin/chmod g+rwx /usr/local/. /usr/local/bin
Password:
==> /usr/bin/sudo /usr/sbin/chown PatrickSanders /usr/local/. /usr/local/bin
==> /usr/bin/sudo /usr/bin/chgrp admin /usr/local/. /usr/local/bin
==> /usr/bin/sudo /bin/mkdir /Library/Caches/Homebrew
==> /usr/bin/sudo /bin/chmod g+rwx /Library/Caches/Homebrew
==> /usr/bin/sudo /usr/sbin/chown PatrickSanders /Library/Caches/Homebrew
==> Downloading and installing Homebrew...
remote: Counting objects: 3867, done.
remote: Compressing objects: 100% (3709/3709), done.
remote: Total 3867 (delta 33), reused 2425 (delta 23), pack-reused 0
Receiving objects: 100% (3867/3867), 3.37 MiB | 730.00 KiB/s, done.
Resolving deltas: 100% (33/33), done.
From https://github.com/Homebrew/homebrew
 * [new branch]      master     -> origin/master
HEAD is now at 2a6bb5c gauge: HEAD added
==> Installation successful!
==> Next steps
Run `brew help` to get started
MacBook-Pro-van-Patrick-Sanders% brew install cowsay
==> Downloading https://homebrew.bintray.com/bottles/cowsay-3.03.yosemite.bottle
######################################################################## 100,0%
==> Pouring cowsay-3.03.yosemite.bottle.1.tar.gz
🍺  /usr/local/Cellar/cowsay/3.03: 53 files, 228K
MacBook-Pro-van-Patrick-Sanders% `cowsay "Moo"`
zsh: command not found: _____
MacBook-Pro-van-Patrick-Sanders% `cowsay "Moo"`
zsh: command not found: _____
MacBook-Pro-van-Patrick-Sanders% cowsay "hoi"
 _____ 
< hoi >
 ----- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
MacBook-Pro-van-Patrick-Sanders% cowsay -f stegosaurus "hoi Patrick"
 _____________ 
< hoi Patrick >
 ------------- 
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
MacBook-Pro-van-Patrick-Sanders% 

```