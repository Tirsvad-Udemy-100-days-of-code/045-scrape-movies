from scrape_movies import constants


def test_constants_when_imported_point_into_project() -> None:
    assert constants.PROJECT_ROOT.name
    assert constants.FIXTURES_DIR.parent.name == "tests"
