from PIL import Image
from os import *
import itertools as tool
import math as m
system('clear')

filter_list = ["Rouge", "Vert", "Bleu", "Gris", "Noir Et Blanc", "Miroir", "Pixelisation", "Luminosité", "Color", "Color255"]
file = str(input("Quel fichier utiliser (photo.jpg si vide) ?\n"))
system('clear')
save_name = str(input("Quel nom donner au nouveau fichier (pas de sauvegarde si vide) ?\n"))
system('clear')

if file == "":
    im = Image.open("/home/c1g5/alexandre.loubet/Bureau/alexandre.loubet/Travail/Projets NSI/Projet Photo/photo.jpg")
else:
    im = Image.open(f"/home/c1g5/alexandre.loubet/Bureau/alexandre.loubet/Travail/Projets NSI/Projet Photo/{file}")

def color_change():
    for x, y in tool.product(range(im.width), range(im.height)):
        save_color_list = [0 ,0 ,0]
        save_color_list[filter_color] = im.getpixel((x,y))[filter_color]
        im.putpixel((x,y),(save_color_list[0],save_color_list[1],save_color_list[2]))

def gray_change():
    for x, y in tool.product(range(im.width), range(im.height)):
        gray_rgb_value = round((im.getpixel((x, y))[0] + im.getpixel((x, y))[1] + im.getpixel((x, y))[2])/3)
        im.putpixel((x,y), (gray_rgb_value, gray_rgb_value, gray_rgb_value))

def white_and_black():
    for x, y in tool.product(range(im.width), range(im.height)):
        gray_rgb_value = round((im.getpixel((x, y))[0] + im.getpixel((x, y))[1] + im.getpixel((x, y))[2])/3)
        im.putpixel((x,y),(m.floor(gray_rgb_value/128)*255,m.floor(gray_rgb_value/128)*255,m.floor(gray_rgb_value/128)*255))

def mirror():
    im_copy = im.copy()
    for x,y in tool.product(range(im.width), range(im.height)):
        im.putpixel((x,y),(im_copy.getpixel((im.width-x-1, y))[0], im_copy.getpixel((im.width-x-1, y))[1], im_copy.getpixel((im.width-x-1, y))[2]))

def pixel_n(n):
    for x_pixel_n, y_pixel_n in tool.product(range(m.floor(im.width/n)), range(m.floor(im.height/n))):
        RGB = [0,0,0]
        for x_inside, y_inside, rgb_list_value in tool.product(range(n), range(n), range(3)):
            RGB[rgb_list_value] = RGB[rgb_list_value] + im.getpixel((x_pixel_n*n+x_inside, y_pixel_n*n+y_inside))[rgb_list_value]
        for x_inside, y_inside, rgb_list_value in tool.product(range(n), range(n), range(3)):
            im.putpixel((x_pixel_n*n+x_inside, y_pixel_n*n+y_inside), (round(RGB[0]/(n*n)), round(RGB[1]/(n*n)), round(RGB[2]/(n*n))))

def luminosity_change():
    for x, y in (range(im.width), range(im.height)):
        im.putpixel((x,y),(im.getpixel((x,y))[0]+luminosity_change, im.getpixel((x,y))[1]+luminosity_change,im.getpixel((x,y))[2]+luminosity_change))

print("Voici les filtres disponibles :")
for number_filter, filter in enumerate(filter_list):
    print(f'{number_filter} - {filter}')
filter_color = int(input("Quel filtre choisissez-vous ?\n"))



if filter_color in [0, 1, 2]:
    color_change()
elif filter_color == 3:
    gray_change()
elif filter_color == 4:
    white_and_black()
elif filter_color == 5:
    mirror()
elif filter_color == 6:
    pixel_n(int(input("A quel niveau voulez-vous pixeliser votre image (1-infini) ?\n")))
elif filter_color == 7:
    luminosity_change(int(input("A quel niveau augmenter(+)/baisser(-) la luminosité de votre image (1-infini) ?\n")))

if filter_color == 9:
    primary_color, k=(input("Choisissez une couleur primaire et une valeur K (Rouge/Vert/Bleu,K).\n")).split(",")
    k = int(k)
else:
    for x, y in tool.product(range(im.width),range(im.height)):
        elif filter_color == 9:
            if primary_color.lower() == "rouge":
                im.putpixel((x,y),(im.getpixel((x,y))[0]+k, round(im.getpixel((x,y))[1]-(k/2)), round(im.getpixel((x,y))[2]-(k/2))))
            elif primary_color.lower() == "vert":
                im.putpixel((x,y),(round(im.getpixel((x,y))[0]-(k/2)), im.getpixel((x,y))[1]+k, round(im.getpixel((x,y))[2]-(k/2))))
            elif primary_color.lower() == "bleu":
                im.putpixel((x,y),(round(im.getpixel((x,y))[0]-(k/2)), round(im.getpixel((x,y))[1]-(k/2)), im.getpixel((x,y))[2]+k))
            else:
                print("error")
        elif filter_color == 0:
            im.putpixel((x,y),(m.floor(im.getpixel((x,y))[0]/31.875)*32,m.floor(im.getpixel((x,y))[1]/31.875)*32,m.floor(im.getpixel((x,y))[2]/31.875)*32))
        else:
            print("error")
            exit()
    system('clear')
    print(f"Filtre {filter_list[filter_color-1]} appliqué")







if save_name != "":
    im.save(f"/home/c1g5/alexandre.loubet/Bureau/alexandre.loubet/Travail/Projets NSI/Projet Photo/{save_name}")
else:
    im.show()
