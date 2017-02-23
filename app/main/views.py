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
	return render_template('index.html',posts = posts,pagination = pagination)

@main.route('/<int:page>')
def blogs(page):
	pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
	posts = pagination.items
	return render_template('index.html',posts = posts,pagination = pagination,show_article_list = True)
