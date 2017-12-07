from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, usd

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///charitychange.db")


@app.route("/")
@login_required
def index():
    transactions = db.execute("SELECT * from transactions WHERE id=:id", id=session["user_id"])

    return render_template("index.html", transactions=transactions)

@app.route("/donate", methods=["GET", "POST"])
@login_required
def donate():
    """Confirm donation"""

     # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("firstname"):
            return apology("Missing first name!")

        # Ensure password was submitted
        elif not request.form.get("lastname"):
            return apology("Missing last name!")

        # Ensure charity was submitted
        elif not request.form.get("charity"):
            return apology("Missing charity!")


        # Ensure address was submitted
        elif not request.form.get("address"):
            return apology("Missing address!")

        # Ensure card number was submitted
        elif not request.form.get("cardnumber"):
            return apology("Missing card number!")

        # Ensure card type was submitted
        elif not request.form.get("cardtype"):
            return apology("Missing card type!")

        # Ensure cvc was submitted
        elif not request.form.get("cvc"):
            return apology("Missing CVC!")

        # Ensure expiration date was submitted
        elif not request.form.get("expirdate"):
            return apology("Missing expiration date!")

        # Ensure expiration date was submitted
        elif not request.form.get("amount"):
            return apology("Missing amount, you scrooge!")

        # Insert the elements into payments database
        payment_result = db.execute("INSERT INTO payments (firstname, lastname, address, cardnumber, cardtype, cvc, expirdate, charity, amount) \
                    VALUES(:firstname, :lastname, :address, :cardnumber, :cardtype, :cvc, :expirdate, :charity, :amount)", firstname=request.form.get("firstname"), lastname=request.form.get("lastname"), address=request.form.get("address"), cardnumber=request.form.get("cardnumber"), cardtype=request.form.get("cardtype"), cvc=request.form.get("cvc"), expirdate=request.form.get("expirdate"), charity=request.form.get("charity"), amount=request.form.get("amount"))
        if not payment_result:
            return apology("Could not input payment processing, try again!")

        transaction_result = db.execute("INSERT INTO transactions (charity, amount, id) \
                    VALUES(:charity, :amount, :id)", charity=request.form.get("charity"), amount=request.form.get("amount"),id=session["user_id"])

        if not transaction_result:
            return apology("Could not properly store this transaction, sorry!")

        # Redirect user to home page
        return render_template("donated.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("donate.html")

@app.route("/transactions")
@login_required
def transactions():
    """Show history of transactions"""

    transactions = db.execute("SELECT * from transactions WHERE id=:id", id=session["user_id"])

    return render_template("transactions.html", transactions=transactions)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Missing username!")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Missing password!")

        password = request.form.get("password")

        # Verify that the password must be a certain length
        if "%" not in password and "!" not in password and "*" not in password and "@" not in password and len(password) < 7:
            return apology("Your password must include special characters!")

        # Check passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match!")

        # Insert the new user into users, store hash of the password
        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",
                            username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))

        if not result:
            return apology("This username is already taken!")

        # Logs the user in after registration
        session["user_id"] = result

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
