from rtrim import right_trim


class TestRtrim:

    def test_testing_works(self):
        assert True is True

    def test_returns_abc_when_abc_passed(self):
        text = "abc"

        actual = right_trim(text)
        expected = "abc"

        assert actual == expected

    def test_returns_bcd_when_bcd_passed(self):
        text = "bcd"

        actual = right_trim(text)
        expected = "bcd"

        assert actual == expected

    def test_deletes_space_from_the_end_of_string(self):
        text = "bcd "

        actual = right_trim(text)
        expected = "bcd"

        assert actual == expected

    def test_deletes_tab_from_the_end_of_string(self):
        text = "bcd\t"

        actual = right_trim(text)
        expected = "bcd"

        assert actual == expected

    def test_deletes_signs_from_the_end_of_line_followed_by_unix_newline_sign(self):
        text = "bcd\t\n"

        actual = right_trim(text)
        expected = "bcd\n"

        assert actual == expected
