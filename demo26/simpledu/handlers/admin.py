from flask import Blueprint , render_template , request,current_app , flash , redirect , url_for
from simpledu.decorators import admin_required
from simpledu.modes import Course ,db ,User,Live , Message
from simpledu.forms import CourseForm ,UserForm ,UserForm1 ,LiveForm ,MessageForm

admin = Blueprint('admin',__name__,url_prefix='/admins')


@admin.route('')
@admin_required
def index():
    return render_template('admin/index.html')


@admin.route('/courses')
@admin_required
def courses():
    page = request.args.get('page',default=1,type=int)
    pagination = Course.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return  render_template('admin/courses.html',pagination=pagination)


@admin.route('/courses/create',methods=['GET','POST'])
@admin_required
def create_course():
    form = CourseForm()
    if form.validate_on_submit():
        form.create_course()
        flash('课程创建成功','success')
        return redirect(url_for('.courses'))
    return render_template('admin/create_course.html',form=form)

@admin.route('/courses/update/<int:course_id>',methods=['GET','POST'])
@admin_required
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    form = CourseForm(obj=course)
    if form.validate_on_submit():
        form.update_course(course)
        flash('课程创建成功','success')
        return redirect(url_for('.courses'))
    return render_template('admin/update_course.html',form=form,course=course)

@admin.route('/courses/delete/<int:course_id>',methods=['GET','POST'])
@admin_required
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    flash('{} 删除成成'.format(course.name),'success')
    return redirect(url_for('admin.courses'))

@admin.route('/users')
@admin_required
def users():
    page = request.args.get('page',default=1,type=int)
    pagination = User.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return  render_template('admin/users.html',pagination=pagination)

@admin.route('/users/create',methods=['GET','POST'])
@admin_required
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        form.create_user()
        flash('用户创建成功','success')
        return redirect(url_for('.users'))
    return render_template('admin/create_user.html',form=form)



@admin.route('/users/update/<int:user_id>',methods=['GET','POST'])
@admin_required
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm1(obj=user)
    if form.validate_on_submit():
        form.update_user(user)
        flash('用户修改成功','success')
        return redirect(url_for('.users'))
    return render_template('admin/update_user.html',form=form,user=user)

@admin.route('/users/delete/<int:user_id>',methods=['GET','POST'])
@admin_required
def delete_users(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('{} 删除成成'.format(user.username),'success')
    return redirect(url_for('admin.users'))


@admin.route('/live')
@admin_required
def lives():
    page = request.args.get('page',default=1,type=int)
    pagination = Live.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return  render_template('admin/lives.html',pagination=pagination)


@admin.route('/live/create',methods=['GET','POST'])
@admin_required
def create_live():
    form = LiveForm()
    if form.validate_on_submit():
        form.create_live()
        flash('直播创建成功','success')
        return redirect(url_for('.lives'))
    return render_template('admin/create_live.html',form=form)


@admin.route('/live/delete/<int:live_id>',methods=['GET','POST'])
@admin_required
def delete_live(live_id):
    live = Live.query.get_or_404(live_id)
    db.session.delete(live)
    db.session.commit()
    flash('{} 删除成成'.format(live.name),'success')
    return redirect(url_for('admin.lives'))




@admin.route('/messages')
@admin_required
def messages():
    page = request.args.get('page',default=1,type=int)
    pagination = Message.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return  render_template('admin/messages.html',pagination=pagination)


@admin.route('/message/create',methods=['GET','POST'])
@admin_required
def create_message():
    form = MessageForm()
    if form.validate_on_submit():
        form.create_message()
        flash('消息创建成功','success')
        return redirect(url_for('.messages'))
    return render_template('admin/create_messages.html',form=form)



@admin.route('/message/delete/<int:message_id>',methods=['GET','POST'])
@admin_required
def delete_message(message_id):
    message = Message.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    flash('{} 删除成成'.format(message.message),'success')
    return redirect(url_for('admin.messages'))