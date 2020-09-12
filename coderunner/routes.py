from coderunner import coderunner, db
from flask import render_template, request, flash, redirect, url_for
from coderunner.models import FileContents, User
import time
import subprocess
# routes
@coderunner.route('/')
def main():
    coderunner.logger.info('Debug info: coderunner.logger.info')
    return render_template("index.html")


@coderunner.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['inputFile']

        if '.cpp' not in file.filename:
            return render_template('500.html'), 500

        # converts the input to the record
        newFile = FileContents(filename=file.filename, data=file.read())
        db.session.add(newFile)
        db.session.commit()
        flash('uploaded and running')
        return redirect('/result')
    else:
        return render_template('upload.html')

# Comile classes and display result
@coderunner.route('/result', methods=['GET'])
def compileRun():
    files = FileContents.query.all()

    with open('./coderunner/fileStorage/runner.cpp', 'wb') as file:
        file.write(files[-1].data)
    # the cpp file is copied into a container
    # client = docker.from_env()

    start = time.time()
    output = subprocess.check_output(
        ['sudo', 'docker-compose', 'run', '--rm', 'sandbox']).decode("utf-8")
    end = time.time()

    return render_template('result.html', filename=files[-1].filename, filecontents=files[-1].data.decode('ascii'), runtime='%3.2f seconds' % (end - start), output=output)
