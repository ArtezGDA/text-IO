```
Last login: Mon Dec 21 11:46:34 on ttys000
[JesseWensing@admins-MBP: ~]% ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
==> This script will install:
/usr/local/bin/brew
/usr/local/Library/...
/usr/local/share/man/man1/brew.1
==> The following directories will be made group writable:
/usr/local/.
/usr/local/bin
==> The following directories will have their owner set to JesseWensing:
/usr/local/.
/usr/local/bin
==> The following directories will have their group set to admin:
/usr/local/.
/usr/local/bin

Press RETURN to continue or any other key to abort
==> /usr/bin/sudo /bin/chmod g+rwx /usr/local/. /usr/local/bin
Password:
==> /usr/bin/sudo /usr/sbin/chown JesseWensing /usr/local/. /usr/local/bin
==> /usr/bin/sudo /usr/bin/chgrp admin /usr/local/. /usr/local/bin
==> /usr/bin/sudo /bin/mkdir /Library/Caches/Homebrew
==> /usr/bin/sudo /bin/chmod g+rwx /Library/Caches/Homebrew
==> /usr/bin/sudo /usr/sbin/chown JesseWensing /Library/Caches/Homebrew
==> Downloading and installing Homebrew...
remote: Counting objects: 3898, done.
remote: Compressing objects: 100% (3740/3740), done.
remote: Total 3898 (delta 33), reused 2376 (delta 21), pack-reused 0
Receiving objects: 100% (3898/3898), 3.39 MiB | 473.00 KiB/s, done.
Resolving deltas: 100% (33/33), done.
From https://github.com/Homebrew/homebrew
 * [new branch]      master     -> origin/master
HEAD is now at 4cf9479 brew.rb: only print "Kernel.exit" on failures.
==> Installation successful!
==> Next steps
Run `brew help` to get started
[JesseWensing@admins-MBP: ~]% brew install cowsay                          [15]
==> Downloading https://homebrew.bintray.com/bottles/cowsay-3.03.yosemite.bottle
######################################################################### 100.0%
==> Pouring cowsay-3.03.yosemite.bottle.1.tar.gz
🍺  /usr/local/Cellar/cowsay/3.03: 53 files, 228K
[JesseWensing@admins-MBP: ~]% cowsay "Hoi"                                 [16]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) n
 _____ 
< Hoi >
 ----- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
[JesseWensing@admins-MBP: ~]% cowsay -f stegosaurus "Hoi Jesse"                 [17]
 ___________ 
< Hoi Jesse >
 ----------- 
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
[JesseWensing@admins-MBP: ~]%               

```