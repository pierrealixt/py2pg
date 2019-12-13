import unittest



def satisfy_dependency(package):
    """Install a package if not present.

    plpython installs packages here:
    /var/lib/postgresql/.local/lib/python3.7/site-packages/

    """
    import subprocess
    import importlib

    try:
        importlib.import_module(package)
    except ModuleNotFoundError:
        subprocess.check_call(["pip3", "install", package])



class Test(unittest.TestCase):

    def test_known_package(self):
        self.package = 'falcon'

        with self.assertRaises(ModuleNotFoundError):
            importlib.import_module(self.package)

        satisfy_dependency(self.package)

        assert importlib.import_module(self.package)

        # uninstall the package
        subprocess.check_call(["pip3", "uninstall", "-y", self.package])

    def test_unknown_package(self):
        self.package = 'i-do-not-exist'

        satisfy_dependency(self.package)

    # def tearDown(self):

