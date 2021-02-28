from django.core.files.storage import DefaultStorage
from django.core.files import File, locks
from django.core.files.move import file_move_safe
import hashlib
import os


def upload_to(filename):
    """
    Кастомный upload_to используется для указания пути для
    хранилища картинок, т.к. дефолтный upload_to теперь не играет роли
    """
    return f"images/{filename[:2]}/{filename}"


class RewriteableStorageMixin(DefaultStorage):

    def _save(self, name, content):
        full_path = self.path(name)
        # Create any intermediate directories that do not exist.
        directory = os.path.dirname(full_path)
        try:
            if self.directory_permissions_mode is not None:
                # Set the umask because os.makedirs() doesn't apply the "mode"
                # argument to intermediate-level directories.
                old_umask = os.umask(0o777 & ~self.directory_permissions_mode)
                try:
                    os.makedirs(directory, self.directory_permissions_mode, exist_ok=True)
                finally:
                    os.umask(old_umask)
            else:
                os.makedirs(directory, exist_ok=True)
        except FileExistsError:
            raise FileExistsError('%s exists and is not a directory.' % directory)

        # There's a potential race condition between get_available_name and
        # saving the file; it's possible that two threads might return the
        # same name, at which point all sorts of fun happens. So we need to
        # try to create the file, but if it already exists we have to go back
        # to get_available_name() and try again.

        while True:
            try:
                # This file has a file path that we can move.
                if hasattr(content, 'temporary_file_path'):
                    file_move_safe(content.temporary_file_path(), full_path)

                # This is a normal uploadedfile that we can stream.
                else:
                    # The current umask value is masked out by os.open!
                    fd = os.open(full_path, self.OS_OPEN_FLAGS, 0o666)
                    _file = None
                    try:
                        locks.lock(fd, locks.LOCK_EX)
                        for chunk in content.chunks():
                            if _file is None:
                                mode = 'wb' if isinstance(chunk, bytes) else 'wt'
                                _file = os.fdopen(fd, mode)
                            _file.write(chunk)
                    finally:
                        locks.unlock(fd)
                        if _file is not None:
                            _file.close()
                        else:
                            os.close(fd)
            except FileExistsError:
                # A new name is needed if the file exists.
                break
            else:
                # OK, the file save worked. Break out of the loop.
                break

        if self.file_permissions_mode is not None:
            os.chmod(full_path, self.file_permissions_mode)

        # Store filenames with forward slashes, even on Windows.
        return str(name).replace('\\', '/')


class HashedImageStorage(RewriteableStorageMixin):
    """
    Кастомный стораж для наших картинок
    """

    def save(self, name, content, max_length=None):
        """
        Заменяем дефолт нейм на хеш.
        Кстати upload_to теперь не ворк если юзать этот стораж
        """
        name = f"{hashlib.md5(content.read()).hexdigest()}.{content.content_type.split('/')[-1]}"
        name = upload_to(name)
        if not hasattr(content, 'chunks'):
            content = File(content, name)
        return self._save(name, content)


class WebpStorage(RewriteableStorageMixin):
    """
    А это кастомный стораж для вебп чтобы они не плодились по 10001000 раз
    (отключает попытки создания новых файлов если файл с таким именем существует)
    """

    def save(self, name, content, max_length=None):
        """
        Заменяем дефолт нейм на хеш.
        Кстати upload_to теперь не ворк если юзать этот стораж
        """
        if name is None:
            name = content.name
        if not hasattr(content, 'chunks'):
            content = File(content, name)
        return self._save(name, content)
