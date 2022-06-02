import pytest
import os
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    test_user1 = Director(id=1, name='Иван')
    test_user2 = Director(id=2, name='Петр')
    test_user3 = Director(id=3, name='Тест')

    director_dao.query = MagicMock()
    director_dao.get_one = MagicMock(return_value=test_user1)
    director_dao.get_all = MagicMock(return_value=[test_user1, test_user2, test_user3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "name": "TEST"
        }

        director = self.director_service.create(director_d)

        assert director.id is not None

    def test_update(self):
        director_d = {
            "id":3,
            "name":"Test update"
        }
        self.director_service.update(director_d)

    def test_delete(self):
        self.director_service.delete(1)

if __name__ =="__main__":
    os.system("pytest")
