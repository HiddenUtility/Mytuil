from pyutil.dummy.DateFileDummiyMaker import RandomDummyMaker
from pyutil.pathuil.DirectoryTreeRemover import DirectoryTreeRemover


from pathlib import Path

from pyutil.pathuil.directory_creator import DirectoryCreator


def test_DirectoryTreeRemover():
    target_path = Path('../dest/test.pyutil/DirectoryTreeRemover')
    DirectoryCreator(target_path,clear=True)

    maker = RandomDummyMaker(target_path)
    maker.create_file('LICENSE')
    maker.create_file('_test_hogehoge.py')

    gomi_maker = RandomDummyMaker(target_path)
    gomi_maker.create_file('hogehoge_test_hogehoge.py')
    gomi_maker.create_ramdom_files()
    gomi_maker.ramdom_create()


    DirectoryTreeRemover(target_path,
                            ignore_filename_patterns=['requirements.txt','LICENSE',r'_test(.+?)\.py'],
                            ignore_dirname_patterns=['libs', 'xsdbeditor.tests', 'xsappmanager.tests'],
                            ).run()
    
    for f in gomi_maker.get_created_filepaths():
        assert not f.exists(), f'{f}が消されてません'

    for f in maker.get_created_filepaths():
        assert f.exists(), f'{f}がありません'

