from app import version


def test_version_is_declared():
    """응답에 사용할 프로젝트 버전이 선언되어 있어야 한다."""
    assert version().count(".") == 2
