# -*- coding: utf-8 -*-
# The spleeter runs on python 3.7 only....😑

# Using AI to split songs to multiple sources/channels

import subprocess
import os
from os import path

Executable = 'ffmpeg.exe'


def convert_mp3_to_wav(audio_):
    if audio_.endswith('.mp3'):
        cmd = Executable + ' -i ' + audio_ + ' ' + audio_[:-4] + '_.wav'
        subprocess.call(cmd, shell=True)
        print("Converting audio file [mp3->wav] completed..")
        return audio_[:-4]+'_.wav'
    else:
        return audio_


def get_stems(ouput, audio_file):
    print("Processing ", audio_file)
    # Help command -- os.system('spleeter separate -h')

    os.system('spleeter separate -i ' + audio_file + ' -p spleeter:4stems -o' + ouput)
    print(audio_file, " split successful\n")


if __name__ == '__main__':
    file1 = input("Enter path to audio file: ")
    if not path.exists(file1):
        print("Invalid path")
        exit()
    else:
        audio_file = convert_mp3_to_wav(file1)
        output = input("Enter path to save output split audio files: ")
        if path.exists(output):
            get_stems(output, audio_file)
        else:
            print("Invalid path")
            exit()

    # Use Audacity to play different parts of the song
