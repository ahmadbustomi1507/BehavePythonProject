from dataclasses import dataclass

@dataclass
class home:
    button_login: str = ".header .menus__item button.btn__login"
    button_daftar: str = ".user.menus__item button.btn__register"
    frame_notification: str = "div.sp-fancybox-wrap iframe.sp-fancybox-iframe"
    button_close_modal: str = "#insider-notification-content div.element-content .element-close-button"

    # for login page
    field_login_username: str = ".login__form input.form__input.login__username"
    field_login_password: str = ".login__form input.form__input.login__password"
    button_confirm_login: str         = ".login__form .login__button button[type=button]"

