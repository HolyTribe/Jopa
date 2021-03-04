from django.conf import settings
from subprocess import Popen
import os


def convert_to_webp(image_path, output_path, quality=90):
    proc = Popen([os.path.normpath(os.path.join(settings.BASE_DIR, 'apps/commons/libs/webp', 'cwebp.exe')),
                  os.path.normpath(image_path),
                  '-o', os.path.normpath(output_path),
                  '-q', str(quality)])
    proc.wait()
    return proc.returncode == 0
