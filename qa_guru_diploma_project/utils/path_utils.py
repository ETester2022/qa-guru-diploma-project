import os

def get_picture_path(filename):
    """Возвращает абсолютный путь к картинке в tests/resources."""
    base_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(base_dir, '..', '..'))  # поднимаемся к корню проекта
    resources_dir = os.path.join(project_root, 'tests', 'resources')
    picture_path = os.path.join(resources_dir, filename)

    if not os.path.isfile(picture_path):
        raise FileNotFoundError(f"Файл {filename} не найден в {resources_dir}")
    return picture_path