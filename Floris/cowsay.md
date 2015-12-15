Last login: Sun Dec 13 14:03:01 on ttys000
[florisversteeg@floriss-mbp: ~]% cowsay "hoi"                             [128]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) a
[florisversteeg@floriss-mbp: ~]%                                          [129]
[florisversteeg@floriss-mbp: ~]% ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
It appears Homebrew is already installed. If your intent is to reinstall you
should do the following before running this installer again:
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
The current contents of /usr/local are bin CODEOFCONDUCT.md CONTRIBUTING.md Library LICENSE.txt README.md share SUPPORTERS.md .git .gitignore
[florisversteeg@floriss-mbp: ~]% cowsay "Hoi"                             [130]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) a
[florisversteeg@floriss-mbp: ~]% ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
Warning: This script will remove:
/Library/Caches/Homebrew/
/usr/local/.git/
/usr/local/.gitignore
/usr/local/.travis.yml
/usr/local/.yardopts
/usr/local/CODEOFCONDUCT.md
/usr/local/CONTRIBUTING.md
/usr/local/LICENSE.txt
/usr/local/Library/
/usr/local/README.md
/usr/local/SUPPORTERS.md
/usr/local/bin/brew
/usr/local/share/doc/homebrew/
/usr/local/share/man/man1/brew.1
Are you sure you want to uninstall Homebrew? [y/N] y
==> Removing Homebrew installation...
==> Removing empty directories...
==> Homebrew uninstalled!
The following possible Homebrew files were not deleted:
/usr/local/bin/
/usr/local/share/
You may consider to remove them by yourself.
You may want to restore /usr/local's original permissions
  sudo chmod 0755 /usr/local
  sudo chgrp wheel /usr/local

[florisversteeg@floriss-mbp: ~]% ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
==> This script will install:
/usr/local/bin/brew
/usr/local/Library/...
/usr/local/share/man/man1/brew.1

Press RETURN to continue or any other key to abort
==> /usr/bin/sudo /bin/mkdir /Library/Caches/Homebrew
Password:
==> /usr/bin/sudo /bin/chmod g+rwx /Library/Caches/Homebrew
==> /usr/bin/sudo /usr/sbin/chown florisversteeg /Library/Caches/Homebrew
==> Downloading and installing Homebrew...

[florisversteeg@floriss-mbp: ~]%



pwd
Hoi
cowsay "hoi"
remote: Counting objects: 3881, done.
remote: Compressing objects: 100% (3725/3725), done.
remote: Total 3881 (delta 33), reused 2365 (delta 21), pack-reused 0
Receiving objects: 100% (3881/3881), 3.36 MiB | 68.00 KiB/s, done.
Resolving deltas: 100% (33/33), done.
From https://github.com/Homebrew/homebrew
 * [new branch]      master     -> origin/master
HEAD is now at 2ebbd5c bottle: don't use empty tab.
==> Installation successful!
==> Next steps
Run `brew help` to get started
[florisversteeg@floriss-mbp: ~]%                                          [133]
[florisversteeg@floriss-mbp: ~]% [florisversteeg@floriss-mbp: ~]%         [133]
zsh: command not found: [florisversteeg@floriss-mbp:
[florisversteeg@floriss-mbp: ~]%                                          [134]
[florisversteeg@floriss-mbp: ~]%                                          [134]
[florisversteeg@floriss-mbp: ~]%                                          [134]
[florisversteeg@floriss-mbp: ~]% pwd                                      [134]
/Users/florisversteeg
[florisversteeg@floriss-mbp: ~]% Hoi                                      [135]
zsh: command not found: Hoi
[florisversteeg@floriss-mbp: ~]% cowsay "hoi"                             [135]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) a
[florisversteeg@floriss-mbp: ~]%                                          [136]
[florisversteeg@floriss-mbp: ~]% pwd                                      [136]
/Users/florisversteeg
[florisversteeg@floriss-mbp: ~]% cowsay "hoi"                             [137]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) a
[florisversteeg@floriss-mbp: ~]%                                          [136]
[florisversteeg@floriss-mbp: ~]% 'brew help'                              [136]
zsh: command not found: brew help
[florisversteeg@floriss-mbp: ~]% run 'brew help'                          [137]
zsh: correct run to ru ? ([Y]es/[N]o/[E]dit/[A]bort) y
USER              PID  %CPU %MEM      VSZ    RSS   TT  STAT STARTED      TIME COMMAND
[florisversteeg@floriss-mbp: ~]%                                          [138]
[florisversteeg@floriss-mbp: ~]% ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
It appears Homebrew is already installed. If your intent is to reinstall you
should do the following before running this installer again:
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
The current contents of /usr/local are bin CODEOFCONDUCT.md CONTRIBUTING.md Library LICENSE.txt README.md share SUPPORTERS.md .git .gitignore
[florisversteeg@floriss-mbp: ~]% cowsay "hoi"                             [139]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) a
[florisversteeg@floriss-mbp: ~]%                                          [140]
[florisversteeg@floriss-mbp: ~]% brew install cowsay                      [140]
==> Downloading https://homebrew.bintray.com/bottles/cowsay-3.03.el_capitan.bott
######################################################################### 100.0%
==> Pouring cowsay-3.03.el_capitan.bottle.1.tar.gz
🍺  /usr/local/Cellar/cowsay/3.03: 53 files, 228K
[florisversteeg@floriss-mbp: ~]% 'cowsay "moo"'                           [141]
zsh: command not found: cowsay "moo"
[florisversteeg@floriss-mbp: ~]% cowsay "moo"                             [142]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) a
[florisversteeg@floriss-mbp: ~]% cowsay "hoi"                             [143]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort)  
_arguments:comparguments:312: can only be called from completion function
[florisversteeg@floriss-mbp: ~]% cowsay "hoi"                             [144]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort)  
_arguments:comparguments:312: can only be called from completion function
[florisversteeg@floriss-mbp: ~]% cowsay "hoi"                             [144]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort)  
_arguments:comparguments:312: can only be called from completion function
[florisversteeg@floriss-mbp: ~]% cowsay "hoi"                             [144]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) a
[florisversteeg@floriss-mbp: ~]%  cowsay "hoi"                            [145]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) a
[florisversteeg@floriss-mbp: ~]% cowsay "Hoi"                             [146]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) a
[florisversteeg@floriss-mbp: ~]% 'brew help'                              [146]
zsh: command not found: brew help
[florisversteeg@floriss-mbp: ~]%  install brew                            [147]
usage: install [-bCcpSsv] [-B suffix] [-f flags] [-g group] [-m mode]
               [-o owner] file1 file2
       install [-bCcpSsv] [-B suffix] [-f flags] [-g group] [-m mode]
               [-o owner] file1 ... fileN directory
       install -d [-v] [-g group] [-m mode] [-o owner] directory ...
[florisversteeg@floriss-mbp: ~]% brew install cowsay                      [148]
Warning: cowsay-3.03 already installed
[florisversteeg@floriss-mbp: ~]% cowsay "welkom"                          [148]
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) n
 ________ 
< welkom >
 -------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
[florisversteeg@floriss-mbp: ~]% cowsay "hooi"                            [149]
 ______ 
< hooi >
 ------ 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
[florisversteeg@floriss-mbp: ~]% cowsay -f stegosaurus "ARRGGGGG"         [150]
 __________ 
< ARRGGGGG >
 ---------- 
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
[florisversteeg@floriss-mbp: ~]%                                          [151]
