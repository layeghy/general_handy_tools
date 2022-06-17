# renames files of a folder
import os
import re


def fldr_rename(fldr_path):
    file_list = os.listdir(fldr_path)
    for filename in file_list:
        new_filename = file_rename(filename)
        # print(f"old: {filename}\nnew: {new_filename}\n{50*'*'}")
        old_path_name = os.path.join(fldr_path, filename)
        new_path_name = os.path.join(fldr_path, new_filename)
        try:
            os.rename(old_path_name, new_path_name)
        except:
            print(f"{old_path_name} skipped")

        print(f'{old_path_name} is renamed to: {new_path_name}')


def file_rename(filename):
    # remove extra spaces
    filename = " ".join(filename.split())

    remove_list1 = ['PAL.Retail.Rip.DD5.1.NL.Subs', 'LiMiTED.BDRip.x264-LPD', 'TrueHD_7_1_x264-EVO',
                    'NBY_FardaDownload', 'FardaDownload_ir', '-Extratorrentrg', 'Film2serial_ir',
                    'FardaDownload', 'Sonicx-Ukb-Rg', 'SCREENER-P2P', 'filmtoonz_co', 'Film2serial',
                    'AC3-Anarchy', 'Downloadha', 'Film2Media', 'Film2Movie', 'OSCAR DVD', 'Glorytoon',
                    '-WarrLord', 'DXVA-MXMG', 'anoXmous', 'Warrlord', 'MkvCage', 'Dts-Waf', 'Mrmovie',
                    '-Fuzion', 'Cropped', 'Sujaidr', 'Full_HD', 'ILPruny', '2Dooble', 'WEBRip', 'Dubble',
                    'French', 'DVDRip', 'Ganool', 'Dubbed', 'PROPER', 'Dvdscr', 'BluRay', 'Melite', 'Refill',
                    'Truehd', 'RMTeam', 'WEB-DL', 'XViD-', 'Atmos', '10Bit', 'x265-', 'HDRip', 'x264-', 'Farsi',
                    '1080p', '-VLiS', 'BDRip', ' ENG ', 'BRRip', 'RARBG', '-aXXo', 'Hexdl', 'HDDVD', 'AAC5',
                    'x265', 'x264', 'BTRG', '-Psa', 'ETRG', 'Bozx', 'XViD', 'M99M', '720p', 'YIFY', 'HEVC',
                    '7Evo', '-EVO', '-Fxg', 'BHRG', 'AAC-', 'AAC', ' - ', '5.1', '( )', 'www', 'com', 'Yts',
                    'ORG', '_1_', '8Ch', '6CH', '_1-', 'DD5', 'Ac3', '()']

    filename = filename.upper()
    for r in remove_list1:
        filename = filename.replace(r.upper(), "")
    filename = filename.title()

    if ('[' in filename) or (']' in filename):
        if re.search('\[(.*?)\]', filename) is not None:
            to_remove_list = re.findall('\[(.*?)\]', filename)
            for to_remove in to_remove_list:
                if not to_remove.isnumeric():
                    filename = filename.replace("[" + to_remove + "]", "").strip()
                else:
                    filename = filename.replace("[" + to_remove + "]", "(" + to_remove + ")").strip()

    if '.' in filename:
        filename = " ".join(filename.split("."))

    if '_' in filename:
        filename = " ".join(filename.split("_"))

    filename = " ".join(filename.split())
    if filename.split(" ")[-1].isnumeric():
        last_part = filename.split(" ")[-1]
        last_part = "(" + last_part + ")"
        filename = " ".join(filename.split(" ")[:-1] + [last_part])

    remove_list2 = ["( )", "()"]
    for r in remove_list2:
        filename = filename.replace(r, "")

    if filename[-1] == "-":
        filename = filename[:-1]
        filename = file_rename(filename)

    return filename


if __name__ == '__main__':
    path = 'D:/Movie'
    sub_fldr_list = os.listdir(path)
    for sub_fldr in sub_fldr_list:
        sub_fldr_path = os.path.join(path, sub_fldr)
        fldr_rename(sub_fldr_path)
