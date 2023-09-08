from flask import Flask, render_template, redirect, session, request, flash
from flask_session import Session
import secrets
import crud
from model import connect_to_db, db

app = Flask(__name__)
app.app_context().push()
app.secret_key = secrets.token_hex(16)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def render_home():
    return render_template('home.html')


@app.route('/label/<level>')
def render_labeller(level):
    session.clear()

    if level == '0':
        session['job_ids'] = crud.get_advanced_job_ids()   
    elif level == '1':
        session['job_ids'] = crud.get_entry_job_ids()
    elif level == '-1':
        session['job_ids'] = crud.get_uncertain_job_ids()
    else:
        session['job_ids'] = crud.get_unlabelled_job_ids()

    job_id = session['job_ids'][-1]

    return redirect(f'/label_entry/{job_id}')


@app.route('/label_entry/<job_id>')
def render_label_job(job_id):
    job = crud.get_job(job_id)
    count = crud.get_labelled_count()

    return render_template('label_job.html', job=job, count=count)


@app.route('/update')
def label_job():
    if not session.get('job_ids'):
        flash('Error: Session timeout.')

        return redirect('/')
    
    crud.update_job_label(request.args.get('job_id'), request.args.get('label'))
    session['job_ids'].pop()

    if not session['job_ids']:
        flash('All labelling complete.')
        return redirect('/')
    
    job_id = session['job_ids'][-1]
    print(len(session['job_ids']))
    return redirect(f'/label_entry/{job_id}')


if __name__ == '__main__':
    connect_to_db(app, 'li-job-data', echo=True)
    app.run(host='0.0.0.0', debug=True)