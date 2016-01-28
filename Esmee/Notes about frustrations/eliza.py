# simple, slow eliza in bash

#Script started on Wed Apr 30 12:38:14 1997
#sh-2.00$ cat frock
#echo "WELCOME TO DR. FROCK'S COUCH", 
while [ "1" = "1" ]
do
read line
line=`echo $line | tr "[a-z]" "[A-Z]" |
     sed 's/^/ /; s/$/ /; s/\./ /g
     s/ I / i /g; s/ YOU ARE/ you are/g; s/ AM / am /g; s/ ME / me /g
     s/ YOU / you /g
     s/ MY / my /g; s/ YOUR / your /g; s/ MINE / mine /g; s/ ARE / are /g
     s/ me / YOU /g; s/ my / YOUR /g; s/ your / DR. FROCKS /g;
     s/ i / YOU /g; s/ am / ARE /g;s/ mine / YOURS /g; s/ are / IS /; s/ you / DR. FROCK /
     s/^ //; s/ $//'`
echo "$line"
case "$line" in
   *YOU\ ARE\ *)  echo "`echo $line |
           sed 's/^.*YOU\ ARE/WHY DO YOU THINK YOU ARE/' `?" ;;
   *YOU\ HAVE\ *) echo "`echo $line | 
           sed 's/^.*YOU\ HAVE/HOW LONG HAVE YOU HAD/'`?" ;;
   YOU*) echo "WHEN DID YOU FIRST REALIZE THAT $line?" ;;
   *BECAUSE*) echo "IS THAT REALLY THE REASON?";;
   *DO\ DR.\ SPOCK\ THINK*) echo "CAN YOU ANSWER THAT YOURSELF?";;
   GO*|EAT*|TRY*|HELP*|PUT*) echo "WHY DO YOU WANT ME TO $line?";;
   YES*) echo "HOW CAN YOU BE SURE?";;
   NO*) echo "TRY NOT TO BE SO NEGATIVE.";;
 *MOTHER*|*FATHER*|*BROTHER*|*SISTER*) echo "TELL ME MORE ABOUT YOUR FAMILY.";;
   WHY*|WHO*|WHAT*|HOW*) echo "YOU TELL ME `echo $line | sed s/?/./g`";;
   QUIT) exit;;
   *) echo "WHY DO YOU SAY $line?";;
esac
done

sh-2.00$ frock
WELCOME TO DR. FROCK'S COUCH
hello
HELLO
WHY DO YOU SAY HELLO?
i am just trying to be friendly
YOU ARE JUST TRYING TO BE FRIENDLY
WHY DO YOU THINK YOU ARE JUST TRYING TO BE FRIENDLY?
why are you so arrogant?
WHY IS DR. FROCK SO ARROGANT?
YOU TELL ME WHY IS DR. FROCK SO ARROGANT.
you are just a machine
DR. FROCK IS JUST A MACHINE
WHY DO YOU SAY DR. FROCK IS JUST A MACHINE?
your responses are stupid
DR. FROCKS RESPONSES IS STUPID
WHY DO YOU SAY DR. FROCKS RESPONSES IS STUPID?
i am getting very angry
YOU ARE GETTING VERY ANGRY
WHY DO YOU THINK YOU ARE GETTING VERY ANGRY?
quit
QUIT
sh-2.00$ exit
exit

script done on Wed Apr 30 12:39:39 1997