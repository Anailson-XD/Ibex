import os


def exibir_nome():
    print('#################################')
    print('Ｂｅｍ ｖｉｎｄｏ ａｏ Ｉｂｅｘ！')
    print('#################################')

def exibir_subtitulo(texto):
    os.system('cls')
    exibir_nome()
    print(texto)
    print()

def finalizando_app():
    exibir_subtitulo('Finalizando App')