import pytest
from FreezeLibs import FreezeLibs

def test_extract_imports():
    freeze_libs = FreezeLibs()
    imports = freeze_libs.extract_imports("test.py")
    expected_imports = {"cv2", "matplotlib", "pandas", "numpy", "PIL", "yaml", "sklearn", "bs4", "dateutil"}
    assert imports == expected_imports

def test_get_install_name():
    freeze_libs = FreezeLibs()
    assert freeze_libs.get_install_name("cv2") == "opencv-python"
    assert freeze_libs.get_install_name("PIL") == "Pillow"
    assert freeze_libs.get_install_name("unknown_lib") == "unknown_lib"