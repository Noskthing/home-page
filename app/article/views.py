#!/usr/bin/env python  
# -*- coding: utf-8 -*-  

from flask import render_template, redirect, url_for,session, flash, redirect, request, current_app, make_response


from . import article
from .forms import PostForm
from ..models import  Post
from .. import  db

@article.route('/post',methods = ['GET','POST'])
def post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(body = form.body.data,
					tag = form.tag.data,
                    introduction = form.introduction.data,
                    title = form.title.data)
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('main.index'))
	return render_template('article/article_post.html', form=form)