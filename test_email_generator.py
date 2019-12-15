
import pytest 
import emailGenerator 

emailGeneratorClass = emailGenerator.emailGenerator("@paragraph.ai")

def test_toLower():
    test = 'Makan Malam Malam'
    expected = 'makan malam malam'
    assert emailGeneratorClass.toLower(test) == expected

def test_split():
    test = "makan malam sini sama aku"
    expected = ['makan', 'malam', 'sini', 'sama', 'aku']
    assert emailGeneratorClass.split(test) == expected

def test_oneWordName():
    words = ['mirdan']
    number = 1
    expected = 'mirdan1'
    assert emailGeneratorClass.oneWordName(words, number) == expected

def test_moreThanOneWord():
    words = ['aku', 'sekarang', 'laper']
    number = 2
    expected = 'aku.laper2'
    assert emailGeneratorClass.moreThanOneWord(words, number) == expected

def test_generateEmailName():
    words = 'nama.depan'
    expected = 'nama.depan@paragraph.ai'
    assert emailGeneratorClass.generateEmailName(words) == expected

 

