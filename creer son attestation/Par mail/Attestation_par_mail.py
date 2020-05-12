# ###################################
# Help
import datetime
from time import strftime
from time import gmtime, strftime

import time

import qrcode

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import mimetypes
import email.mime.application

box='box.png'
vbox='vbox.png'
sibox='signature.png'
qrpng='qrcode.png'
pbox = box
dbox = box
tbox = box
qbox = box
cbox = box
sbox = box
ssbox = box
motif=''

date = datetime.datetime.now()
print(date)
print(' ')
print('Réalisé par Gugus le Pingouin#0547 (Gugus le Pangolin)')
print('Pour toute réclamation ou question, veuillez me contacter via : attestation.py@gmail.com')
print(' ')
print(' ')
mail=''#à renseigner, uniquement en gmail
nom=''
prenom=''
datenaissance=''# format jj/mm/aaaa
lieunaissance=''#lieu de naissance
residence=''
codepostal=''
ville=''
date = datetime.datetime.now()
str(date)
dateyear = str(date.year)
datehourr=date.hour
datehour=str(date.hour)
datemnn = date.minute + 1


if datemnn == 60 :
    datemnn=0
else:
    datemnn=datemn

if datemnn==0:
    datehourr=datehourr+1
else:
    datehourr=datehourr
	
if datemnn == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
    datemnn=str(datemnn).zfill(2)
else:
    datemnn=str(datemnn)

if datehourr == 24:
    datehourr=0
else:
    datehourr=datehourr


datemnn=str(datemnn)
minute = date.minute
datehourr=str(datehourr)

dayy= date.day

monthh = date.month 

if minute == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
    datemn=str(minute).zfill(2)
else:
    datemn=str(minute)

if dayy == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
    dateday= str(dayy).zfill(2)
else:
    dateday= str(dayy)

if monthh == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
    datemonth= str(monthh).zfill(2)
else:
    datemonth= str(monthh)





    
################################## Bloc pouvant être supprimé pour éviter de choisir ##########################

print('')
print('Que devez vous faire ?')
print('')
time.sleep(.500)
print('1 > Déplacements entre le domicile et le lieu d’exercice de l’activité professionnelle,')
print('lorsqu’ils sont indispensables à l’exercice d’activités ne pouvant être organisées sous')
print('forme de télétravail ou déplacements professionnels ne pouvant être différés (2)')
print('')
time.sleep(.500)
print('2 > Déplacements pour effectuer des achats de fournitures nécessaires à l’activité')
print('professionnelle et des achats de première nécessité (3) dans des établissements dont les')
print('activités demeurent autorisées (liste sur gouvernement.fr).')
time.sleep(.500)
print('')
print('3 > Consultations et soins ne pouvant être assurés à distance et ne pouvant être différés ;')
print('consultations et soins des patients atteints d\'une affection de longue durée.')
time.sleep(.500)
print('')
print('4 > Déplacements pour motif familial impérieux, pour l’assistance aux personnes')
print('vulnérables ou la garde d’enfants.')
time.sleep(.500)
print('')
print('5 > Déplacements brefs, dans la limite d\'une heure quotidienne et dans un rayon maximal')
print('d\'un kilomètre autour du domicile, liés soit à l\'activité physique individuelle des',)
print('personnes, à l\'exclusion de toute pratique sportive collective et de toute proximité avec',)
print('d\'autres personnes, soit à la promenade avec les seules personnes regroupées dans un',)
print('même domicile, soit aux besoins des animaux de compagnie.')
print('')
time.sleep(.500)
print('6 > Convocation judiciaire ou administrative.')
print('')
time.sleep(.500)
print('7 > Participation à des missions d’intérêt général sur demande de l’autorité administrative.')
print('')
time.sleep(.500)
choix = int(input('Entrer le n° de votre choix [Ex : Convocation judiciaire ou administrative. = 6] : '))

print('Votre choix est donc le n°',choix)
time.sleep(1)

#################################################################################################################



# si vous voulez eviter de choisir, enlever la partie au dessus et mettez enlever le # dessous
# et changez votrechoix par 1/2/3/4/5/6/7 en fonction de votre activité


#choix=votrechoix

if choix ==1 :
    pbox = vbox
    motif='travail'
elif choix ==2 :
    dbox = vbox
    motif='courses'
elif choix ==3 :
    tbox = vbox
    motif='sante'
elif choix ==4 :
    qbox = vbox
    motif='famille'
elif choix ==5 :
    cbox = vbox
    motif='sport'
elif choix ==6 :
    sbox = vbox
    motif='judiciaire'
elif choix ==7 :
    ssbox = vbox
    motif='missions'
else:
    print('Erreur')


# ###################################
# Content
fileName = 'Attestation.pdf'
documentTitle = 'dérogation'
title = 'ATTESTATION DE DÉPLACEMENT DÉROGATOIRE'
subTitle = 'En application de l’article 3 du décret du 23 mars 2020 prescrivant les mesures générales' 
subtitle = 'nécessaires pour faire face à l’épidémie de Covid19 dans le cadre de l’état d’urgence sanitaire'

textLines = [
'',
'',
'Je soussigné(e),',
'',
'Mme / M. : '+prenom+' '+nom,
'',
'Né(e) le : '+datenaissance,
'',
'À : '+lieunaissance,
'',
'Demeurant : '+residence+' '+codepostal+' '+ville,
'',

'certifie que mon déplacement est lié au motif suivant (cocher la case) autorisé',
'par l’article 3 du décret du 23 mars 2020 prescrivant les mesures générales',
'nécessaires pour faire face à l’épidémie de Covid19 dans le cadre de ',
'l’état d’urgence sanitaire (1) : ',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'Fait à : '+ville,
'',
'Le : ' +dateday +'/' +datemonth +'/' +dateyear +'      à     ' +datehour +'H'+datemn,
'(Date et heure de début de sortie à mentionner obligatoirement)',
'',
#'Signature :',
'',
]


textLines2 = [

'Déplacements entre le domicile et le lieu d’exercice de l’activité professionnelle,',
'lorsqu’ils sont indispensables à l’exercice d’activités ne pouvant être organisées sous',
'forme de télétravail ou déplacements professionnels ne pouvant être différés (2)',
'',
'Déplacements pour effectuer des achats de fournitures nécessaires à l’activité',
'professionnelle et des achats de première nécessité (3) dans des établissements dont les',
'activités demeurent autorisées (liste sur gouvernement.fr).',
'',
'Consultations et soins ne pouvant être assurés à distance et ne pouvant être différés ;',
'consultations et soins des patients atteints d\'une affection de longue durée.',
'',
'Déplacements pour motif familial impérieux, pour l’assistance aux personnes',
'vulnérables ou la garde d’enfants.',
'',
'Déplacements brefs, dans la limite d\'une heure quotidienne et dans un rayon maximal',
'd\'un kilomètre autour du domicile, liés soit à l\'activité physique individuelle des',
'personnes, à l\'exclusion de toute pratique sportive collective et de toute proximité avec',
'd\'autres personnes, soit à la promenade avec les seules personnes regroupées dans un',
'même domicile, soit aux besoins des animaux de compagnie.',
'',
'Convocation judiciaire ou administrative.',
'',
'',
'Participation à des missions d’intérêt général sur demande de l’autorité administrative.',
]

textLines3 = [
'Date de création:',
dateday +'/' +datemonth +'/' +dateyear +' à ' +datehourr +'H'+datemnn,
]



Textlines = [
'1 Les personnes souhaitant bénéficier de l\'une de ces exceptions doivent se munir s’il y a lieu, lors de leurs',
'd\'un document leur permettant de justifier que le déplacement considéré entre',
'dans le champ de l\'une de ces exceptions.',
'2 A utiliser par les travailleurs non-salariés,',
'lorsqu’ils ne peuvent disposer d’un justificatif de déplacement établi par leur employeur.',
'3 Y compris les acquisitions à titre gratuit (distribution de denrées alimentaires…) et les déplacements liés à la',
'perception de prestations sociales et au retrait d’espèces.',
]


box = 'box.png'

vbox = 'vbox.png'

sibox = 'signature.png'

qrpng = 'qrcode.png'


# ###################################
# 0) Create document 
from reportlab.pdfgen import canvas 

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)



# ###################################
# 1) Title :: Set fonts 
# # Print available fonts
# for font in pdf.getAvailableFonts():
#     print(font)

# Register a new font
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('abc', 'Arial.ttf')
)
pdf.setFont('abc', 16)
pdf.drawCentredString(300, 780, title)









# ###################################
# 2) Sub Title 
# RGB - Red Green and Blue
pdf.setFillColorRGB(0, 0, 0)
pdf.setFont("Helvetica-Bold", 10)
pdf.drawCentredString(300,760, subTitle)



pdf.setFillColorRGB(0, 0, 0)
pdf.setFont("Helvetica-Bold", 10)
pdf.drawCentredString(300,750, subtitle)

# ###################################
# 3) Draw a line
##pdf.line(30, 710, 550, 710)


qrrr='Cree le: '+dateday+'/'+datemonth+'/'+dateyear+' a '+datehourr+'h'+datemnn+'; Nom: '+nom+'; Prenom: '+prenom+'; Naissance: '+datenaissance+' a '+lieunaissance+'; Adresse: '+residence+' '+codepostal+' '+ville+'; Sortie: '+dateday+'/'+datemonth+'/'+dateyear+' a '+datehour+'h'+datemn+'; Motifs: '+motif
print(str(qrrr))
img = qrcode.make(qrrr)
img.save('qrcode.png')



# ###################################
# 4) Text object :: for large amounts of text
from reportlab.lib import colors

text = pdf.beginText(65, 740)
text.setFont("Helvetica", 11)
text.setFillColor(colors.black)
for line in textLines:
    text.textLine(line)

pdf.drawText(text)


Text = pdf.beginText(65, 70)
Text.setFont("Helvetica", 8)
Text.setFillColor(colors.black)
for line in Textlines:
    Text.textLines(line)

pdf.drawText(Text)

Text2 = pdf.beginText(100, 515)
Text2.setFont("Helvetica", 11)
Text2.setFillColor(colors.black)
for line in textLines2:
    Text2.textLines(line)

pdf.drawText(Text2)


Text3 = pdf.beginText(460, 85)
Text3.setFont("Helvetica", 7)
Text3.setFillColor(colors.black)
for line in textLines3:
    Text3.textLines(line)

pdf.drawText(Text3)


# ###################################
# 5) Draw image
            
#pdf.drawInlineImage(sig, 200, 100, width=63, height=20)
            
pdf.drawInlineImage(pbox, 65, 495, width=20, height=20)
pdf.drawInlineImage(dbox, 65, 445, width=20, height=20)
pdf.drawInlineImage(tbox, 65, 398, width=20, height=20)
pdf.drawInlineImage(qbox, 65, 358, width=20, height=20)
pdf.drawInlineImage(cbox, 65, 298, width=20, height=20)
pdf.drawInlineImage(sbox, 65, 245, width=20, height=20)
pdf.drawInlineImage(ssbox, 65, 205, width=20, height=20)
pdf.drawInlineImage(qrpng, 425, 90, width=120, height=120)
pdf.save()

print('Attestation crée')
time.sleep(.500)

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
s = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
s.login('votremail@gmail.com','password')
#rentrez ici votre mail et votre password, mais veuillez d'abord désactiver la sécurité sur google (sinon ça ne marchera pas) compte -> securité -> Accès moins sécurisé des applications -> activer

msg = MIMEMultipart()
msg['Subject'] = 'Votre attestation'
msg['From'] = 'votremail@gmail.com'
msg['To'] = mail #destinataire

txt = MIMEText('Veuillez trouver ci-joint votre attestion et votre qrcode')#changez le texte comme bon vous semble
msg.attach(txt)

filename = 'Attestation.pdf' #path to file
fo=open(filename,'rb')
attach = email.mime.application.MIMEApplication(fo.read(),_subtype="pdf")
fo.close()
attach.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(attach)

filename = 'qrcode.png' #path to file
fo=open(filename,'rb')
attach = email.mime.application.MIMEApplication(fo.read(),_subtype="png")
fo.close()
attach.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(attach)
s.send_message(msg)
s.quit()
print('Attestation envoyé par mail à',mail)
print('Merci de vérifier que votremail@gmail.com n\'est pas en spam')#changez par votre mail
time.sleep(5)
