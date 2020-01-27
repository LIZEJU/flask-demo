from flask import Blueprint , render_template , request,current_app , flash , redirect , url_for
from simpledu.decorators import admin_required
from simpledu.modes import Course ,db
from simpledu.forms import CourseForm

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