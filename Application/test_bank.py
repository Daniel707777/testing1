import pytest
from bank import Account

def test_initial_balance():
    '''Tests the balance of a new account'''
    test_account1 = Account('dude')
    assert test_account1.balance == 0

def test_deposit():
    '''Tests the balance after a deposit'''
    test_account2 = Account('guy')
    test_account2.deposit(15)
    assert test_account2.balance == 15
    

def test_withdraw():
    '''Tests the balance after a withdraw'''
    test_account3 = Account('chad',100)
    test_account3.withdraw(20)
    assert test_account3.balance == 80

def test_deposit_negative_amount():
    '''Checks negative deposit error handling'''
    test_account4 = Account('bro')
    test_account4.deposit(-15)
    assert test_account2.balance == ValueError
    

def test_withdraw_more_than_balance():
     '''Checks negative deposit error handling'''
    test_account5 = Account('bud')
    test_account5.withdraw(15)
    

def test_withdraw_negative_amount():
