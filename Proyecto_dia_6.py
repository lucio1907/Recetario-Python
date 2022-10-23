import os
from pathlib import Path

# Ruta principal
principal_route = Path(Path.home() / 'Desktop', 'Recetas')

def format_console():
    return os.system('cls')

def menu():
    format_console()
    print(f'El recetario se encuentra en el directorio {principal_route}')
    print('''BIENVENIDO A MI RECETARIO
    =========================
 
    1) Leer una receta
    2) Crear una receta
    3) Crear una categoria
    4) Eliminar una receta
    5) Eliminar una categoria
    6) Salir
    ''')

def user_selection_validation():
    while True:
        selection = int(input('Elige una operación: '))

        if selection <= 0:
            format_console()
            print(f'Debes ingresar un número entre el 1 y el 6, ingresaste {selection}')
            continue

        if selection > 6:
            format_console()
            print(f'Debes ingresar un número entre el 1 y el 6, ingresaste {selection}')

        if selection <= 6:
            break
    return selection

def user_selection():
    if selected == 1:
        option_1()
    elif selected == 2:
        option_2()
    elif selected == 3:
        option_3()
    elif selected == 4:
        option_4()
    elif selected == 5:
        option_5()
    elif selected == 6:
        print('Te veo luego!')
        return False

def option_1():
    format_console()
    files = os.listdir(principal_route)
    print(f'Estas son las recetas disponibles: {tuple(files)}')
    user_selection_option_1 = input(f'¿Qué categoría eliges?: ').capitalize()
    files = [prescription.capitalize() for prescription in files]
    
    while True:
        if user_selection_option_1 not in files:
            format_console()
            print(f'Estas son las recetas disponibles: {tuple(files)}')
            print('No existe el recetario seleccionado')
            user_selection_option_1 = input(f'¿Qué categoría eliges?: ').capitalize()

            continue
        else:
            read_selected_file(user_selection_option_1)
            break

def option_2():
    format_console()
    files = os.listdir(principal_route)
    print(f'Estas son las recetas disponibles: {tuple(files)}')
    user_selection_option_2 = input(f'¿Qué categoría eliges?: ').capitalize()
    files = [prescription.capitalize() for prescription in files]

    while True:
        if user_selection_option_2 not in files:
            format_console()
            print(f'Estas son las recetas disponibles: {tuple(files)}')
            print('No existe el recetario seleccionado')
            user_selection_option_2 = input(f'¿Qué categoría eliges?: ').capitalize()

            continue
        else:
            write_selected_file(user_selection_option_2)
            break

def option_3():
    format_console()
    new_directory_name = input('¿Cómo se va a llamar tu nueva categoría?: ').capitalize()
    new_directory = os.makedirs(principal_route / new_directory_name)
    print('Se ha creado la carpeta correctamente!')
        
    return new_directory

def option_4():
    format_console()
    files = os.listdir(principal_route)
    print(f'Estas son las recetas disponibles: {tuple(files)}')
    user_selection_option_4 = input(f'¿Qué categoría eliges?: ').capitalize()
    files = [prescription.capitalize() for prescription in files]
    
    while True:
        if user_selection_option_4 not in files:
            format_console()
            print(f'Estas son las recetas disponibles: {tuple(files)}')
            print('No existe el recetario seleccionado')
            user_selection_option_4 = input(f'¿Qué categoría eliges?: ').capitalize()

            continue
        else:
            delete_selected_file(user_selection_option_4)
            break
    
def option_5():
    format_console()
    files = os.listdir(principal_route)
    print(f'Elige entre estas carpetas {tuple(files)}')
    directoy_name_to_delete =  input('¿Qué directorio querés borrar?: ').capitalize()
    deleted_directory = os.removedirs(principal_route / directoy_name_to_delete)

    print('Se ha eliminado la carpeta correctamente!')

    return deleted_directory

def write_selected_file(selected_file):
    if selected_file:
        format_console()
        route_selected = Path(principal_route / selected_file)
        
        directory_name_input = input('Escribe el nombre de tu receta: ').capitalize()
        new_file = open(f'{route_selected}/{directory_name_input}.txt', 'a')
        new_file.close()
        
        if new_file:
            format_console()
            new_file_contents = input('Ingrese el contenido de la receta: ').capitalize()
            file_created = open(f'{route_selected}/{directory_name_input}.txt', 'a')
            file_created.write(new_file_contents)
            print('La receta se creó correctamente!')
            file_created.close()

def read_selected_file(selected_file):
    if selected_file:
        format_console()
        route_selected = Path(principal_route / selected_file)
        archives = os.listdir(route_selected)
        
        is_valid, user_archive_selected = validation_archive_selected(archives)
        
        if is_valid:
            format_console()
            final_route = route_selected / archives[user_archive_selected - 1]
            print(final_route.read_text())

def delete_selected_file(selected_file):
    total_archives = 0

    if selected_file:
        format_console()
        route_selected = Path(principal_route / selected_file)
        archives = os.listdir(route_selected)

        for archive in archives:
            total_archives += 1
            print(f'{total_archives}) {archive}')
    
    while True:
        if not archives:
            print('No existen archivos en esta carpeta')
            break
        else:
            archive_to_delete = int(input('¿Qué archivo desea eliminar?: '))

            if archive_to_delete > len(archives):
                format_console()
                print('La receta seleccionada no existe')
                print(f'{total_archives}) {archive}')
                continue
            
            if archive_to_delete not in range(0, 7):
                format_console()
                print('La receta seleccionada no existe')
                print(f'{total_archives}) {archive}')
            else:
                archive_deleted = os.remove(route_selected / archives[archive_to_delete - 1])
                print('La receta se ha eliminado correctamente!')
                break
        return archive_deleted

def validation_archive_selected(archives):
    total_archives = 0
    is_valid = False

    for archive in archives:
        total_archives += 1
        print(f'{total_archives}) {archive}')

    while True:
        user_archive_selected = int(input('Elige entre estas listas: '))

        if user_archive_selected > total_archives:
            format_console()
            print('Ingresaste un número incorrecto, ingresa otro!')
            print(f'{total_archives}) {archive}')
            continue
        else:
            is_valid = True
            break
    return is_valid, user_archive_selected

menu()
selected = user_selection_validation()
user_selection()
