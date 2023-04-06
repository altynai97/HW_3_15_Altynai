from app import app

from . import views

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/course/<int:course_id>', view_func=views.course_detail)


app.add_url_rule('/admin/course/create', view_func=views.admin_course_create, methods=['POST', 'GET'])
app.add_url_rule('/admin/student/create', view_func=views.admin_student_create, methods=['POST', 'GET'])
app.add_url_rule('/admin/course/list', view_func=views.admin_course_list)
app.add_url_rule('/admin/student/list', view_func=views.admin_student_list)
app.add_url_rule('/admin/course/<int:course_id>/update', view_func=views.admin_course_update, methods=['POST', 'GET'])
app.add_url_rule('/admin/student/<int:student_id>/delete', view_func=views.admin_student_delete, methods=['POST', 'GET'])
app.add_url_rule('/admin/course/<int:course_id>/update', view_func=views.admin_course_update, methods=['POST', 'GET'])
app.add_url_rule('/admin/student/<int:student_id>/delete', view_func=views.admin_student_delete, methods=['POST', 'GET'])

app.add_url_rule('/account/register', view_func=views.user_register, methods=['POST', 'GET'])
app.add_url_rule('/account/login', view_func=views.user_login, methods=['POST', 'GET'])
app.add_url_rule('/account/logout', view_func=views.user_logout)