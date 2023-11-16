from PIL import Image
import itertools as tool
import math as m
import os

os.system('cls')
percentage_save = 0
filter_list = ["Rouge", "Vert", "Bleu", "Gris", "Noir & Blanc", "Miroir", "Pixelisation", "Luminosité", "Color", "Color255"]
file = str(input("Quel fichier utiliser (photo.jpg si vide) ?\n"))
os.system('cls')
save_name = str(input("Quel nom donner au nouveau fichier (pas de sauvegarde si vide) ?\n"))
os.system('cls')

if file == "":
    im = Image.open("./photo.jpg")
else:
    im = Image.open(f"./{file}")
    
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

def luminosity_change(lum_change):
    for x, y in tool.product(range(im.width), range(im.height)):
        im.putpixel((x,y),(im.getpixel((x,y))[0]+lum_change, im.getpixel((x,y))[1]+lum_change,im.getpixel((x,y))[2]+lum_change))

def color_k():
    primary_color, k=(input("Choisissez une couleur primaire et une valeur K (0-Rouge/1-Vert/2-Bleu,K).\n")).split(",")
    primary_color,k = int(primary_color),int(k)
    if primary_color not in[0,1,2]:
        print("invalid primary color value")
        exit()
    for x, y in tool.product(range(im.width), range(im.height)):
        save_color_list = [round(im.getpixel((x,y))[0]-(k/2)), round(im.getpixel((x,y))[1]-(k/2)), round(im.getpixel((x,y))[2]-(k/2))]
        save_color_list[primary_color] = im.getpixel((x,y))[primary_color]+k
        im.putpixel((x,y),(save_color_list[0],save_color_list[1],save_color_list[2]))
        
def color_255():
    for x, y in tool.product(range(im.width),range(im.height)):
        im.putpixel((x,y),(m.floor(im.getpixel((x,y))[0]/31.875)*32,m.floor(im.getpixel((x,y))[1]/31.875)*32,m.floor(im.getpixel((x,y))[2]/31.875)*32))

def special_change(n):
    for x, y in tool.product(range(im.width), range(im.height)):
        save_color_list = [0 ,0 ,0]
        save_color_list[n] = 255-im.getpixel((x,y))[n]
        im.putpixel((x,y),(save_color_list[0],save_color_list[1],save_color_list[2]))

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
elif filter_color == 8:
    color_k()
elif filter_color == 9:
    color_255()
elif filter_color in [10, 20, 30]:
    special_change(int(fliter_color/10))
else:
    print('invalid filter')
    exit()
    
os.system('clear')
print(f"Filtre {filter_list[filter_color]} appliqué")

if save_name != "":
    im.save(f"./{save_name}")
else:
    im.show()