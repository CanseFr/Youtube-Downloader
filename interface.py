
import os
import youtube_down_multi_link

 
def ban():
    cls()
    print("""
            _____      _____        _____            _____     ____   ____  _________________  ____   ____       _____        ______   
            |\    \    /    /|  ____|\    \      ____|\    \   |    | |    |/                 \|    | |    | ___|\     \   ___|\     \  
            | \    \  /    / | /     /\    \    /     /\    \  |    | |    |\______     ______/|    | |    ||    |\     \ |     \     \ 
            |  \____\/    /  //     /  \    \  /     /  \    \ |    | |    |   \( /    /  )/   |    | |    ||    | |     ||     ,_____/|
             \ |    /    /  /|     |    |    ||     |    |    ||    | |    |    ' |   |   '    |    | |    ||    | /_ _ / |     \--'\_|/
              \|___/    /  / |     |    |    ||     |    |    ||    | |    |      |   |        |    | |    ||    |\    \  |     /___/|  
                  /    /  /  |\     \  /    /||\     \  /    /||    | |    |     /   //        |    | |    ||    | |    | |     \____|\ 
                 /____/  /   | \_____\/____/ || \_____\/____/ ||\___\_|____|    /___//         |\___\_|____||____|/____/| |____ '     /|
                |`    | /     \ |    ||    | / \ |    ||    | /| |    |    |   |`   |          | |    |    ||    /     || |    /_____/ |
                |_____|/       \|____||____|/   \|____||____|/  \|____|____|   |____|           \|____|____||____|_____|/ |____|     | /
                )/             \(    )/         \(    )/        \(   )/       \(                \(   )/    \(    )/      \( |_____|/ 
                '               '    '           '    '          '   '         '                 '   '      '    '        '    )/    
    
      ____           _____      _____          _____   ______    ____                _____           ____        _____        ______        _____   
 ___|\    \     ____|\    \    |\    \   _____|\    \ |\     \  |    |          ____|\    \     ____|\   \   ___|\    \   ___|\     \   ___|\    \  
|    |\    \   /     /\    \   | |    | /    /|\\    \| \     \ |    |         /     /\    \   /    /\    \ |    |\    \ |     \     \ |    |\    \ 
|    | |    | /     /  \    \  \/     / |    || \|    \  \     ||    |        /     /  \    \ |    |  |    ||    | |    ||     ,_____/||    | |    |
|    | |    ||     |    |    | /     /_  \   \/  |     \  |    ||    |  ____ |     |    |    ||    |__|    ||    | |    ||     \--'\_|/|    |/____/ 
|    | |    ||     |    |    ||     // \  \   \  |      \ |    ||    | |    ||     |    |    ||    .--.    ||    | |    ||     /___/|  |    |\    \ 
|    | |    ||\     \  /    /||    |/   \ |    | |    |\ \|    ||    | |    ||\     \  /    /||    |  |    ||    | |    ||     \____|\ |    | |    |
|____|/____/|| \_____\/____/ ||\ ___/\   \|   /| |____||\_____/||____|/____/|| \_____\/____/ ||____|  |____||____|/____/||____ '     /||____| |____|
|    /    | | \ |    ||    | /| |   | \______/ | |    |/ \|   |||    |     || \ |    ||    | /|    |  |    ||    /    | ||    /_____/ ||    | |    |
|____|____|/   \|____||____|/  \|___|/\ |    | | |____|   |___|/|____|_____|/  \|____||____|/ |____|  |____||____|____|/ |____|     | /|____| |____|
  \(    )/        \(    )/        \(   \|____|/    \(       )/    \(    )/        \(    )/      \(      )/    \(    )/     \( |_____|/   \(     )/  
   '    '          '    '          '      )/        '       '      '    '          '    '        '      '      '    '       '    )/       '     '   
                                          '                                                                                      '                                                                                                                                   '       
    """)
    menu_principal()

def cls():
    os.system('cls')

def menuListener(n: int):
    return n

def menu_principal():
    print("""
1)__________________Telecharger flux
2)__________Obtenir information flux 
0)___________________________Quitter
    """)
    choix_menu_Principal = input("Votre choix : ")
    if choix_menu_Principal == "1":
        sous_menu_telechargement()
    elif choix_menu_Principal == "2" :
        sous_menu_information()
    elif choix_menu_Principal == "0":
        quit()

def sous_menu_telechargement():
    cls()
    print("""
    1)____________________Telecharger flux Audio
    2)____________________Telecharger flux Video
    0)_____________________Retour menu principal
    """)
    choix_sous_menu_telechargement = input("Votre choix : ")
    if choix_sous_menu_telechargement == "1":
        sous_menu_telechargement_audio()
    elif choix_sous_menu_telechargement == "2" :
        sous_menu_telechargement_video()
    elif choix_sous_menu_telechargement == "0":
        ban()

def sous_menu_information():
    cls()
    print("""
        1)_____________Obtenir les informations d'un flux
        0)__________________________Retour menu principal
    """)
    choix_sous_menu_information = input("Votre choix : ")
    if choix_sous_menu_information == "1":
        url_info = input("Veuillez saisir l'url :")
        youtube_down_multi_link.get_info_flux(url_info)
        sous_menu_information()
    elif choix_sous_menu_information == "0":
        ban()
 
def sous_menu_telechargement_video():
    cls()
    print("""
        1)__________________________Telecharger un flux video
        2)_________________________Telecharger des flux video
        0)___________________________Retour au menu precedent
    """)
    choix_sous_menu_telechargement_video = input("Votre choix : ")
    if choix_sous_menu_telechargement_video == "1":
        youtube_down_multi_link.download_video()
    elif choix_sous_menu_telechargement_video == "2":
        youtube_down_multi_link.downloadS_videoS()
    elif choix_sous_menu_telechargement_video == "0":
        sous_menu_telechargement()

def sous_menu_telechargement_audio():
    cls()
    print("""
        1)__________________________Telecharger un flux audio
        2)____________________Telecharger plusieur flux audio
        0)___________________________Retour au menu precedent
    """)
    choix_sous_menu_telechargement_audio = input("Votre choix : ")
    if choix_sous_menu_telechargement_audio == "1":
        youtube_down_multi_link.download_audio()
        sous_menu_telechargement()
    elif choix_sous_menu_telechargement_audio == "2" :
        youtube_down_multi_link.downloadS_audioS()
    elif choix_sous_menu_telechargement_audio == "0":
        sous_menu_telechargement()

