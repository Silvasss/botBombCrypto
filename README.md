# Automatização do BombCrypto

O código recebe as informações sobre o jogo por impressões da tela. Sem a necessidade de analisar o código-fonte da página.

## Ferramentas

[Python 3.7](https://www.python.org/downloads/release/python-370/), selecionar a versão "Windows x86-64 executable installer". No processo de instalação selicionar "Add Path".

[PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=windows).

[Anaconda](https://www.anaconda.com/products/individual), caso não utilize o PyCharm.


## Instalação das bibliotecas necessárias

PyAutoGui.
```bash
pip install pyautogui
```
Ultra fast cross-platform multiple screenshots module in pure python using ctypes.
```bash
pip install mss
```
OpenCV.
```bash
pip install opencv-python
```
Numpy.
```bash
pip install numpy
```

Pure Python, cross platform, single function module with no dependencies for playing sounds.
```bash
pip install playsound==1.2.2
```

# Cuidados na execução

```
* Resolução Full-HD (1920x1080).
* Escala da tela em 100%.
* Não deixar outras abas abertas, enquanto executa o script.
* Tema ou icones do navegador pode afetar o desempenho do script.
* Tema ou icones do Windows pode afetar o desempenho do script.
```

# Funcionalidades disponíveis

###**Alterar os valores do arquivo "configMain.py"**
