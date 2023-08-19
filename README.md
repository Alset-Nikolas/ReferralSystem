<h1 align="center">Тестовое задание Python разработчик (Django) 
<a href='https://hammer.systems/'>
(Hammer Systems)
</a>
</h1>


<h2 align="center">1. Структура репозитория:
<img width="64" height="64" src="https://img.icons8.com/external-justicon-lineal-color-justicon/64/external-tree-tree-justicon-lineal-color-justicon-6.png" alt="external-tree-tree-justicon-lineal-color-justicon-6"/>
</h2>

    .
    ├── app   -> Приложение
    ├── README.md -> Описание (мы тут)
    ├── ReferralSystem.postman_collection.json - коллекция Postman
    └── TASK.docx -> ТЗ

<h2 align="center">2. Запуск
<img width="100" height="100" src="https://img.icons8.com/stickers/100/construction-worker.png" alt="construction-worker"/>
</h2>

1. Клонируем репозиторий

```
    git clone git@github.com:Alset-Nikolas/ReferralSystem.git
```
2. Настройка файла infra/.env
```
    SECRET_KEY = 'django-insecure-r7lng6xaaystn%o45+l=_63gqr*h^cc$i68&-x!a0n#%&^eh5v'
    
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=referral_system_db 
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=qwerty1234QWERTY
    DB_HOST=refferal_system_db
    DB_PORT=5432 

    DJANGO_SUPERUSER_PHONE=7-000-000-0000
```


3. Собрать и запустить контейнеры
  ```
  sudo docker-compose build
  sudo docker-compose up
  ```

    
<h2 align="center">3. Иллюстрация</h2>

<img width="50" height="50" src="https://img.icons8.com/stickers/100/phone.png" alt="phone"/>
Регистрация пользователя происходит при первой авторизации.<br>
Пользователь вбивает свой номер, например 7-999-100-1031<br>
Дальше нужно ввести 4х значный код: для простоты это 4 последние цифры номера (для нашего примера это 1031)   <br>



<details>
  <summary>Авторизация по номеру телефона. Первый запрос на ввод номера телефона.</summary>
  <img src="./info/login_first_req.png" name="image-name">
</details>
<details>
  <summary>Пример ввода другого формата на 1 запрос</summary>
  <img src="./info/err_login_first_req.png" name="image-name">
</details>
<details>
  <summary>Имитировать отправку 4х значного кода авторизации</summary>
  <img src="./info/login_second_req.png" name="image-name">
</details>
<details>
  <summary>Пример ввода ошибочного токена на 2 запрос</summary>
  <img src="./info/err_login_second_req.png" name="image-name">
</details>

<br>

<img width="48" height="48" src="https://img.icons8.com/color/48/registration-skin-type-7.png" alt="registration-skin-type-7"/>
После авторизации пользователь попадает в свой профиль.
При первой авторизации рандомно генерируется 6-значный инвайт-код (у меня L5C4Yp)
<details>
  <summary>Профиль пользователя 7-999-100-1031 (L5C4Yp)</summary>
  <img src="./info/profile.png" name="image-name">
</details>
<details>
  <summary>Профиль пользователя 7-777-777-7777 (R42HbT)</summary>
  <img src="./info/profile2.png" name="image-name">
</details>
<br>
<img width="50" height="50" src="https://img.icons8.com/clouds/100/work.png" alt="work"/>
В профиле у пользователя есть возможность ввести чужой инвайт-код<br>
В своем профиле можно активировать только 1 инвайт код<br>
<details>
  <summary>Активация токена L5C4Yp у пользователя 7-777-777-7777</summary>
  <img src="./info/token_activate.png" name="image-name">
</details>
<details>
  <summary>Попытка активации своего или несуществующего токена</summary>
  <img src="./info/err_token_activate.png" name="image-name">
</details>
<br>
<img width="50" height="50" src="https://img.icons8.com/plasticine/100/list.png" alt="list"/>
В профиле должен выводиться список пользователей, которые ввели инвайт код текущего пользователя.
<details>
  <summary>Список пользователей</summary>
  <img src="./info/token_list.png" name="image-name">
</details>


<h2 align="center">4. Документация Api
<img width="40" height="40" src="https://img.icons8.com/office/40/Archive-List-Of-Parts.png" alt="Archive-List-Of-Parts"/>
</h2>
Если перейти по /swagger-ui/ будет Swagger-ui
<img src="./info/docs.png" name="image-name">

<h2 align="center">5. Админка
<img width="48" height="48" src="https://img.icons8.com/color/48/admin-settings-male.png" alt="admin-settings-male"/>
</h2>
Если перейти по /admin/ будет форма авторизации. Если зайти под админом откроется адмнка
<img src="./info/admin.png" name="image-name">

<h2 align="center">6. Postman
<img width="50" height="50" src="https://img.icons8.com/bubbles/50/man-with-a-mailbox.png" alt="man-with-a-mailbox"/>
</h2>

<div align="center">
<img src="./info/postman.png" name="image-name" center>
</div>


<h2 align="center">7. Для тестов полезен pgAdmin
<img width="50" height="50" src="https://img.icons8.com/bubbles/50/man-with-a-mailbox.png" alt="man-with-a-mailbox"/>
</h2>
http://ip_server:5555/
<div align="center">
<img src="./info/pgadmin.png" name="image-name" center>
</div>

Инструкция по запуску
<details>
  <summary>логин/пароль --> z@mail.ru/z</summary>
  <div align="center">
    <img src="./info/pgadmin_login.png" name="image-name">
  </div>
</details>
<details>
  <summary>Servers/Register/Сервер...</summary>
  <div align="center">
    <img src="./info/pg_step1.png" name="image-name">
  </div>
</details>
<details>
  <summary>Имя - любое</summary>
  <div align="center">
    <img src="./info/pg_step2.png" name="image-name">
  </div>
</details>
<details>
  <summary>refferal_system_db/5432/referral_system_db/postgres/qwerty1234QWERTY</summary>
  <div align="center">
    <img src="./info/pg_step3.png" name="image-name">
  </div>
</details>
<details>
  <summary>Ура</summary>
  <div align="center">
    <img src="./info/pg_step_end.png" name="image-name">
  </div>
</details>
