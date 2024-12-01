from os import path


ALLOWED_IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png']


def rel_path(media_path, assigned_filename, ext):
    relpath = '{media_path}/{filename}'
    new_path = relpath.format(media_path=media_path,
                              filename=assigned_filename)

    return new_path + ext


def vendor_category_icon_paths(instance, curr_file):
    _, ext = path.splitext(curr_file)
    assigned_filename: str = instance.name.replace(' ', '')

    return rel_path('vendor_category_icons', assigned_filename, ext)


def vendor_profile_images(instance, curr_file):
    _, ext = path.splitext(curr_file)
    assigned_filename: str = instance.name.replace(' ', '')

    return rel_path('vendor_profile_images', assigned_filename, ext)


def vendor_galleries(_, curr_file):
    filename, ext = path.splitext(curr_file)

    return rel_path('vendor_galleries', filename, ext)
