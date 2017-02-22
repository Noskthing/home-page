#!/usr/bin/env python  
# -*- coding: utf-8 -*-  

from flask import render_template, redirect, url_for,session, flash, redirect, request, current_app, make_response
from . import main

@main.route('/')
def index():
	return render_template('index.html')