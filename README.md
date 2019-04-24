# Cooporate

## 受け取るもの

1. ファイル名
2. 実行される関数名

## 返却される構造体
実行した関数が返却する値をWebSocket側に流します。

受け取り側の言語はまだなんであるはわかりませんが
Pythonだと以下のような感じで渡します

```Python3
from enum import Enum, auto
from typing import TypeVar, Generic

class State(Enum):
    Err = auto()
    FileNotFound = auto()
    FunctionNotFound = auto()
    Ok  = auto()

class Type(Enum):
    Str = auto()
    Int  = auto()
    Float  = auto()

T = TypeVar('T')
class Result(Generic[T]):
    def __init__(self, state: State, values_type: Type, value: T, error_message: str) -> None:
        self.state = state        
        self.val_type = values_type
        self.val = value
        self.err_message = error_message

result = Result[str](State.Ok, Type.Str, "Hello", None)
```

### self.state

* 実行が成功した: ``OK``
  
* 実行が失敗した: ``Err``
  
* ファイル名が見つからない: ``FileNotFound``
  
* 関数名が見つからない: ``FunctionNotFound``
  
の4値をとります。
  
### self.val

実行した関数が返却した値です。
    
### self.val_type
 
実行した関数が返却する値の型です。
    
### self.err_message

実行が失敗した場合(``State.Err``)のエラーメッセージです。

## 実行例

ファイル名: ``input.py``
関数名: ``p.get_name()``

```Python3
#input.py
class Person:
    def __init__(self,age,name):
        self.__age = age
        self.__name = name
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name

    

p = Person(14, "Ayaya")
print(str(p.get_name()) + str(p.get_age()))
print(str(p.get_age()))
```

### 実行されるプログラム

```Python3
#input.py
class Person:
    def __init__(self,age,name):
        self.__age = age
        self.__name = name
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
   
p = Person(14, "Ayaya")
p.get_name()
```

