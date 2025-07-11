@echo off
setlocal enabledelayedexpansion

::Ім'я файлу, який шукаємо
set "filename=menu.py"

:: Шукаємо файл у всіх підпапках
for /r %%f in (*%filename%) do (
    echo Знайдено: %%f

    :: Запуск з утриманням консолі відкритою
    cmd /k python "%%f"
    goto :eof
)

echo Файл %filename% не знайдено
pause
