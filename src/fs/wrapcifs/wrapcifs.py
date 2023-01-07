"""Makes a Filesystem with case insensitive lookups."""

from typing import Generic, Mapping, TypeVar

from fs.base import FS
from fs.path import combine, iteratepath, normpath
from fs.wrapfs import WrapFS

_F = TypeVar("_F", bound=FS, covariant=True)

class WrapCaseInsensitive(WrapFS[_F], Generic[_F]):
	"""Makes a Filesystem with case insensitive lookups.
	
	Arguments:
		fs (FS): A filesystem instance.
	Returns:
		FS: A case insensitive version of ``fs``

	Note:
		If multiple entries in ``fs`` match the same case insensitive name,
		if `path` matches an existing case sensitive path, it is used,
		otherwise the first matching path is used.
	"""

	wrap_name = "case-insensitive"

	def __init__(self, wrap_fs: _F) -> None:
		super().__init__(wrap_fs)
		self._passthru = self.delegate_fs().getmeta()['case_insensitive']

	def delegate_path(self, path: str) -> tuple[_F, str]:
		if not self._passthru and not self.delegate_fs().exists(path):
			if (new_path := self.checkpath(iteratepath(normpath(path)))):
				path = new_path
		
		return self._wrap_fs, path

	def checkpath(self, testing_path: list[str], current_path: str = '/') -> str | None:
		if not len(testing_path):
			return current_path

		try:
			directory_entries = self.delegate_fs().listdir(current_path)
		except Exception:
			directory_entries = []

		for entry in directory_entries:
			if entry.lower() == testing_path[0].lower() and (new_path := self.checkpath(testing_path[1:], combine(current_path, entry))):
				return new_path

		return None

	def getmeta(self, namespace: str = "standard") -> Mapping[str, object]:
		meta = dict(self.delegate_fs().getmeta(namespace))

		if not self._passthru and namespace == "standard":
			meta.update(case_insensitive=True)

		return meta