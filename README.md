# ThinkIt — my Class 12 Python project

I built ThinkIt for my Class 12 high school final project in 2023, about three years ago. I wanted to see if I could make a little version of Blinkit with what I knew at the time: Python, some MySQL, and a terminal. You can sign up, pick groceries by item code, change quantities in your cart, and get a bill at the end.

When I opened it again, I’d forgotten more of the SQL than I expected. The original database lived on my laptop, so someone downloading the Python file had no catalog to shop from. This time I set up a Python virtual environment, added a dependency list, and included two SQL files you can download to recreate the database and try it yourself.

## What I used

- **Python basics.** Functions, loops, `if` and `elif` branches, lists, tuples, and terminal input. A category letter takes you to a product list, and the menu loops so you can keep shopping.
- **MySQL and SQL.** I used `SELECT` to find products and check logins, `INSERT` to save accounts and cart items, `UPDATE` to change quantities, and `DELETE` to remove items. The app uses parameterized queries to pass values like an item code separately from the SQL.
- **Billing and basic checks.** The bill adds up quantity × unit price for each item and applies a 5% discount from 500 or a 10% discount from 1,000. It checks for things like an empty cart and a duplicate signup. In this revisit I also switched the bill calculation to Python’s `Decimal` so it works with MySQL’s decimal prices.
- **Setting up a project someone else can run.** I used `venv` to keep the Python packages together and moved the database password into an environment variable so each person can use their own local MySQL login.

## Database files

- [`database/schema.sql`](database/schema.sql) creates the `thinkit_demo` database and its tables.
- [`database/seed.sql`](database/seed.sql) adds 26 fictional products across the 13 categories and promotions.

Both files are included if you clone the repo or download it as a ZIP. Run the schema first, then load the sample products once.

## Run it on Windows

I tested this with **Python 3.14 and MySQL Server 8.0.46**. You’ll need Python, a running local MySQL Server, and the MySQL command-line client. Open the project folder in PowerShell or in VS Code with **File → Open Folder**, then **Terminal → New Terminal**. Your terminal should show `PS` at the start of the prompt, and `project.py` should be in the current folder.

### 1. Set up Python once

In **PowerShell**, run these from the project folder:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 2. Set up MySQL once

Still in **PowerShell**, open MySQL with your administrator account:

```powershell
mysql -u root -p
```

If PowerShell can’t find `mysql`, use the full path to your installed `mysql.exe`. On my machine, that command is:

```powershell
& "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p
```

Enter your MySQL `root` password. Once you see the **`mysql>`** prompt, run these one at a time:

```sql
SOURCE database/schema.sql
SOURCE database/seed.sql
```

Still at **`mysql>`**, create the account the Python app will use. Replace `your-local-demo-password` with a password you choose for `thinkit_app`.

```sql
CREATE USER 'thinkit_app'@'localhost' IDENTIFIED BY 'your-local-demo-password';
GRANT SELECT, INSERT, UPDATE, DELETE ON thinkit_demo.* TO 'thinkit_app'@'localhost';
GRANT DROP ON thinkit_demo.cart TO 'thinkit_app'@'localhost';
GRANT DROP ON thinkit_demo.login TO 'thinkit_app'@'localhost';
EXIT;
```

The two `DROP` grants let the app empty the cart and login tables when it starts and after checkout. Use the separate demo database for this project.

### 3. Start ThinkIt

Back at the **`PS`** prompt, run this line and enter the password you chose for **`thinkit_app`**:

```powershell
$env:THINKIT_DB_PASSWORD = [System.Net.NetworkCredential]::new("", (Read-Host "Enter your thinkit_app password" -AsSecureString)).Password
```

Wait for the `PS` prompt to return, then run:

```powershell
.\.venv\Scripts\python.exe project.py
```

You should see **WELCOME TO THINKIT**. Set the password again when you open a new terminal.

## Try the mango-box checkout

Sign up with fictional details and log in. Choose **Select Items → A**, then add **two mango boxes** using code **101**. Choose **Bill**, answer **N** when asked if you want to keep shopping, and select **Cash**. With a subtotal of **550.00**, you should get a 5% discount and a final bill of **522.50**.

I still treat this as a school-project demo. It stores shopper passwords in plain text, so I use made-up details and the cash option when testing. The next change I’d like to make is saving completed orders. Then I can use pandas to answer questions like which category sells the most and how much shoppers spend per basket.
