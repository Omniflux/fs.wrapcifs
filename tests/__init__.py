from pkgutil import extend_path

import fs

fs.__path__ = extend_path(fs.__path__, 'fs')