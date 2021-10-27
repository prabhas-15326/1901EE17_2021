import os
import re


def Breaking_bad(season_padding, episode_padding):
    # Accessing to Breaking Bad folder
    folder = os.listdir(".\\wrong_srt\\Breaking Bad")
    files = []
    # appending all the files in breaking bad to files list
    for file in folder:
        files.append(file)

    for file in range(0, len(files)):
        # storing files[file] in str1
        str1 = files[file]
        # removing unneccessary symbols from the file
        re_name = re.split("[ \.]", str1)
        del re_name[3:6]  # deleting unnecessary words
        s_e = re_name[2]  # storing season and episode word in s_e
        pattern = re.compile(r'\d+')
        s = re.findall(pattern, s_e)
        season = s[0]
        episode = s[1]
        full_name = re_name[0]+" "+re_name[1]+" "+"season"+str(season).zfill(
            season_padding)+" "+"episode"+str(episode).zfill(episode_padding)+"."+re_name[3]  # renaming the file
        os.rename(".\\wrong_srt\\Breaking Bad"+"\\" +
                  files[file], ".\\wrong_srt\\Breaking Bad"+"\\"+full_name)
        # storing the new renamed files in Breaking Bad
        path = "corrected_srt\\Breaking bad"
        with open(os.path.join(path, full_name), 'w') as fp:
            pass


def Game_Of_Thrones(season_padding, episode_padding):
    # Accessing to Game of Thrones folder
    folder = os.listdir(".\\wrong_srt\\Game of Thrones")
    files = []
    # appending all the files in Game of Thrones to files list
    for file in folder:
        files.append(file)
    for file in range(0, len(files)):
        # storing files[file] in str1
        str1 = files[file]
        # removing unneccessary symbols from the file
        re_name = re.split("[-\.]", str1)
        del re_name[3:7]  # deleting unnecessary words
        s_e = re_name[1]  # storing season and episode word in s_e
        pattern = re.compile(r'\d+')
        s = re.findall(pattern, s_e)
        season = s[0]
        episode = s[1]
        full_name = re_name[0]+" "+"-"+" "+"Season"+str(season).zfill(season_padding)+" "+"Episode"+str(
            episode).zfill(episode_padding)+" "+"-"+" "+re_name[2]+"."+re_name[3]  # renaming the file
        os.rename(".\\wrong_srt\\Game of Thrones"+"\\" +
                  files[file], ".\\wrong_srt\\Game of Thrones"+"\\"+full_name)
        # storing the new renamed files in Game of Thrones
        path = "corrected_srt\\Game of Thrones"
        with open(os.path.join(path, full_name), 'w') as fp:
            pass


def Lucifer(season_padding, episode_padding):
    # Accessing to Lucifer folder
    folder = os.listdir(".\\wrong_srt\\Lucifer")
    files = []
    # appending all the files in Lucifer to files list
    for file in folder:
        files.append(file)
    for file in range(0, len(files)):
        # storing files[file] in str1
        str1 = files[file]
        # removing unneccessary symbols from the file
        re_name = re.split("[-\.]", str1)
        del re_name[3:6]  # deleting unnecessary words
        s_e = re_name[1]  # storing season and episode word in s_e
        pattern = re.compile(r'\d+')
        s = re.findall(pattern, s_e)
        season = s[0]
        episode = s[1]
        full_name = re_name[0]+" "+"-"+" "+"Season"+str(season).zfill(season_padding)+" "+"Episode"+str(
            episode).zfill(episode_padding)+" "+"-"+" "+re_name[2]+"."+re_name[3]  # renaming the file
        os.rename(".\\wrong_srt\\Lucifer"+"\\" +
                  files[file], ".\\wrong_srt\\Lucifer"+"\\"+full_name)
        path = "corrected_srt\\Lucifer"
        # storing the new renamed files in Lucifer
        with open(os.path.join(path, full_name), 'w') as fp:
            pass


def regex_renamer():
    # Taking input from the user
    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")

    webseries_num = int(
        input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))

    # creating corrected_srt folders
    if not os.path.exists("corrected_srt"):
        path = "corrected_srt"
        os.mkdir(path)

    if webseries_num == 1:
        # creating Breaking Bad folder
        path = "corrected_srt\\Breaking Bad"
        os.mkdir(path)
        Breaking_bad(season_padding, episode_padding)
    elif webseries_num == 2:
        # creating Game Of Thrones folder
        path = "corrected_srt\\Game Of Thrones"
        os.mkdir(path)
        Game_Of_Thrones(season_padding, episode_padding)
    elif webseries_num == 3:
        # creating Lucifer folder
        path = "corrected_srt\\Lucifer"
        os.mkdir(path)
        Lucifer(season_padding, episode_padding)
    else:
        print("Enter above mentioned Web series")


regex_renamer()
