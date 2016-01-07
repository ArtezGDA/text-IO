#!/usr/bin/env python
# encoding: utf-8

# dit gedeelte zorgt ervoor dat stdout, stderr = subprocess.Popen werkt.
import subprocess

# tussen word = "" kun je de tekst typen die de koe moet uitspreken.
# cowsay staat voor een koe, maar als je een ander karakter wilt zul je de code moeten aanpassen.
# van 'cowsay', naar 'cowsay' '-f' 'hier komt de naam van je karakter'

word="In de hal van kasteel Elseneur."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Stil nu! De schone Ophelia! Nimf, gedenk in uw gebeden al mijn zonden."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Edele heer, hoe gaat het u de laatste tijd?"
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Ik dank u heel goed."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Ik heb nog souvenirs van u, die ik al lang terug had willen geven. Hier... neemt u ze."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Nee, nee, ik niet ik heb u nimmer iets gegeven."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="U weet heel goed, heer, dat u 't wel gedaan hebt, en met zó zoete woorden dat hun waarde nog groter werd. Hun geur is nu vervlogen, neem ze dus terug; want voor een edele geest verbleekt de rijkste gift wanneer de gever zich arm aan liefde toont. Hier zijn ze, heer."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Aha! ben je kuis?"
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Heer"
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Ben je mooi?"
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Wat bedoelt uwe hoogheid?"
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Dat als je kuis en mooi bent, je kuisheid geen omgang met je schoonheid zou mogen toestaan."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Maar, heer, kan schoonheid ooit beter omgang hebben dan met kuisheid?"
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Jazeker, want de macht van de schoonheid zal de kuisheid eer der in een koppelaarster veranderen, dan dat kuisheid de schoonheid dwingen kan haar te gelijken. Dit was vroeger een paradox, maar nu wordt het door de tijd bewezen. Ik heb je eens liefgehad."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Ja, heer, dat hebt u me doen geloven."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Je had me niet moeten geloven, want de deugd kan niet zó geënt worden op onze oude stam, dat er geen zweem van overblijft. Ik heb je niet liefgehad."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Dan ben ik des te meer bedrogen."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Ga in een klooster! Waarom zou je zondaars fokken? Ik mag wel zeggen dat ik vrij deugdzaam ben, maar toch zou ik me kunnen beschuldigen van dingen waarom mijn moeder me beter niet had kunnen baren. Ik ben erg hoogmoedig, wraak zuchtig en eergierig, en ik heb meer wandaden voor 't grijpen dan gedachten om ze uit te drukken, verbeelding om ze vorm te geven of tijd om ze te begaan. Wat moeten kerels als ik ook rond kruipen tussen hemel en aarde? Wij zijn aartsschavuiten geloof niemand van ons. Maak dat je in een klooster komt! Waar is je vader?"
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Thuis, heer."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Laat dan de deuren achter hem dichtdoen, opdat hij nergens anders voor gek kan spelen dan in zijn eigen huis. Vaarwel."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="0 hemelse goedheid, help hem! "
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Mocht je trouwen, dan geef ik je deze vloek als bruidsschat mee, je kunt zo kuis als ijs, zo zuiver als sneeuw zijn, tóch ontkom je niet aan de laster. Ga in een klooster! Vaarwel. Of als je met alle geweld trouwen wilt, trouw dan een idioot, want mannen met hersens weten te goed wat voor monsters je van hen maakt. Naar een klooster en gauw! Vaarwel."
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Ik weet maar al te goed hoe jullie je beschildert. God heeft je een gezicht gegeven, maar jullie maakt je een ander. Je huppelt en trippelt, je geeft Gods schepselen bijnamen en laat je wulpsheid doorgaan voor argeloosheid. Ga weg, ik wil er niets meer van weten het heeft me gek gemaakt. Ik zeg je, dat er geen huwelijken meer moeten komen. De getrouwden mogen blijven leven op één na - en de ongetrouwden moeten blijven zoals ze zijn. Naar een klooster! Ga! "
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()

word="Wat een edele geest is hier verscheurd! Oog, tong en zwaard van hoveling, geleerde en krijgsman, hoop en bloem van onze staat, spiegel der zeden, toonbeeld van beschaving, door eerbetoon omringd... voorgoed verloren. En ik, rampzaligste van alle vrouwen, die honing zoog uit zijn welluidend woord, hoor nu de tonen van dat helder brein verward en schril als een ontstemde beiaard, en zie het ongeëvenaarde beeld van bloesemende jeugd, verdord door waanzin. 0, wee mij, die gezien heeft wat ik zag, zie wat ik zie!"
stdout, stderr = subprocess.Popen(
                     ['cowsay', word]).communicate()


def main():
       """ Hiermee opent u de script bestanden en print u de conversatie. """
       #roep de python bestand op en voert het uit, met de juiste cowfile.
       
       py = conversation.py
       print conversation.py #print conversatie uit script bestand
       
#if __name__ == '__main__':
#       main()


#def main():
#       word = .communicate()
#       stdout, stderr = subprocess.Popen(
 #                    ['cowsay', word]).communicate()

#if __name__ == '__main__':
#      main()