from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message(message="edcba", key=2) == "abc_de"
    assert encrypt_message(message="edcba", key=3) == "cde_ab"
    assert encrypt_message(message="abcde", key=5) == "edcba"
    assert encrypt_message(message="edcba", key=5) == "abcde"
    assert encrypt_message(message="edcba", key=-5) == "abcde"
    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(message=12, key=2)
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message(message='edcba', key='2')
