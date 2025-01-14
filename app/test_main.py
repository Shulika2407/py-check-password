import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Pass@word1", True, id="one test"),
        pytest.param("Str@ng", False, id="two test"),
        pytest.param("qwerty1", False, id="three test"),

    ]
)
def test_check_password(password: str, result: bool) -> None:
    res = check_password(password)
    assert res == result
