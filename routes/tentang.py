from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response, flash
#from app import DAO
from Misc.functions import *

#from Controllers.TentangManager import TentangManager
# test

tentang_view = Blueprint('tentang_routes', __name__, template_folder='/templates')

#tentang_manager = TentangManager(DAO)

@tentang_view.route('/tentang', methods=['GET'])
def home():
    return render_template('tentang.html')