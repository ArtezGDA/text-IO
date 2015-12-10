```
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
==> This script will install:
/usr/local/bin/brew
/usr/local/Library/...
/usr/local/share/man/man1/brew.1

Press RETURN to continue or any other key to abort
==> /usr/bin/sudo /bin/mkdir /usr/local

WARNING: Improper use of the sudo command could lead to data loss
or the deletion of important system files. Please double-check your
typing when using sudo. Type "man sudo" for more information.

To proceed, enter your password, or type Ctrl-C to abort.

Password:
Sorry, try again.
Password:
==> /usr/bin/sudo /bin/chmod g+rwx /usr/local
==> /usr/bin/sudo /usr/sbin/chown Kimberleyterheerdt:admin /usr/local
==> /usr/bin/sudo /bin/mkdir /Library/Caches/Homebrew
==> /usr/bin/sudo /bin/chmod g+rwx /Library/Caches/Homebrew
==> /usr/bin/sudo /usr/sbin/chown Kimberleyterheerdt /Library/Caches/Homebrew
==> Downloading and installing Homebrew...
remote: Counting objects: 3859, done.
remote: Compressing objects: 100% (3705/3705), done.
remote: Total 3859 (delta 41), reused 650 (delta 19), pack-reused 0
Receiving objects: 100% (3859/3859), 3.34 MiB | 1.51 MiB/s, done.
Resolving deltas: 100% (41/41), done.
From https://github.com/Homebrew/homebrew
 * [new branch]      master     -> origin/master
HEAD is now at aeeee75 centralize the logic of handling `homebrew-` in Tap.fetch
==> Installation successful!
==> Next steps
Run `brew help` to get started
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% install brew            [28]
usage: install [-bCcpSsv] [-B suffix] [-f flags] [-g group] [-m mode]
               [-o owner] file1 file2
       install [-bCcpSsv] [-B suffix] [-f flags] [-g group] [-m mode]
               [-o owner] file1 ... fileN directory
       install -d [-v] [-g group] [-m mode] [-o owner] directory ...
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% brew install cowsay     [29]
==> Downloading https://homebrew.bintray.com/bottles/cowsay-3.03.yosemite.bottle
######################################################################### 100.0%
==> Pouring cowsay-3.03.yosemite.bottle.1.tar.gz
🍺  /usr/local/Cellar/cowsay/3.03: 53 files, 228K
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% cowsay "Welcome ladies and gentlemen!"
zsh: correct cowsay to _cowsay ? ([Y]es/[N]o/[E]dit/[A]bort) a
y "Moo"dquote> y "Moo"
dquote> 
dquote> "Moo"
dquote> "        
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% fortune                 [31]
zsh: correct fortune to _fortune ? ([Y]es/[N]o/[E]dit/[A]bort) y
_arguments:comparguments:312: can only be called from completion function
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% brew install fortune    [32]
==> Downloading https://homebrew.bintray.com/bottles/fortune-9708.yosemite.bottl
fortune
######################################################################### 100.0%
==> Pouring fortune-9708.yosemite.bottle.1.tar.gz
🍺  /usr/local/Cellar/fortune/9708: 116 files, 3.6M
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% fortune                 [33]
zsh: correct fortune to _fortune ? ([Y]es/[N]o/[E]dit/[A]bort) y
_arguments:comparguments:312: can only be called from completion function
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]%                         [34]
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% fortune                 [34]
zsh: correct fortune to _fortune ? ([Y]es/[N]o/[E]dit/[A]bort) 
Last login: Thu Dec  3 10:29:54 on ttys007
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% fortune                 [46]
I'll turn over a new leaf.
		-- Miguel de Cervantes
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% cowsay "hoi kimberley"   [47]
 ______________ 
< hoi kimberley >
 -------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% cowsay -f stegosaurus "hoi kimberley"
 ______________ 
< hoi kimberley >
 -------------- 
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
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% cowsay -l               [49]
Cow files in /usr/local/Cellar/cowsay/3.03/share/cows:
beavis.zen bong bud-frogs bunny cheese cower daemon default dragon
dragon-and-cow elephant elephant-in-snake eyes flaming-sheep ghostbusters
head-in hellokitty kiss kitty koala kosh luke-koala meow milk moofasa moose
mutilated ren satanic sheep skeleton small sodomized stegosaurus stimpy
supermilker surgery telebears three-eyes turkey turtle tux udder vader
vader-koala www
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]% cowsay "Welcome ladies and gentlemen!"
dquote> "
 _______________________________ 
< Welcome ladies and gentlemen  >
 ------------------------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
[Kimberleyterheerdt@MacBook-Pro-van-Kimberley: ~]%                         [52]
```
