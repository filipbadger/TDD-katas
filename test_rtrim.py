from rtrim import right_trim


class TestRtrim:

    def test_testing_works(self):
        assert True is True

    def test_returns_abc_when_abc_passed(self):
        argument = "abc"

        actual = right_trim(argument)
        expected = "abc"

        assert actual == expected

    def test_returns_bcd_when_bcd_passed(self):
        argument = "bcd"

        actual = right_trim(argument)
        expected = "bcd"

        assert actual == expected

    def test_deletes_space_from_the_end_of_string(self):
        argument = "bcd "

        actual = right_trim(argument)
        expected = "bcd"

        assert actual == expected

    def test_deletes_tab_from_the_end_of_string(self):
        argument = "bcd\t"

        actual = right_trim(argument)
        expected = "bcd"

        assert actual == expected

    def test_