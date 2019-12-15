
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
    expected = 'mirdan'
    assert emailGeneratorClass.oneWordName(words) == expected

def test_moreThanOneWord():
    words = ['aku', 'sekarang', 'laper']
    expected = 'aku.laper'
    assert emailGeneratorClass.moreThanOneWord(words) == expected

def test_generateUserName():
    user = "hubby"
    number = 123
    expect = 'hubby123'
    assert emailGeneratorClass.generateUserName(user, number) == expect

def test_generateEmailName():
    words = 'nama.depan'
    expected = 'nama.depan@paragraph.ai'
    assert emailGeneratorClass.generateEmailName(words) == expected

 

