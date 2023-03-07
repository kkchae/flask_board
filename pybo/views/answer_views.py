from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g
from werkzeug.utils import redirect

from pybo import db
from ..forms import AnswerForm
from pybo.models import Question, Answer
from .auth_views import login_required


bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
@login_required
def create(question_id): # 매개변수 question_id는 URL에서 전달된다.
    # question = Question.query.get_or_404(question_id)

    # # form 엘리먼트를 통해 전달된 데이터들은 create 함수에서 request 객체로 얻을 수 있다.
    # # POST 폼 방식으로 전송된 데이터 항목 중 name 속성이 'content'인 값을 의미한다.
    # content = request.form['content']

    # answer = Answer(content=content, create_date=datetime.now())

    # question.answer_set.append(answer) # ‘질문에 달린 답변들’을 의미
    # # Question과 Answer 모델이 연결되어 backref에 설정한 answer_set을 사용할 수 있다.

    # db.session.commit()

    # # 답변을 생성한 후 화면을 이동하도록 redirect 함수를 사용
    # return redirect(url_for('question.detail', question_id=question_id))
    # # question_id는 question_views.py 파일에 있는 detail 함수의 매개변수로 전달
    
    # 폼 사용용
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now(), user=g.user)
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html', question=question, form=form)