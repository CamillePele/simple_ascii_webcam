import cv2
from PIL import Image
import time


char = [' ', '.', ':', '-', '=', '+', '#', '%', '@']
#char = ['@', '%', '#', '+', '=', '-', ':', '.', ' ']


def ascii_art(img, width = -1):
  img = img.resize( (int(img.size[0]), int(img.size[1] * (7/11))) )
  if width != -1:
    ratio = width / img.size[0]

    img = img.resize( ( int(img.size[0]*ratio), int(img.size[1]*ratio)) )
  #on récupère les dimensions
  largeur,hauteur=img.size
  text = ''
  # On parcourt l'image avec une double boucle
  for y in range(hauteur):
      ligne = ''
      for x in range(largeur):
          pixel=img.getpixel((x,y))
          #chargement des composantes dans des variables
          rouge=pixel[0]
          vert=pixel[1]
          bleu=pixel[2]
          moy = int( (rouge+bleu+vert)/3 )
          # remplissage de la nouvelle image
          ligne += char[ int(moy*len(char)/255)%len(char) ]
      text += ligne + '\n'
  return text

cam = cv2.VideoCapture(0)


while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    print(ascii_art(img, 100))
    time.sleep(.02)


cam.release()