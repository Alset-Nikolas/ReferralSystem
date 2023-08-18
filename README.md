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
    └── TASK.docx -> ТЗ

<h2 align="center">2. Запуск
<img width="100" height="100" src="https://img.icons8.com/stickers/100/construction-worker.png" alt="construction-worker"/>
</h2>

1. Клонируем репозиторий
   * git clone git@github.com:Alset-Nikolas/ReferralSystem.git

    
<h2 align="center">3. Иллюстрация</h2>

<p>
<img width="50" height="50" src="https://img.icons8.com/stickers/100/phone.png" alt="phone"/>
Регистрация пользователя происходит при первой авторизации.<br>
Пользователь вбивает свой номер, например 7-999-100-1031<br>
Дальше нужно ввести 4х значный код: для простоты это 4 последние цифры номера (для нашего примера это 1031)   <br>

</p>

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
