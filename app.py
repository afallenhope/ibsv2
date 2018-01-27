# -*- coding: utf-8 -*-
from os import environ

from flask import Flask, render_template, request, redirect, url_for
from flask_dance.contrib.twitch import make_twitch_blueprint, twitch
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha512_crypt

from fallen.db import SettingsManager, UserManager
from fallen.models.base_model import db
from fallen.ui.forms import RegisterForm, LoginForm

environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('private.config.DebugConfig')
    db.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    settings_manager = SettingsManager.SettingsManager()
    client_id = settings_manager.get_setting('twitch_client_id').value
    client_secret = settings_manager.get_setting('twitch_client_secret').value

    twitch_blueprint = make_twitch_blueprint(client_id=client_id,
                                             client_secret=client_secret,
                                             scope='chat_login user_subscriptions')

    app.register_blueprint(blueprint=twitch_blueprint,
                           url_prefix='/twitch_login')

    user_manager = UserManager.UserManager()


    @app.route('/')
    def index():
        return render_template('pages/home.html', title='InfoSec Bot Services')


    @app.route('/register', methods=['GET', 'POST'])
    def register():
        register_form = RegisterForm.RegisterForm(request.form)
        if request.method == 'POST' and register_form.validate():
            name = register_form.name.data
            username = register_form.username.data
            email = register_form.email.data
            password = sha512_crypt.encrypt(str(register_form.password.data), salt='f4773nb01m30w', rounds=20180123)

            user = user_manager.create(name=name, username=username, email=email, password=password)
            return user
        return render_template('pages/register.html', form=register_form)


    @app.route('/twitch')
    def twitch_login():
        if not twitch.authorized:
            return redirect(url_for('twitch.login'))

        return "Twitch: %s" % twitch


    # @oauth_authorized.connect_via(twitch_blueprint)
    # def twitch_logged_in(blueprint, token):
    #     return "meow"

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        login_form = LoginForm.LoginForm(request.form)
        if request.method == 'POST' and login_form.validate():
            username = login_form.username.data
            password = sha512_crypt.encrypt(str(login_form.password.data), salt='f4773nb01m30w', rounds=20180123)

            return render_template('pages/success.html')
        return render_template('pages/login.html', form=login_form)


    app.run(debug=True)
