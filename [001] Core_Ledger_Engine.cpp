#include <iostream>
#include <map>
#include <string>

class HAICoreLedger {
private:
    std::map<std::string, double> balance_vault;
    std::string master_key = "HAI_PAY_99_ALPHA_SECURE";

public:
    void creditAccount(std::string account_id, double amount) {
        balance_vault[account_id] += amount;
    }

    bool transfer(std::string from, std::string to, double amount) {
        if (balance_vault[from] >= amount) {
            balance_vault[from] -= amount;
            balance_vault[to] += amount;
            return true;
        }
        return false;
    }

    double getBalance(std::string account_id) {
        return balance_vault[account_id];
    }
};

