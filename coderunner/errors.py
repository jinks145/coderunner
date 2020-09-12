from flask import render_template
from coderunner import coderunner
@coderunner.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@coderunner.errorhandler(500)
def runtime_error(error):
    return render_template('500.html'), 500
