from rtrim import right_trim


class TestRtrim:

    def test_testing_works(self):
        assert True is True

    def test_rtrim_returns_abc_when_abc_passed(self):
        argument = "abc"

        actual = right_trim(argument)
        expected = "abc"

        assert actual == expected
