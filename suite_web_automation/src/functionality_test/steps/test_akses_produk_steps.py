from selenium.webdriver.common.by import By
from resource.pages.home_page import home_shipper

@given(u'user is in homepage')
def step_impl(context):
    print("user is in homepage")
    context.driver.get(context.config.userdata['base_url'])

@when(u'user click dropdown produk')
def step_impl(context):
    produk          = context.driver.find_element(By.CSS_SELECTOR,home_shipper.dropdown_produk)
    context.action.click(produk).pause(10).perform()
    context.driver.implicitly_wait(15)
    context.action.reset_actions()

@then(u'user will see 4 main products')
def step_impl(context):
    list_produk = context.driver.find_elements(By.CSS_SELECTOR,home_shipper.list_dropdown_produk)
    assert "Agregator Logistik Domestik" in list_produk[0].text , f"cannot find 1st product {list_produk[0].text}"
    assert "Agregator Logistik Internasional" in list_produk[1].text , f"cannot find 2nd product {list_produk[1].text} "
    assert "Manajemen Pergudangan" in list_produk[2].text , f"cannot find 3ed product{list_produk[2].text} "
    assert "Atoor by Shipper" in list_produk[3].text , f"cannot find 4th product {list_produk[3].text}"

@when(u'user click "{produk}"')
def step_impl(context,produk):
    dropdown_produk          = context.driver.find_element(By.CSS_SELECTOR,home_shipper.dropdown_produk)
    print(f"click {produk}")
    match produk:
        case "Aggregator Logistik Domestik":
            choose_produk = context.driver.find_element(By.CSS_SELECTOR,home_shipper.option_produk_1)
            context.action.click(dropdown_produk).click(choose_produk).pause(10).perform()
            context.driver.implicitly_wait(15)
        case "Aggregator Logistik Internasional":
            choose_produk = context.driver.find_element(By.CSS_SELECTOR, home_shipper.option_produk_2)
            context.action.click(dropdown_produk).click(choose_produk).pause(10).perform()
            context.driver.implicitly_wait(15)
            case
        case "Manajemen Pergudangan":
            choose_produk = context.driver.find_element(By.CSS_SELECTOR, home_shipper.option_produk_3)
            context.action.click(dropdown_produk).click(choose_produk).pause(10).perform()
            context.driver.implicitly_wait(15)
        case "_":
            pass
    context.action.reset_actions()


@then(u'user will be redirected to shipping page')
def step_impl(context):
    assert context.driver.title=="Cek Ongkir Semua Ekspedisi JNE, SiCepat, J&T, TIKI - Shipper", f"wrong title {context.driver.title}"
    assert context.driver.current_url==f"{context.config.userdata['base_url']}/international-shipping", f"wrong current_url {context.driver.current_url}"
    context.driver.implicitly_wait(10)

@when(u'user back to previous page')
def step_impl(context):
    context.driver.back()
    assert context.driver.current_url==f"{context.config.userdata['base_url']}/", f"wrong current_url {context.driver.current_url}"


@then(u'user will be redirected to international shipping page')
def step_impl(context):
    assert context.driver.title == "Cek Ongkir Semua Ekspedisi JNE, SiCepat, J&T, TIKI - Shipper", f"wrong title {context.driver.title}"
    assert context.driver.current_url == f"{context.config.userdata['base_url']}/shipping", f"wrong current_url {context.driver.current_url}"
    context.driver.implicitly_wait(10)


@then(u'user will be redirected to warehouse page')
def step_impl(context):
    assert context.driver.title == "Jasa Sewa Gudang Terpercaya Di Indonesia - Shipper", f"wrong title {context.driver.title}"
    assert context.driver.current_url == f"{context.config.userdata['base_url']}/warehouse", f"wrong current_url {context.driver.current_url}"
    context.driver.implicitly_wait(10)

@then(u'user will be redirected to atoor page')
def step_impl(context):
    pass