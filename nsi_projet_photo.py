from PIL import Image
import itertools as tool
import math as m

color_list = ["Rouge", "Vert", "Bleu", "Gris", "Noir Et Blanc", "Miroir", "Pixelisation", "Luminosité", "Color", "Color255"]
file = str(input("Quel fichier utiliser (photo.jpg si vide) ?\n"))
save_name = str(input("Quel nom donner au nouveau fichier (pas de sauvegarde si vide) ?\n"))

if file == "":
    im = Image.open("D:\\NSI Travail\\photo.jpg")
else:
    im = Image.open(f"D:\\NSI Travail\\{file}")

im_copy = im.copy()

def pixel_n(n):
    for x_pixel_n, y_pixel_n in tool.product(range(m.floor(im.width/n)), range(m.floor(im.height/n))):
        RGB = [0,0,0]
        for x_inside, y_inside, rgb_list_value in tool.product(range(n), range(n), range(3)):
            RGB[rgb_list_value] = RGB[rgb_list_value] + im.getpixel((x_pixel_n*n+x_inside, y_pixel_n*n+y_inside))[rgb_list_value]
        for x_inside, y_inside, rgb_list_value in tool.product(range(n), range(n), range(3)):
            im.putpixel((x_pixel_n*n+x_inside, y_pixel_n*n+y_inside), (round(RGB[0]/(n*n)), round(RGB[1]/(n*n)), round(RGB[2]/(n*n))))
        

filter_color = int(input("Voici les filtres disponibles :\n1 – Rouge\n2 – Vert\n3 – Bleu\n4 – Gris\n5 – Noir et Blanc\n6 – Miroir\n7 - Pixelisation\n8 - Luminosité\n9 - Color\n0 - Color512\nQuel filtre choisissez-vous ?\n"))
if filter_color == 9:
    primary_color, k=(input("Choisissez une couleur primaire et une valeur K (Rouge/Vert/Bleu,K).\n")).split(",")
    k = int(k)
elif filter_color == 8:
    luminosity_change = int(input("A quel niveau augmenter(+)/baisser(-) la luminosité de votre image (1-infini) ?\n"))
if filter_color == 7:
    pixel_n(int(input("A quel niveau voulez-vous pixeliser votre image (1-infini) ?\n")))
else:
    for x, y in tool.product(range(im.width),range(im.height)):
        gray_rgb_value = round((im.getpixel((x, y))[0] + im.getpixel((x, y))[1] + im.getpixel((x, y))[2])/3)
        if filter_color == 1:
            im.putpixel((x, y),(im.getpixel((x, y))[0], 0, 0))
        elif filter_color == 2:
            im.putpixel((x, y),(0, im.getpixel((x, y))[1], 0))
        elif filter_color == 3:
            im.putpixel((x, y),(0, 0, im.getpixel((x, y))[2]))
        elif filter_color == 4:
            im.putpixel((x,y),(gray_rgb_value, gray_rgb_value, gray_rgb_value))
        elif filter_color == 5:
            if gray_rgb_value < 128:
                im.putpixel((x,y),(0, 0, 0))
            else:
                im.putpixel((x,y),(255, 255, 255))
        elif filter_color == 6:
            im.putpixel((x,y),(im_copy.getpixel((im.width-x-1, y))[0], im_copy.getpixel((im.width-x-1, y))[1], im_copy.getpixel((im.width-x-1, y))[2]))
        elif filter_color == 8:
            im.putpixel((x,y),(im.getpixel((x,y))[0]+luminosity_change, im.getpixel((x,y))[1]+luminosity_change,im.getpixel((x,y))[2]+luminosity_change))
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

    print(f"Filtre {color_list[filter_color-1]} appliqué")

if save_name != "":
    im.save(f"D:\\NSI Travail\\{save_name}")
else:
    im.show()
