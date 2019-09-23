from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_quotes
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Upvote
from .forms import UpdateProfile,NewBlog,MyComment
from .. import db

@main.route('/')
def index():
    blog = Blog.query.all()
    title = "Bloggy-site"
    # Getting the quotes
    quotes = get_quotes()
    print(quotes)

    upvotes = Upvote.get_all_upvotes(blog_id=Blog.id)

    return render_template('index.html',title=title,blog=blog,quotes=quotes)

@main.route('/new/blog/',methods=['GET','POST'])
@login_required
def new_blog():
    form = NewBlog()
    if form.validate_on_submit():
        title = form.title.data
        blog_content = form.blog_content.data
        owner_id = current_user
        print(current_user._get_current_object().id)
        new_blog = Blog(owner_id=current_user._get_current_object().id,title=title,blog_content=blog_content)
        db.session.add(new_blog)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('blogs.html',form=form)

@main.route('/new/comment/<int:blog_id>',methods=['GET','POST'])
@login_required
def new_comment(blog_id):
    form=MyComment()
    if form.validate_on_submit():
        description = form.description.data
        new_comment=Comment(description=description,user_id=current_user._get_current_object().id, blog_id=blog_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.new_comment',form = form,blog_id=blog_id))
    # all_comments = Comment.query.filter_by(blog_id=blog_id).all()
    return render_template('comments.html',form=form)

@main.route('/blog/<int:blog_id>', methods=["POST"])
@login_required
def del_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.author != current_user:
        error = "You can't delete this Pitch"
        return redirect(url_for('main.index'))
    blog.delete()
    return redirect(url_for('main.index'))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)
    return render_template('profile/profile.html',user=user)

@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redireRegistrationFormct(url_for('.profile',uname=user.username))
    
    return render_template('profile/update.html',form=form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))