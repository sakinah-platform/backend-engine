
ALLOWED_IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png']


def rel_path(media_path, assigned_filename, ext):
    relpath = '{media_path}/{filename}'
    new_path = relpath.format(media_path=media_path,
                              filename=assigned_filename)

    return new_path + ext
