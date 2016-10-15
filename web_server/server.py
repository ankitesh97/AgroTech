from flask import Flask
import server_func

app = Flask(__name__)

@app.route("/user_auth")
def user_auth(query):
    print query
    # anmol's code
    valid = authentcate(username,password)
    if(valid):
      return {"status":"1"}

    return {"status":"0"}


if __name__ == "__main__":
	app.run()

