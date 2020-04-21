"""
Using terminal:
diff <(cat count.txt) <(python wordcount.py --count letras.txt)
diff <(cat count.txt) <(python wordcount.py --topcount letras.txt)
"""
import sys

from wordcount import main


def run(mode, capsys, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['wordcount.py', mode, 'letras.txt'])
    main()
    out, _ = capsys.readouterr()
    return out


def test_wordcount__count_from_file__return_a_2_b_4_c_3(capsys, monkeypatch):
    assert run('--count', capsys, monkeypatch) == 'a 2\nb 4\nc 3\n'


def test_wordcount__topcount_from_file__return_b_4_c_3_a_2(capsys, monkeypatch):
    assert run('--topcount', capsys, monkeypatch) == 'b 4\nc 3\na 2\n'
