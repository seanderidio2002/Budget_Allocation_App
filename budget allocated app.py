# # ==============================
# Class: Expense
# ==============================
class Expense:
    def __init__(self, expense_name: str, amount: float, date: str):
        self.expense_name: str = expense_name
        self.amount: float = amount
        self.date: str = date

    def getExpense(self):
        return f"{self.expense_name} - ₱{self.amount:.2f} on {self.date}"


# ==============================
# Class: Budget
# ==============================
class Budget:
    def __init__(self, budget_amount: float = 0.0, budget_type: str = "Not Set"):
        self.budget_amount: float = budget_amount
        self.type: str = budget_type

    def setBudget(self, amount: float, budget_type: str):
        self.budget_amount: float = amount
        self.type: str = budget_type

    def getBudget(self):
        return f"Budget Type: {self.type}, Amount: ₱{self.budget_amount:.2f}"


# ==============================
# Class: User
# ==============================
class User:
    def __init__(self, name: str):
        self.name: str = name
        self.budget: Budget = Budget()   
        self.expenses: list[Expense] = []

    def setBudget(self, amount: float, budget_type: str):
        if amount < 0:
            print("Budget cannot be negative.")
            return
        self.budget.setBudget(amount, budget_type)
        print("Budget set successfully!")

    def addExpense(self, expense_name: str, amount: float, date: str):
        if amount < 0:
            print("Expense cannot be negative.")
            return
        expense = Expense(expense_name, amount, date)
        self.expenses.append(expense)
        print("Expense added successfully!")

    def viewExpense(self):
        if not self.expenses:
            print("No expenses found.")
        else:
            print("\n===== EXPENSE LIST =====")
            for i, exp in enumerate(self.expenses, start=1):
                print(f"{i}. {exp.getExpense()}")

    def getTotalExpenses(self):
        return sum(exp.amount for exp in self.expenses)


# ==============================
# Class: Dashboard
# ==============================
class Dashboard:
    def __init__(self, user):
        self.user = user

    def showDashboard(self):
        total_expenses = self.user.getTotalExpenses()
        budget_amount = self.user.budget.budget_amount
        remaining = budget_amount - total_expenses

        print("\n===== BUDGET DASHBOARD =====")
        print(f"User: {self.user.name}")
        print(f"Budget Type: {self.user.budget.type}")
        print(f"Total Budget: ₱{budget_amount:.2f}")
        print(f"Total Expenses: ₱{total_expenses:.2f}")
        print(f"Remaining Budget: ₱{remaining:.2f}")

        if budget_amount > 0:
            percent = (total_expenses / budget_amount) * 100
            bars = int(percent // 5)

            bars = min(bars, 20)  # limit to 20 bars

            progress_bar = "█" * bars + "-" * (20 - bars)

            print("\nBudget Usage:")
            print(f"[{progress_bar}] {percent:.2f}%")

            if percent > 100:
                print("Warning: Budget exceeded!")
            elif percent >= 80:
                print("Caution: Near budget limit.")
            else:
                print("Budget is under control.")
        else:
            print("Please set a budget first.")


# ==============================
# Class: Report
# ==============================
class Report:
    def __init__(self, user):
        self.user = user

    def displayReport(self):
        total_expenses = self.user.getTotalExpenses()
        remaining = self.user.budget.budget_amount - total_expenses

        print("\n===== REPORT PAGE =====")
        print(f"User: {self.user.name}")
        print(self.user.budget.getBudget())
        print(f"Total Expenses: ₱{total_expenses:.2f}")
        print(f"Remaining Budget: ₱{remaining:.2f}")

        print("\nExpense Details:")
        if not self.user.expenses:
            print("No expenses recorded.")
        else:
            for exp in self.user.expenses:
                print(f"- {exp.getExpense()}")

        if remaining < 0:
            print("\nYou exceeded your budget!")
        else:
            print("\nBudget is under control.")


# ==============================
# Expense Input Screen
# ==============================
def expenseInputScreen(user):
    print("\n===== EXPENSE INPUT SCREEN =====")

    expense_name = input("Enter Expense Name: ")

    try:
        amount = float(input("Enter Amount: ₱"))
    except ValueError:
        print("Invalid amount.")
        return

    date = input("Enter Date (MM/DD/YYYY): ")

    user.addExpense(expense_name, amount, date)


# ==============================
# Main Application
# ==============================
def main():
    print("===== EXPENSE TRACKER APPLICATION =====")

    name = input("Enter your name: ")
    user = User(name)

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Set Budget")
        print("2. Expense Input Screen")
        print("3. View Expenses")
        print("4. Budget Dashboard")
        print("5. Report Page")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter Budget Amount: ₱"))
            except ValueError:
                print("Invalid budget amount.")
                continue

            btype = input("Enter Budget Type (Monthly/Weekly): ")
            user.setBudget(amount, btype)

        elif choice == "2":
            expenseInputScreen(user)

        elif choice == "3":
            user.viewExpense()

        elif choice == "4":
            dashboard = Dashboard(user)
            dashboard.showDashboard()

        elif choice == "5":
            report = Report(user)
            report.displayReport()

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


# ==============================
# Run Program
# ==============================
if __name__ == "__main__":
    main()