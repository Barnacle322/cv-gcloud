from flask import Flask, render_template
import os
import datetime

app = Flask(__name__)

def get_dates():
    today = datetime.date.today()
    bilimkana = (today - datetime.date(2022, 9, 1)).days
    developstoday = (today - datetime.date(2022, 8, 8)).days
    eso = (today - datetime.date(2021, 9, 14)).days
    dates = {
        "bilimkana": bilimkana,
        "developstoday": developstoday,
        "eso": eso,
    }
    return dates

def get_dates_ru():
    today = datetime.date.today()
    bilimkana = (today - datetime.date(2022, 9, 1)).days
    developstoday = (today - datetime.date(2022, 8, 8)).days
    eso = (today - datetime.date(2021, 9, 14)).days

    dates = {
        "bilimkana": bilimkana,
        "developstoday": developstoday,
        "eso": eso,
    }

    for key, date in dates.items():
        if str(date)[-1] == "1":
            dates[key] = str(date) + " день"
        elif str(date)[-1] == "2" or str(date)[-1] == "3" or str(date)[-1] == "4":
            dates[key] = str(date) + " дня"
        else:
            dates[key] = str(date) + " дней"
    
    return dates


@app.get("/")
def home():
    return render_template("home.html", dates=get_dates())


@app.get('/ru')
def ru():
    return render_template("home_ru.html", dates=get_dates_ru())


if __name__ == "__main__":
    app.run(debug = True)#, host='0.0.0.0', port = int(os.environ.get('PORT', 8080)))