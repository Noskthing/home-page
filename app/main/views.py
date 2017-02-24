#!/usr/bin/env python  
# -*- coding: utf-8 -*-  

from flask import render_template, redirect, url_for,session, flash, redirect, request, current_app, make_response
from ..models import Post
from . import main

@main.route('/')
def index():
	pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        1, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
	posts = pagination.items
	return render_template('main/index.html',posts = posts,pagination = pagination)

@main.route('/<int:page>')
def blogs(page):
	pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
	posts = pagination.items
	return render_template('main/index.html',posts = posts,pagination = pagination,show_article_list = True)

@main.route('/article/<int:id>')
def article(id):
	post = Post.query.get_or_404(id)
	pre_post = Post.query.get(id - 1)
	next_post = Post.query.get(id + 1)
	return render_template('main/article.html',post = post,pre_post = pre_post,next_post = next_post,show_article_list = True)
