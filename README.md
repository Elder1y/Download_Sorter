===============================================================================
   ____             _   ____        _           _   
  / ___|  ___   ___| |_/ ___|  ___ | |_   _____| |_
  \___ \ / _ \ / __| __\___ \ / _ \| \ \ / / _ \ __|
   ___) | (_) | (__| |_ ___) | (_) | |\ V /  __/ |_
  |____/ \___/ \___|\__|____/ \___/|_| \_/ \___|\__|
===============================================================================

# 🧹 AutoSort — Персональный дворецкий вашей папки «Загрузки» / Your Downloads Folder’s Personal Butler

> _«Пусть машины сортируют хаос. Вы — наслаждайтесь жизнью.»_  
> _“Let the machine sort your chaos. You focus on what matters.”_

![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero%20External-00C853?style=flat)
![MIT License](https://img.shields.io/badge/License-MIT-FFD700?style=flat)
![Magic Inside](https://img.shields.io/badge/Magic-100%25%20Guaranteed-purple?style=for-the-badge)

<div align="center">
  <img src="https://media.giphy.com/media/l0HlG8vJkDQAXvJ7W/giphy.gif" width="450" alt="Organized Folder Magic">
  <br>
  <em>Смотрите, как ваша папка превращается в цифровой дзен 🌿 / Watch your messy Downloads folder turn into a zen garden 🌿</em>
</div>

---

### 🇷🇺 Русский

#### ✨ До и После

| ❌ **ДО** — Цифровой хаос       | ✅ **ПОСЛЕ** — Цифровой порядок     |
|-------------------------------|------------------------------------|
| ![Messy Downloads](https://i.imgur.com/6X2J8Kk.png) | ![Sorted Folders](https://i.imgur.com/9V4W3rF.png) |
| _«Где тот PDF?!»_             | _«Всё отсортировано. Автоматически.»_ |

#### ⚡ Что делает скрипт?

Скрипт сканирует папку `Загрузки` и **автоматически сортирует все файлы** по категориям:

📁 `Images` — `.jpg`, `.png`, `.gif`, `.bmp`, `.svg`  
📄 `Documents` — `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`  
📦 `Archives` — `.zip`, `.rar`, `.7z`, `.tar`, `.gz`  
🎬 `Videos` — `.mp4`, `.mkv`, `.avi`, `.mov`  
🎵 `Music` — `.mp3`, `.wav`, `.flac`, `.aac`  
⚙️ `Executables` — `.exe`, `.msi`

> 💡 Больше не нужно перетаскивать файлы вручную. Запустил — и всё на своих местах.

#### 🚀 Как использовать

##### Шаг 1: Клонируйте или скачайте

git clone https://github.com/yourusername/autosort.git
cd autosort python AutoSort.py

✅ Готово. Ваши загрузки теперь в идеальном порядке.

### 🇺🇸 English
#### ✨ Before & After
Messy Downloads
Sorted Folders
“Where’s that PDF?!”
“Everything sorted. Automatically.”

## ⚡ What It Does
This script scans your Downloads folder and automatically sorts every file into categorized subfolders:

📁 Images — .jpg, .png, .gif, .bmp, .svg
📄 Documents — .pdf, .docx, .txt, .xlsx, .pptx
📦 Archives — .zip, .rar, .7z, .tar, .gz
🎬 Videos — .mp4, .mkv, .avi, .mov
🎵 Music — .mp3, .wav, .flac, .aac
⚙️ Executables — .exe, .msi

> 💡 No more manual dragging. One run → instant order.

#### 🚀 How to Use
##### Step 1: Clone or Download
bash git clone https://github.com/yourusername/autosort.git
cd autosort
Step 2: Run the Magic
bash python AutoSort.py
✅ Done. Your downloads are now beautifully organized.

🔄 Автоматизация / Automation
🇷🇺 Хотите, чтобы скрипт запускался каждый день? Используйте Планировщик заданий Windows:
Откройте Планировщик заданий → Создать задачу
Триггер: “Ежедневно в 20:00”
Действие:
Программа: python.exe
Аргумент: путь к AutoSort.py
🤖 Как невидимый дворецкий — убирает за вами, пока вы спите.

🇺🇸 Want it to run every day automatically? Use Windows Task Scheduler:
Open Task Scheduler → Create Task
Trigger: “Daily at 8:00 PM”
Action:
Program: python.exe
Arguments: C:\path\to\AutoSort.py
🤖 Like a silent butler — cleaning your digital mess while you sleep.

🛠️ Кастомизация / Customization
🇷🇺 Добавьте свои категории — просто отредактируйте словарь EXTENSIONS в коде:
python


1
2
3
4
5
⌄
EXTENSIONS = {
    "Design": [".psd", ".ai", ".fig"],
    "Ebooks": [".epub", ".mobi"],
    "Scripts": [".py", ".js", ".bat"],
}
❓ Что значит “Поддержка конфиг-файла”?
Сейчас категории жёстко прописаны в коде. “Поддержка конфиг-файла” означает, что вы сможете вынести настройки (типы файлов, названия папок) в отдельный файл config.json — и менять их без открытия кода. Пример:

json


1
2
3
4
⌄
{
  "Images": [".jpg", ".png"],
  "MyFolder": [".myext"]
}
Это удобно для пользователей, не умеющих программировать.

🇺🇸 Add your own categories — just edit the EXTENSIONS dictionary:
python


1
2
3
4
5
⌄
EXTENSIONS = {
    "Design": [".psd", ".ai", ".fig"],
    "Ebooks": [".epub", ".mobi"],
    "Scripts": [".py", ".js", ".bat"],
}
❓ What is “Config File Support”?
Currently, categories are hardcoded. “Config file support” means you can move settings (file types, folder names) into a separate config.json file — and change them without touching the code. Example:

json
'''bash
{
  "Images": [".jpg", ".png"],
  "MyFolder": [".myext"]
}
bash'''
Great for non-programmers or frequent customization.

📦 Требования / Requirements
✅ Python 3.6+ (установлен почти везде)
✅ Нет внешних зависимостей — только os и shutil
✅ Работает на Windows, macOS, Linux
✅ Python 3.6+ (pre-installed on most systems)
✅ No external libraries — pure os and shutil
✅ Works on Windows, macOS, Linux
🌟 Почему это нравится людям / Why People Love This
🇷🇺 «Тратил 10 минут в день на уборку загрузок. Теперь — 0. Этот скрипт вернул мне 60+ часов в год.» — Анонимный пользователь
🇺🇸 “I used to waste 10 mins/day cleaning downloads. Now? Zero. This script gave me back 60+ hours a year.” — Anonymous User

🇷🇺 «Так просто, но так приятно запускать. Как цифровой ASMR.» — Пользователь Reddit
🇺🇸 “So simple, yet so satisfying to run. Like digital ASMR.” — Reddit User

📜 Лицензия / License
MIT — Делайте что хотите. Только не вините меня, если ваш кот научится программировать.
MIT — Do whatever you want. Just don’t blame me if your cat learns to code.

Полная лицензия → LICENSE
Full License → LICENSE

☕ Поддержать автора / Support the Author
Если скрипт сэкономил вам время или нервы — можно поддержать автора:
If this saved you time, sanity, or both — consider buying me a coffee:

Buy Me a Coffee

<div align="center">
<img src="https://media.giphy.com/media/3o7TKsQ8UQIzIwNklG/giphy.gif" width="300" alt="Folder Magic">
<br>
<em>Потому что даже папки заслуживают немного магии ✨ / Because even folders deserve a little magic ✨</em>
</div>

🧹 🇷🇺 «Цивилизация измеряется не технологиями — а тем, сколько рутины она устраняет.»
🧹 🇺🇸 “Civilization is measured not by its tech — but by how much routine it eliminates.”
— Скорее всего, это будешь ты, очень скоро™ / — Probably You, Soon™
