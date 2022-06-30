from flask import Flask, render_template, session,redirect
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

app.secret_key="one"

@app.route('/')
def home():
    return redirect('/counter')

@app.route('/counter')          # The "@" decorator associates this route with the function immediately following
def counter():
    if 'count' not in session:
        session['count'] =0
    else:
        session['count'] +=1
    return render_template("index.html")



@app.route('/reset')          
def reset():
    session.clear()		# clears all keys
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.