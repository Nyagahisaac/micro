from ..models import User,Comment,Pitch
from . import main
from .. import db,photos
from flask import render_template,request,redirect,url_for,abort
from .forms import UpdateProfile
from flask_login import login_required,current_user



#.....
@main.route('/')
def index():
    
    '''
    View root page function that returns theindex page and its data
    '''
    
    title = "Pitch App"
    
    pitches = Pitch.get_all_pitch()
    
    return render_template('index.html', title = title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

# @main.route('/user/<uname>/update/pic',methods = ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.qury.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photo/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/new/<uname>', methods = ['GET','POST'])
@login_required
def new_pitch(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
        form = NewPitch()
        if form.validate_on_submit():
            title = form.title.data
            pitch = form.body.data
            category = form.category.data

            new_pitch = Pitch(pitch_title = title,pitch_body = pitch,category = category,user = current_user.username )

            new_pitch.save_pitch()
            return redirect(url_for('.profile',uname = current_user.username))
        title="create new pitch"
        return render_template('new_pitch.html',title = title,pitch_form = form,user = user)


@main.route('/pitch/<id>')
@login_required
def pitch(id):
    pitch = Pitch.query.filter_by(id = id).first()

    comment = Comment.get_pitch_comment(pitch.id)
    return render_template('pitch.html',pitch = pitch, comment = comment)


@main.route('/user/<uname>/update/pic', methods = ['Post'])
@login_required
def update_pic(uname):
    
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        
        filename = photos.save(request.files['photo'])
        path = f'photo/{filename}'
        user.profile_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname = uname))        


@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    pitch = Pitch.query.filter_by(id = id ).first()
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(pitch_id = pitch.id, comment = comment, user = current_user.username)

        new_comment.save_comment()
        return redirect(url_for('.pitch',id = pitch.id))