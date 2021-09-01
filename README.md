# Readme of Eng-2021-PBL-ML
「Raspberry Piで学ぶ機械学習入門」向けのコンテンツです．

# Requirement
* Raspberry Pi 3 Model B+ or later version
* Raspbian 9.4 (Stretch) or later version
 
# Installation
本リポジトリから，Pythonスクリプト(setup.py)を直接ダウンロードいただくか，端末から
下記コードを打ち込んでいただきます．:
```bash
git clone https://github.com/masashis2021PBL/Eng-2021-PBL-ML.git
```
setup.pyを直接ダウンロードされた場合は，ダウンロード先を端末で指定したうえで，
```bash
sudo python3 setup.py
```
を実行してください．リポジトリをダウンロードした場合(git clone)は，
```bash
cd "Eng-2021-PBL-ML"
sudo python3 setup.py
```
を実行してください．

# Note
インストール後に現れる/deep-learning-models内にあるinception_v3.pyを実行することで
深層学習による物体認識が可能になりますが，初回はinception_v3.pyのうち，いくつかの行を
変更する必要があります．
(35行目)
```bash
from keras.applications.imagenet_utils import _obtain_input_shape
```
を
```bash
from keras_applications.imagenet_utils import _obtain_input_shape
```
に変更すること．
(157行目)
```bash
include_top=include_top
```
を
```bash
require_flatten=include_top
```
に変更すること．

# Usage
Raspberry Piでカメラモジュールを使用する際は，以下のようなコマンドを実行してください．
```bash
raspistill -w 320 -h 240 -e bmp -o cam10.bmp
```
Raspberry Piで物体認識を使用する際は，以下のようなコマンドを実行してください．
```bash
python3 inception_v3.py
```

# License
"Eng-2021-PBL-ML" is Confidential.
