# Пошаговая автоматизация с использованием Bash/Python, Docker и Ansible

## Раздел 1

Была разработана программа на Python, которая выполняет HTTP-запросы к сервису `https://tools-httpstatus.pickup-services.com/` и обрабатывает ответы по ТЗ. 

> [!NOTE]
> При вызове скрипта рандомно выбираются 5 запросов из списка.

---

## Раздел 2

Был разработан Docker-образ на базе **Ubuntu 22.04**. 

> [!TIP]
> Код был скопирован в последнюю очередь, чтобы избежать пересборки слоев при изменении кода.

---

## Раздел 3

Автоматизация с помощью Ansible производилась на двух ВМ на базе **VMware® Workstation 17 Pro**. Было использовано две машины: **Ub1-Pushkarev** (Control Node) и конфигурируемая ВМ **Ub2-Pushkarev** (Target Node) с адресами `192.168.111.164` (рис. 1) и `192.168.111.165` (рис. 2).

| Роль | Имя ВМ | IP адрес |
|------|--------|----------|
| Control Node | Ub1-Pushkarev | `192.168.111.164` |
| Target Node | Ub2-Pushkarev | `192.168.111.165` |

<p align="center">
  <img src="img/vm1.png" alt="Control Node" width="45%">
  <img src="img/vm2.png" alt="Target Node" width="45%">
</p>
<p align="center">
  <em>Рисунок 1 — Control Node (Ub1-Pushkarev)</em>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <em>Рисунок 2 — Target Node (Ub2-Pushkarev)</em>
</p>

---

### SSH

Для безопасного подключения было выполнено создание ключей `ansible-key`. Публичный ключ был скопирован на Target Node (рис. 3–4).

<p align="center">
  <img src="img/ssh_key.png" alt="ssh-keygen">
  <br>
  <em>Рисунок 3 — Генерация SSH ключей (ssh-keygen)</em>
</p>

<p align="center">
  <img src="img/copy.png" alt="ssh-copy">
  <br>
  <em>Рисунок 4 — Копирование публичного ключа (ssh-copy-id)</em>
</p>

---

### Ansible

#### 1. Проверка подключения

Был создан файл `inventory.yml` с указанием адреса VM машины. Для тестирования подключения написан плейбук `test_connection.yml` с проверкой подключения под sudo. Плейбук был запущен с параметром `--ask-become-pass`, который запрашивает sudo пароль перед выполнением задач, требующих повышенных привилегий.

**Результат выполнения плейбука (рис. 5):**

<p align="center">
  <img src="img/test_connection.png" alt="test_connection.yml">
  <br>
  <em>Рисунок 5 — Выполнение плейбука test_connection.yml</em>
</p>

---

#### 2. Установка Docker

Был написан плейбук `install_docker.yml` для установки Docker на VM.

**Результат выполнения плейбука (рис. 6):**

<p align="center">
  <img src="img/docker_install.png" alt="install_docker.yml">
  <br>
  <em>Рисунок 6 — Выполнение плейбука install_docker.yml</em>
</p>

---

#### 3. Публикация Docker образа

Созданный образ из Раздела 2 был выгружен в Docker Hub (рис. 7–8).

<p align="center">
  <img src="img/docker_push.png" alt="docker push">
  <br>
  <em>Рисунок 7 — Выгрузка образа (docker push)</em>
</p>

<p align="center">
  <img src="img/docker_hub.png" alt="Docker Hub">
  <br>
  <em>Рисунок 8 — Образ в Docker Hub</em>
</p>

---

#### 4. Проверка скрипта в контейнере

Был создан плейбук `check_script_container.yml`, который:
- проверяет наличие Docker,
- скачивает образ из облачного хранилища,
- запускает контейнер,
- выводит логи контейнера,
- проверяет код завершения.

**Результат выполнения плейбука (рис. 9):**

<p align="center">
  <img src="img/check_script.png" alt="check_script_container.yml">
  <br>
  <em>Рисунок 9 — Выполнение плейбука check_script_container.yml</em>
</p>