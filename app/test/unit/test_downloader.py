import unittest
from app.bot.downloader import *


class TestDownloader(unittest.TestCase):

    def test_download_requirements(self):
        # it should download requirements for a valid requirements file
        try:
            download_requirements('requirements.txt')
        except Exception:
            self.fail('Failed to DL requirements')

    def test_download_requirements_nf(self):
        # it should throw a FileNotFound error if the requirements file
        # does not exist on the local system
        err = 'Expected {}'.format(FileNotFoundError.__name__)
        try:
            download_requirements('not a real file')
        except FileNotFoundError:
            pass
        except Exception:
            self.fail(err)
        else:
            self.fail(err)

    def test_download_requirements_err(self):
        # it should throw a RequirementDownloaderException if the
        # requirements file fails during install
        err = 'Expected {}'.format(RequirementDownloaderException.__name__)
        try:
            download_requirements('app/test/resources/requirements.txt')
        except RequirementDownloaderException:
            pass
        except Exception:
            self.fail(err)
        else:
            self.fail(err)