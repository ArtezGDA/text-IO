Last login: Tue Dec 15 11:34:22 on ttys000
[noamoll@MacBook-Pro-van-Noa: ~]% ls                                       [54]
Algorithmic-Nature/
Applications/
Creative Cloud Files/
Creative Cloud Files (gearchiveerd)/
Creative Cloud Files (vanillies@gmail.com)/
Desktop/
Documents/
Downloads/
Dropbox/
Library/
Movies/
Music/
Pictures/
Public/
pslog.txt
text-IO/
zsh_dotfiles.tar
[noamoll@MacBook-Pro-van-Noa: ~]% cd Documents                             [55]
[noamoll@MacBook-Pro-van-Noa: ~/Documents]% ls                             [56]
01a_basis.html  nona/           random/         werk/
Artez /         pe/             recepten/
[noamoll@MacBook-Pro-van-Noa: ~/Documents]% cd Artez                       [57]
zsh: correct Artez to Artez  ? ([Y]es/[N]o/[E]dit/[A]bort) y
[noamoll@MacBook-Pro-van-Noa: ~/Documents/Artez ]%                         [58]
[noamoll@MacBook-Pro-van-Noa: ~/Documents/Artez ]% ls                      [58]
1ste jaar/         2e jaar/           Testfiles/         zsh_testfiles.tar
[noamoll@MacBook-Pro-van-Noa: ~/Documents/Artez ]% cd testfiles            [59]
[noamoll@MacBook-Pro-van-Noa: Documents/Artez /testfiles]% ls              [60]
april.txt      friday.txt     march.txt      october.txt    thursday.txt
august.txt     january.txt    may.txt        saturday.txt   tuesday.txt
december.txt   july.txt       monday.txt     september.txt  wednesday.txt
february.txt   june.txt       november.txt   sunday.txt
[noamoll@MacBook-Pro-van-Noa: Documents/Artez /testfiles]% mkdir days      [61]
[noamoll@MacBook-Pro-van-Noa: Documents/Artez /testfiles]% ls              [62]
april.txt      february.txt   june.txt       november.txt   sunday.txt
august.txt     friday.txt     march.txt      october.txt    thursday.txt
days/          january.txt    may.txt        saturday.txt   tuesday.txt
december.txt   july.txt       monday.txt     september.txt  wednesday.txt
[noamoll@MacBook-Pro-van-Noa: Documents/Artez /testfiles]% mkdir months    [63]
[noamoll@MacBook-Pro-van-Noa: Documents/Artez /testfiles]% ls              [64]
april.txt      friday.txt     may.txt        saturday.txt   wednesday.txt
august.txt     january.txt    monday.txt     september.txt
days/          july.txt       months/        sunday.txt
december.txt   june.txt       november.txt   thursday.txt
february.txt   march.txt      october.txt    tuesday.txt
[noamoll@MacBook-Pro-van-Noa: Documents/Artez /testfiles]% mv *day.txt Days/
[noamoll@MacBook-Pro-van-Noa: Documents/Artez /testfiles]% ls              [66]
april.txt      december.txt   july.txt       may.txt        october.txt
august.txt     february.txt   june.txt       months/        september.txt
days/          january.txt    march.txt      november.txt
[noamoll@MacBook-Pro-van-Noa: Documents/Artez /testfiles]% mv *month.txt months?
mv: rename *month.txt to months?: No such file or directory
[68]
[noamoll@MacBook-Pro-van-Noa: Documents/Artez /testfiles]%  
