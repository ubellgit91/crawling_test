# Python 경로지정, 파일만들기, 폴더만들기

## 현재 디렉토리 경로지정

```python
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
```

이런 식으로 os모듈을 import하고,

path를 통해 현재 작업 중인 디렉토리의 경로를 지정할 수 있다.

-------



## 폴더 만들기

```python
import os

def make_folder(folder_name): # isdir()로 해당 경로에 맞는 폴더가 있는지 확인하고 없으면 만든다.
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

```

os.path.isdir('경로')

해당 경로에 일치하는 폴더가 없으면 false, 있으면 true를 반환한다.

os.mkdir('경로') 경로에 맞는 폴더를 만든다.