import pytest

from fs.memoryfs import MemoryFS
from fs.wrapcifs import WrapCaseInsensitive

@pytest.fixture(scope="module")
def filesystem() -> WrapCaseInsensitive[MemoryFS]:
	memoryFS = MemoryFS()
	memoryFS.create('ABC')
	memoryFS.create('AbC')

	return WrapCaseInsensitive(memoryFS)

def test_metadata(filesystem: WrapCaseInsensitive[MemoryFS]) -> None:
	assert filesystem.getmeta()['case_insensitive'] == True

def test_access(filesystem: WrapCaseInsensitive[MemoryFS]) -> None:
	assert [n.name for n in filesystem.scandir('')] == ['ABC', 'AbC']

	assert not filesystem.exists('ab')

	for name in ['abc', 'ABC', 'AbC']:
		assert filesystem.exists(name)

	assert filesystem.getinfo('abc').name == 'ABC'
	assert filesystem.getinfo('ABC').name == 'ABC'
	assert filesystem.getinfo('AbC').name == 'AbC'