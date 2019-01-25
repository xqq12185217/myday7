import allure
class Test_01:
    @allure.step(title="test_01")
    def test_01(self):
        print("test_01")
        assert True

    @allure.step(title="test_02")
    def test_02(self):
        print("test_02")
        assert False