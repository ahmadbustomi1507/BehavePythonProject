from dataclasses import dataclass

@dataclass
class home:
    button_masuk: str = ".user.menus__item button.btn__login"
    button_daftar: str = ".user.menus__item button.btn__register"

    # for login page
    field_masuk_username: str = ".login__form input.form__input.login__username"
    field_masuk_password: str = ".login__form input.form__input.login__password"
    button_masuk: str         = ".login__form .login__button button"