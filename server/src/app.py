import datetime

from flask import Flask, render_template, send_file

app = Flask(__name__)


def get_dates():
    today = datetime.date.today()
    bilimkana = (datetime.date(2023, 6, 1) - datetime.date(2022, 9, 1)).days
    developstoday = (datetime.date(2023, 2, 1) - datetime.date(2022, 8, 8)).days
    eso = (datetime.date(2022, 8, 8) - datetime.date(2021, 9, 14)).days
    cec = (datetime.date(2023, 7, 1) - datetime.date(2023, 3, 1)).days
    globalify = (today - datetime.date(2023, 6, 1)).days

    dates = {
        "bilimkana": bilimkana,
        "developstoday": developstoday,
        "eso": eso,
        "cec": cec,
        "globalify": globalify
    }
    return dates


def get_dates_ru():
    today = datetime.date.today()
    bilimkana = (datetime.date(2023, 6, 1) - datetime.date(2022, 9, 1)).days
    developstoday = (datetime.date(2023, 2, 1) - datetime.date(2022, 8, 8)).days
    eso = (datetime.date(2022, 8, 8) - datetime.date(2021, 9, 14)).days
    cec = (datetime.date(2023, 7, 1) - datetime.date(2023, 3, 1)).days
    globalify = (today - datetime.date(2023, 6, 1)).days

    dates = {
        "bilimkana": bilimkana,
        "developstoday": developstoday,
        "eso": eso,
        "cec": cec,
        "globalify": globalify
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


@app.get("/ru")
def ru():
    return render_template("home_ru.html", dates=get_dates_ru())


@app.get("/download")
def download():
    return send_file(
        "./static/elements/Arstanbek_Usenov_CV.pdf", as_attachment=True
    )
