import random
from PIL import Image
import stepic
import exiftool
import piexif
import re
from shutil import copyfile


def defend_stega(img_source,img_dest,password="password"):
    list_method = ['string','exif','stepic']
    method = random.choice(list_method)
    password = 'flag={'+password+'}'
    print(method)
    
    if method == 'string':
        copyfile(img_source, img_dest)
        with open(img_dest, "ab") as f:
            f.write(password.encode('utf8'))

    if method == 'exif':
        im = Image.open(img_source)
        if "exif" in im.info:
            exif_dict = piexif.load(im.info["exif"])
            exif_dict["0th"][piexif.ImageIFD.ImageDescription] = password
            exif_bytes = piexif.dump(exif_dict)
        else:
            exif_bytes = piexif.dump({"0th":{piexif.ImageIFD.ImageDescription:password}})
        im.save(img_dest, exif=exif_bytes)

    if method == 'stepic':
        img = Image.open(img_source)
        img2 = stepic.encode(img,bytes(password, encoding = "utf-8"))
        img2.save(img_dest,'PNG')
        
def attack_stega(img_source,strength):
    list_method = ['string','exif','stepic']
    attacks = random.sample(list_method, strength+1)
    guess = ''
    for attack in attacks:
        if attack == 'string':
            res = ''
            with open(img_source, "rb") as f:
                for chunk in iter(lambda: f.read(8), b''):
                    res += chunk.decode('utf-8', errors="ignore")
            if res.endswith('}'):
                guess = re.split('{|}', res)[-2]

        if attack == 'exif':
            with exiftool.ExifTool() as et:
                metadata = et.get_metadata(img_source)
                if 'EXIF:ImageDescription' in metadata.keys():
                    if 'flag' in metadata['EXIF:ImageDescription']:
                        guess = re.split('{|}', metadata['EXIF:ImageDescription'])[1]

        if attack == 'stepic':
            img = Image.open(img_source)
            result = stepic.decode(img)
            if 'flag' in result:
                guess = re.split('{|}', result)[1]
    return guess

def simulate_attack_stego(attack,img_source = "/home/kali/Documents/projet_3A/gym-idsgame/gym_idsgame/cyber/ressources/test.png",img_dest = "/home/kali/Documents/projet_3A/gym-idsgame/gym_idsgame/cyber/ressources/test_secret.png",password = "password"):
    defend_stega(img_source,img_dest,password)
    guess = attack_stega(img_dest,attack)
    return guess == password