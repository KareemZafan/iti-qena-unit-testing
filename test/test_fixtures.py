import pytest

@pytest.fixture(autouse=True,scope='module')
def create_new_session():
    print("\nOpening DB session")

def test_insert():
    print("\nInserting ....")
    assert 1 > 0 


def test_update():
    print("\nUpdating ....")
    assert 1 > 0 


def test_delete():
    print("\nDeleting ....")
    assert 1 > 0 



@pytest.fixture(autouse=True,scope='module')
def close_session():
    yield
    print("\nClosing DB session")