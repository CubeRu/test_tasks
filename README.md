
## Инструкция по запуску:
### 1. Развертываем виртуальное окружение 
#### **_Установка виртуального окружения_**

__Windows:__
```
python -m virtualenv test
```

__Linux:__
```
python3 virtualenv test
```

#### **_Запуск виртуального окружения_**

__Windows:__
```
test\Scripts\activate
```

__Linux:__
```
$ source test/bin/activate
```
___
### 2. Клонируем репозиторий
```
git clone https://github.com/CubeRu/test_tasks.git
```
___
### 3.Устанавливаем необходимые библиотеки

**_Windows:_**
```
pip install -r requirements.txt
```

**_Linux:_**
```
pip install -r requirements.txt
```
___
### 4. Запускаем

**_Windows:_**
```
..\test\test_tasks.py
```

**_Linux:_**
```
python test_tasks.py
```
