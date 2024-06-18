from flask import Flask, request, render_template
import random

app = Flask(__name__)

target = random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def home():
    global target
    message = "Guess a number between 1 and 100!"
    
    if request.method == 'POST':
        try:
            user_choice = int(request.form['guess'])
            if user_choice == target:
                message = "Success: Congratuation! you have Correct the Guess! You will start again Guessing ! more fun "
                target = random.randint(1, 100)  # Reset the target number
            elif user_choice < target:
                message = "Your number is too small. Try again!"
            else:
                message = "Your number is too big. Try again!"
        except ValueError:
            message = "Invalid input. Please enter a number."
    
    return render_template('guess.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)









