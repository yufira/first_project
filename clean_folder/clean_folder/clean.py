import os
import sys
import shutil

list_of_directories = ['images', 'video', 'documents', 'music', 'archives', 'unknown_extensions']

def get_files(path, root_path):
    if os.path.exists(path):
        if os.path.isdir(path):
            normalize(path)
            sort_files(path, root_path)
            for i in os.listdir(path):
                i_joined_path = os.path.join(path, i)
                if os.path.isdir(i_joined_path) and (not os.path.basename(i_joined_path) in list_of_directories):
                    get_files(i_joined_path, root_path)
    else:
        print(f"I'm sorry. {path} does not exist")

def make_directory(path):
    for i in list_of_directories:
        i_joined_path = os.path.join(path, i)
        if not os.path.exists(i_joined_path):
            os.mkdir(i_joined_path)

def sort_files(path, root_path):
    ext_dict = {
        'images': ['.jpeg', '.png', '.jpg', '.svg'],
        'video': ['.avi', '.mp4', '.mov', '.mkv'],
        'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
        'music': ['.mp3', '.ogg', '.wav', '.amr'],
        'archives': ['.zip', '.gz', '.tar'],
        'unknown_extensions': []
    }
    
    category_files = {category: [] for category in ext_dict.keys()}
    known_extensions = []
    unknown_extensions = []

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            known_extension_found = False

            for category, extensions in ext_dict.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    known_extension_found = True
                    known_extensions.append(os.path.splitext(file)[1].lower())

                    if category == 'archives':
                        category_files[category].append(file)
                        archive_folder = os.path.join(root_path, 'archives', os.path.splitext(file)[0])  
                        os.makedirs(archive_folder, exist_ok=False)
                        shutil.unpack_archive(file_path, archive_folder)
                        os.remove(file_path)

                    else:
                        category_files[category].append(file)
                        category_path = os.path.join(root_path, category)
                        shutil.move(file_path, category_path)

            if not known_extension_found:
                category_files['unknown_extensions'].append(os.path.splitext(file)[1].lower())
                unknown_extensions.append(os.path.splitext(file)[1].lower())
                category_path = os.path.join(root_path, 'unknown_extensions')
                shutil.move(file_path, category_path)

    return category_files, known_extensions, unknown_extensions

def normalize(path):
    cyrillic_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    latin_symbols = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    
    trans_map = dict(zip(map(ord, cyrillic_symbols), latin_symbols))

    for c, l in zip(cyrillic_symbols, latin_symbols):
        trans_map[ord(c)] = l
        trans_map[ord(c.upper())] = l.upper()
        trans_map[ord(c.lower())] = l.lower()
    
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        base_name, extension = os.path.splitext(file)
        normalized_name = base_name.translate(trans_map)
        normalized_name = ''.join([ch if ch.isalnum() else '_' for ch in normalized_name])
        new_file_name = normalized_name + extension
        new_file_path = os.path.join(path, new_file_name)
        os.rename(file_path, new_file_path)
        
def remove_empty_folders(path):
    if os.path.exists(path) and os.path.isdir(path):
        for i in os.listdir(path):
            i_joined_path = os.path.join(path, i)
            if os.path.isdir(i_joined_path) and (not i in list_of_directories):
                entry_path = os.path.join(path, i)
                os.rmdir(entry_path)
   
def main(): 
    if len(sys.argv) < 2:
        path = ''
    else:
        path = sys.argv[1]
    
    make_directory(path)
    get_files(path, path)
    remove_empty_folders(path)

if __name__ == "__main__":
    main()
