from flask import render_template


def page_not_found(e):
    return render_template('front/404.html')


def register_err_handlers(app):
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, page_not_found)
