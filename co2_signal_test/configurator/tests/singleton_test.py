import singleton
import pytest


class ChildSingleton(singleton.Singleton):
    @singleton.Singleton._init_deco
    def __init__(self):
        self.test_param = 10


class IncorrectChildSingleton(singleton.Singleton):
    def __init__(self):
        self.test_param = 20


class NoinitChildSingleton(singleton.Singleton):
    pass



class TestSingleton:
    def test_correct_usage(self):
        test_singleton = ChildSingleton()
        # check that singleton created
        assert not (test_singleton is None)

        # check that singleton inited
        assert (test_singleton.test_param == 10)

        # check that singleton not reinited
        test_singleton.test_param = 20
        test_singleton1 = ChildSingleton()
        assert (test_singleton.test_param == 20)

        # check that singleton always the same
        assert (test_singleton is test_singleton1)
        test_singleton.test_param = 22
        assert (test_singleton1.test_param == 22)
        test_singleton1.test_param = 21
        assert (test_singleton.test_param == 21)

    def test_incorrect_inheritance(self):
        # check that singleton not reinited
        test_singleton2 = IncorrectChildSingleton()
        test_singleton2.test_param = 30
        test_singleton1 = IncorrectChildSingleton()
        assert (test_singleton2.test_param == 20)

        with pytest.raises(Exception):
            test_singleton = NoinitChildSingleton()
