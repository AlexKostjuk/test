import unittest
from app_test import BankAccount, InsufficientFunds


class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount(initial_balance=100)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)


    def test_minus_deposit(self):
        account = BankAccount(initial_balance=300)
        with self.assertRaises(ValueError):
                account.deposit(-50)

    def test_nol_deposit(self):
        account = BankAccount(initial_balance=300)
        with self.assertRaises(ValueError):
                account.deposit(0)

    def test_withdraw(self):
        account = BankAccount(initial_balance=200)
        account.withdraw(100)
        self.assertEqual(account.get_balance(), 100)



    def test_withdraw_minus_negative_amount(self):
        account = BankAccount(initial_balance=500)
        with self.assertRaises(ValueError):
            account.withdraw(-50)

    def test_withdraw_insufficient_funds(self):
        account = BankAccount(initial_balance=400)
        with self.assertRaises(InsufficientFunds):
            account.withdraw(500)


    def test_transfer_other_account_false(self):
        account = BankAccount(initial_balance=400)
        other_account = False
        with self.assertRaises(TypeError):
            account.transfer(other_account,100)

    def test_transfer_other_account_true(self):
        account = BankAccount(initial_balance=400)
        other_account = BankAccount(initial_balance=200)

        account.transfer(other_account, 100)
        self.assertEqual(other_account.get_balance(), 300)


    def test_transfer_other_account_true_amoumd_nol(self):
        account = BankAccount(initial_balance=400)
        other_account = BankAccount(initial_balance=200)
        with self.assertRaises(ValueError):
            account.transfer(other_account, 0)


    def test_transfer_other_account_true_amoumd_minus(self):
        account = BankAccount(initial_balance=400)
        other_account = BankAccount(initial_balance=200)
        with self.assertRaises(ValueError):
            account.transfer(other_account, -1)


    def test_transfer_other_account_true_insufficient_funds(self):
        account = BankAccount(initial_balance=50)
        other_account = BankAccount(initial_balance=200)

        with self.assertRaises(InsufficientFunds):
            account.transfer(other_account,100)


if __name__ == "__main__":
    unittest.main()


