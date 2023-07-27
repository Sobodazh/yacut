from flask import flash, redirect, render_template, request

from . import app, db
from .forms import СutForm
from .models import URLMap, get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = СutForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id()
        elif URLMap.query.filter_by(short=custom_id).first():
            form.custom_id.errors = [f'Имя {custom_id} уже занято!']
            return render_template('index.html', form=form)
        url = URLMap(
            original=form.original_link.data,
            short=custom_id,
        )
        db.session.add(url)
        db.session.commit()
        flash(f'{request.base_url}{custom_id}', 'link-messages')
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def cut_redirect(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original)