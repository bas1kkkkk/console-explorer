import os
import send2trash

while True:
    path = input('Введите путь к папке')
    if os.path.exists(path) and os.path.isdir(path): 
        break
    else:
        print('Такого пути не существует')

files_and_folders = os.listdir(path)
print('Содержимое папки: ')
for item in files_and_folders: 
    print(f'- {item}')

while True:
    user_choice = input('Введите название файла или папки:')
    if user_choice in files_and_folders:
        target_path = os.path.join(path, user_choice)
        break
    else:
        print('Такой папки не сушествует в данном каталоге')

while True:
    print('')
    print('        Что хотите сделать?         ')
    print('------------------------------------')
    print('|1 - Удалить                       |')
    print('|2 - Переименовать                 |')
    print('|3 - Переместить                   |')
    print('|4 - Посмотреть содержимое папки   |')
    print('|5 - Создать папку                 |')
    print('|6 - Создать файл                  |')
    print('|7 - Редактировать файл            |')
    print('|8 - Указать каталог               |')
    print('|9 - Выйти из программы            |')
    print('------------------------------------')
    print('')
    action = input('Выберите номер действия:   ')

    match action:
        case '1':
            send2trash.send2trash(target_path)
            if not os.path.exists(target_path):
                print('Файл или папка успешно отправлена в корзину')
        case '2':
            new_name = input('Введите новое имя: ')
            new_path = os.path.join(path, new_name)

            try: 
                os.rename(target_path, new_path)
                if os.path.exists(new_path) and not os.path.exists(target_path):
                    print('переименование прошло успешно')
                else:
                    print('Произошла ошибка при переименовании')
            except Exception as e:
                print(f'Произошла ошибка: {e}')
        
        case "3":
            new_location = input('Введите куда хотите переместить: ')
            new_path = os.path.join(new_location, os.path.basename(target_path))

            try:
                os.rename(target_path, new_path)
                if os.path.exists(new_path) and not os.path.exists(target_path):
                    print('Перемещение прошло успешно')
                else:
                    print('Ошибка при перемещении')
            except Exception as e:
                print(f'Ошибка : {e}')

        case "4":
            if os.path.isdir(target_path):
                path = target_path
                files_and_folders = os.listdir(path)
                print('Содержимое папки: ')
                for item in files_and_folders: 
                    print(f'- {item}')

                while True:
                    user_choice = input('Введите название файла или папки:')
                    if user_choice in files_and_folders:
                        target_path = os.path.join(path, user_choice)
                        break
                    else:
                        print('Такой папки не сушествует в данном каталоге')
            else:
                print('Вы выбрали файл а не папку, войти в папку нельзя')
        
        case "5":
            folder_name = input('Введите название: ')
            new_folder_path = os.path.join(path, folder_name)
            try:
                os.mkdir(new_folder_path)
                print(f'Папка {folder_name} создан по пути {new_folder_path}')
            except Exception as e:
                print(f'Ошибка при создании папки: {e}')

        case "6":
            file_name = input('Введите название файла:')
            new_file_path = os.path.join(path, file_name)
            try:
                with open(new_file_path, 'x') as f:
                    pass
            except FileExistsError:
                print('Такой файл уже существует')    
            except Exception as e:
                print(f'Ошибка при создании файла: {e}')
        
        case "7":
            if os.path.isfile(target_path):
                while True:
                    print('         Редактор файлов            ')
                    print('------------------------------------')
                    print('| 1 - Посмотреть файл              |')
                    print('| 2 - Добавить текст               |')
                    print('| 3 - Заменить содержимое          |')
                    print('| 4 - Удалить содержимое           |')
                    print('| 5 - Изменить название файла      |')
                    print('| 6 - Выйти из редактора файлов    |')
                    print('------------------------------------')

                    choice = input('Введите номер действия:  ')

                    match choice:
                        case "1":
                            try:
                                with open(target_path, 'r', encoding='utf-8') as file:
                                    content = file.read()
                                    print(f'Содержимое файла:{content}')
                                    print(content if content else "Файл пустой")       
                            except Exception as e:
                                print(f'Произошла ошибка: {e}')                     

                        case "2":
                            try:
                                with open(target_path, 'a+', encoding='utf-8') as file:
                                    user_text = input('Введите текст который хотите добавить конец файла: ')
                                    file.write(f'{user_text}')
                            except Exception as e:
                                print(f'Произошла ошибка: {e}')

                        case "3":
                            try:
                                with open(target_path, 'w+', encoding='utf-8') as file:
                                    user_content = input('Введите текст файла: ')
                                    file.write(f'{user_content}')
                            except Exception as e:
                                print(f'произошла ошибка: {e}')
                        
                        case "4":
                            try:
                                with open(target_path, 'w+', encoding='utf-8') as file:
                                    file.write('')
                            except Exception as e:
                                print(f'произошла ошибка: {e}')

                        case "5":
                            try:
                                user_filename = input('Введите новое название файла: ')
                                new_path = os.path.join(os.path.dirname(target_path), user_filename)

                                if os.path.exists(new_path):
                                    print('Файл с таким названием уже сущестует')
                                    continue
                        
                                os.rename(target_path, new_path)
                                print(f'Файл успешно переименован в {new_path}')

                                target_path=new_path
                            
                            except Exception as e:
                                print(f'Во время переименования файла произошла ошибка: {e}')
                        
                        case "6":
                            break

        case "8":
            new_path = input('Введите новый путь: ')
            if os.path.exists(new_path) and os.path.isdir(new_path):
                path = new_path
                files_and_folders = os.listdir(path)
                print(f'Вы перешли в папку: {path}')
                for item in files_and_folders:
                    print(f'- {item}')

                while True:
                    user_choice = input('Введите название файла или папки:')
                    if user_choice in files_and_folders:
                        target_path = os.path.join(path, user_choice)
                        break
                    else:
                        print('Такой папки или файла нет в данном каталоге')
            else:
                print('Такого пути не существует')

        case "9":
            print('Выход из программы')
            break

        case _:
            print('Неизвестная команда')