import razorpay
from flask import Flask, render_template

app = Flask(__name__)

razorpay_client = razorpay.Client(auth=("rzp_test_7eGY4KQm08ncO4", "fOOTwKuiyxR11W6D4vVBVNjj"))

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/checkout")
def checkout():
    order_data = {
        "amount": 19900,
        "currency": "INR",
        "payment_capture": 1
    }
    order = razorpay_client.order.create(order_data)
    return render_template("checkout.html", order=order)

@app.route("/thank-you")
def thank_you():
    return "<h1>Thank you for your purchase! Your book will bw sent to you. </h1>"

if __name__ == "__main__":
    app.run(debug=True)
