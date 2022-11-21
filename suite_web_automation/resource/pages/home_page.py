from dataclasses import dataclass


@dataclass
class home_shipper:
    dropdown_produk: str = "div.main-navigation .main-navigation-wrapper div.sublink:nth-child(1)"
    list_dropdown_produk:str = dropdown_produk + " " + "div.dropdown-wrapper a"
    option_produk_1 :str = dropdown_produk + " " + "div.dropdown-wrapper" + " " + "a[href='/shipping']"
    option_produk_2 :str = dropdown_produk + " " + "div.dropdown-wrapper" + " " + "a[href='/international_shipping']"
    option_produk_3 :str = dropdown_produk + " " + "div.dropdown-wrapper" + " " + "a[href='/warehouse']"
    option_produk_4 :str = dropdown_produk + " " + "div.dropdown-wrapper" + " " + "a[href='https://atoor.com/']"

    dropdown_solusi: str = "div.main-navigation .main-navigation-wrapper div:nth-child(2) button"
    dropdown_industri: str = "div.main-navigation .main-navigation-wrapper div:nth-child(3) button"


@dataclass
class home_blibli:
    button_login: str = ".header .menus__item button.btn__login"
    button_daftar: str = ".user.menus__item button.btn__register"
    frame_notification: str = "div.sp-fancybox-wrap iframe.sp-fancybox-iframe"
    button_close_modal: str = "#insider-notification-content div.element-content .element-close-button"

    # for login page
    field_login_username: str = ".login__form input.form__input.login__username"
    field_login_password: str = ".login__form input.form__input.login__password"
    button_confirm_login: str = ".login__form .login__button button[type=button]"

