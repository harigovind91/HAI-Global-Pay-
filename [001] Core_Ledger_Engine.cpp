#include <iostream>
#include <map>
#include <string>
#include <vector>

class HAICoreLedger {
private:
    std::map<std::string, double> balance_vault;
    // आपकी नई मास्टर की (इसे असल में .env से लोड होना चाहिए)
    const std::string MASTER_KEY = "HAI-Admin@786#X";
    std::vector<std::string> transaction_logs;

public:
    // सुरक्षा जांच (Authentication)
    bool authenticate(std::string key) {
        return key == MASTER_KEY;
    }

    void creditAccount(std::string account_id, double amount, std::string key) {
        if (!authenticate(key)) {
            std::cout << "🚨 [ALERT] Unauthorized Access Attempted!\n";
            return;
        }
        balance_vault[account_id] += amount;
        transaction_logs.push_back("CREDIT: " + account_id + " Amount: " + std::to_string(amount));
        std::cout << "✅ Amount Credited Successfully.\n";
    }

    bool transfer(std::string from, std::string to, double amount, std::string key) {
        if (!authenticate(key)) return false;

        if (balance_vault[from] >= amount) {
            balance_vault[from] -= amount;
            balance_vault[to] += amount;
            transaction_logs.push_back("TRANSFER: From " + from + " To " + to + " Amt: " + std::to_string(amount));
            return true;
        }
        return false;
    }

    void showStatus(std::string account_id) {
        std::cout << "--- HAI Global Pay Ledger ---\n";
        std::cout << "Account: " << account_id << " | Balance: $" << balance_vault[account_id] << "\n";
    }
};

int main() {
    HAICoreLedger haiPay;
    
    // टेस्ट ट्रांजेक्शन
    std::string myKey = "HAI-Admin@786#X";
    
    haiPay.creditAccount("HARI_CEO_01", 1000000.0, myKey);
    haiPay.showStatus("HARI_CEO_01");

    return 0;
}

