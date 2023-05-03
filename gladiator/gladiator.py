from flask import (
    Blueprint, render_template, request, flash
)

from gladiator.services.gladiator_interface import GladiatorInterface
from gladiator.services.gladiator_module import injector

bp = Blueprint('gladiator', __name__)

gladiator = injector.get(GladiatorInterface)


@bp.route('/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        prompt = request.form['prompt']
        error = None

        if not prompt:
            error = 'Original prompt is required.'

        if error is not None:
            flash(error)
        else:
            best_id = 0
            success, message, replies = gladiator.run(prompt)
            if not success:
                flash(message)
            else:
                best_id = sorted(replies, key=lambda r: r.confidence, reverse=True)[0].number
            return render_template('index.html', prompt=prompt, prompt_replies=replies, best_id=best_id)

    return render_template('index.html')
