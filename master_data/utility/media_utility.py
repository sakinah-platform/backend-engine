from os import path

def vendor_category_icon_paths(instance, curr_file):

    _, ext = path.splitext(curr_file)

    vendor_category_icon_relpath = 'vendor_category_icons/{filename}'
    assigned_filename: str = instance.name.replace(' ','')
    new_path = vendor_category_icon_relpath.format(filename=assigned_filename)

    return new_path + ext
