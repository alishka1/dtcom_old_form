# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome("chromedriver")
driver.set_page_load_timeout(30)
driver.get("https://www.diplomtime.com/service")
# driver.get("http://develop.diplomtime.com")
driver.implicitly_wait(10)
driver.maximize_window()

try:
	driver.find_element_by_class_name('order_rk').click()
	print(u'1. Открытие - Форма заказа -                 ОК')
except:
	print(u'1. Открытие - Форма заказа -                 ОШИБКА')

time.sleep(2)

# Начало этапа нажатия узнать цену при пустых полях
# Здесь error не должен появиться, так как кнопка узнать цену не нажата при пустых значениях. Следовательно 
# Не_ерор найден является корректным уведомлением. То есть - нет ошибок - уведомления обнаружено, так как ошибок нет.

try:
	driver.find_element_by_css_selector('.rk_type_f.js--validator:not(.error)')
	print(u'2. Выберите тип - Не_ерор найден!            ОК')
except:
	print(u'2. Выберите тип - Не_ерор не найден!         ОШИБКА')


try:
	driver.find_element_by_css_selector('.tema_rk.js--validator:not(.error)')
	print(u'3. Тема работы - Не_ерор найден!             ОК')
except:
	print(u'3. Тема работы - Не_ерор не найден!          ОШИБКА')

try:
	driver.find_element_by_css_selector('.phone_rk.js--validator:not(.error)')
	print(u'4. Телефон - Не_ерор найден!                 ОК')
except:
	print(u'4. Телефон - Не_ерор не найден!              ОШИБКА')

try:
	driver.find_element_by_css_selector('.email_rk.js--validator:not(.error)')
	print(u'5. Email - Не_ерор найден!                   ОК')
except:
	print(u'5. Email - Не_ерор не найден!                ОШИБКА')

try:
	driver.find_element_by_class_name('send_rk').click()
	print(u'6. Кнопка узнать цену -                      ОК')
except:
	print(u'6. Кнопка узнать цену -                      ОШИБКА')

# Здесь error должен появиться, так как кнопка узнать цену нажата при пустых значениях. Следовательно Не_ерор не найден
# является корректным уведомлением. То есть - нет ошибок - уведомления не обнаружено, так как ошибки есть.

try:
	driver.find_element_by_css_selector('.rk_type_f.js--validator:not(.error)')
	print(u'7. Выберите тип - Не_ерор найден!            ОШИБКА')
except:
	print(u'7. Выберите тип - Не_ерор не найден!         ОК')

try:
	driver.find_element_by_css_selector('.tema_rk.js--validator:not(.error)')
	print(u'8. Тема работы - Не_ерор найден!             ОШИБКА')
except:
	print(u'8. Тема работы - Не_ерор не найден!          ОК')

try:
	driver.find_element_by_css_selector('.phone_rk.js--validator:not(.error)')
	print(u'9. Телефон - Не_ерор найден!                 ОШИБКА')
except:
	print(u'9. Телефон - Не_ерор не найден!              ОК')

try:
	driver.find_element_by_css_selector('.email_rk.js--validator:not(.error)')
	print(u'10. Email - Не_ерор найден!                  ОШИБКА')
except:
	print(u'10. Email - Не_ерор не найден!               ОК')

try:
	driver.refresh()
	print(u'11. Обновление страницы -                    ОК')
except:
	print(u'11. Обновление страницы -                    ОШИБКА')

try:
	driver.find_element_by_class_name('order_rk').click()
	print(u'12. Открытие - Форма заказа -                ОК')
except:
	print(u'12. Открытие - Форма заказа -                ОШИБКА')

# Конец этапа нажатия узнать цену при пустых полях

# Начало этапа одиночного фокус аута при пустых полях

# Здесь error не должен появиться, так как фокус аут не активирован при пустых значениях. Следовательно 
# Не_ерор найден является корректным уведомлением. То есть - нет ошибок - уведомления обнаружено, так как ошибок нет.

try:
	driver.find_element_by_css_selector('.rk_type_f.js--validator:not(.error)')
	print(u'13. Выберите тип - Не_ерор найден!           ОК')
except:
	print(u'13. Выберите тип - Не_ерор не найден!        ОШИБКА')


try:
	driver.find_element_by_css_selector('.tema_rk.js--validator:not(.error)')
	print(u'14. Тема работы - Не_ерор найден!            ОК')
except:
	print(u'14. Тема работы - Не_ерор не найден!         ОШИБКА')

try:
	driver.find_element_by_css_selector('.phone_rk.js--validator:not(.error)')
	print(u'15. Телефон - Не_ерор найден!                ОК')
except:
	print(u'15. Телефон - Не_ерор не найден!             ОШИБКА')

try:
	driver.find_element_by_css_selector('.email_rk.js--validator:not(.error)')
	print(u'16. Email - Не_ерор найден!                  ОК')
except:
	print(u'16. Email - Не_ерор не найден!               ОШИБКА')

try:
	driver.find_element_by_css_selector('.rk_type_f').click()
	print(u'17. Выберите тип - активирован               ОК')
except:
	print(u'17. Выберите тип - не активирован            ОШИБКА')

try:
	driver.find_element_by_css_selector('.tema_rk').click()
	print(u'18. Тема работы - активирован                ОК')
except:
	print(u'18. Тема работы - не активирован             ОШИБКА')

try:
	driver.find_element_by_css_selector('.phone_rk').click()
	print(u'19. Телефон - активирован                    ОК')
except:
	print(u'19. Телефон - не активирован                 ОШИБКА')

try:
	driver.find_element_by_css_selector('.email_rk').click()
	print(u'20. Email - активирован                      ОК')
except:
	print(u'20. Email - не активирован                   ОШИБКА')

try:
	driver.find_element_by_css_selector('.date_rk').click()
	print(u'21. Календарь активирован                    ОК')
except:
	print(u'21. Календарь активирован                    ОШИБКА')

try:
	select = Select(driver.find_element_by_class_name('rk_type_f'))
	select.select_by_visible_text('Реферат')
	print(u'22. Тип работы выбран реферат                ОК')
except:
	print(u'22. Тип работы выбран реферат                ОШИБКА')

try:
	driver.find_element_by_css_selector('.tema_rk').click()
	print(u'23. Тема работы - активирован                ОК')
except:
	print(u'23. Тема работы - не активирован             ОШИБКА')

try:
	driver.find_element_by_css_selector('.rk_type_f.js--validator:not(.error)')
	print(u'24. Выберите тип - Не_ерор найден!           ОК')
except:
	print(u'24. Выберите тип - Не_ерор не найден!        ОШИБКА')

try:
	send = driver.find_element_by_class_name('tema_rk')
	send.send_keys(u"Тест")
	print(u'25. Тема работы текст напечатан -            ОК')
except:
	print(u'25. Тема работы текст напечатан              ОШИБКА')	

try:
	driver.find_element_by_css_selector('.tema_rk.js--validator:not(.error)')
	print(u'26. Тема работы - Не_ерор найден!            ОК')
except:
	print(u'26. Тема работы - Не_ерор не найден!         ОШИБКА')

try:	
	send = driver.find_element_by_class_name('phone_rk')
	send.send_keys("77777777777")
	print(u'27. Телефон номер напечатан -                ОК')
except:
	print(u'27. Телефон номер напечатан -                ОШИБКА')

try:
	driver.find_element_by_css_selector('.phone_rk.js--validator:not(.error)')
	print(u'28. Телефон - Не_ерор найден!                ОК')
except:
	print(u'28. Телефон - Не_ерор не найден!             ОШИБКА')

try:
	send = driver.find_element_by_class_name('email_rk')
	send.send_keys("test@diplomtime.ru")
	print(u'29. Email напечатан -                        ОК')
except:
	print(u'29. Email напечатан -                        ОШИБКА')

try:
	driver.find_element_by_css_selector('.email_rk.js--validator:not(.error)')
	print(u'30. Email - Не_ерор найден!                  ОК')
except:
	print(u'30. Email - Не_ерор не найден!               ОШИБКА')

try:
	send = driver.find_element_by_class_name('date_rk')
	send.send_keys(u"11.03.2017")
	print(u'31. Некорректная дата напечатана -           ОК')
except:
	print(u'31. Некорректная дата напечатана -           ОШИБКА')

try:
	driver.find_element_by_css_selector('.tema_rk').click()
	print(u'32. Тема работы - активирован                ОК')
except:
	print(u'32. Тема работы - не активирован             ОШИБКА')

try:
	driver.find_element_by_css_selector('.date_rk.js--validator:not(.error)')
	print(u'33. Дата - Не_ерор найден!                   ОШИБКА')
except:
	print(u'33. Дата - Не_ерор не найден!                ОК')

try:
	send = driver.find_element_by_css_selector('.date_rk')
	send.send_keys(Keys.CONTROL + "a");
	send.send_keys(Keys.BACK_SPACE)
	# send.send_keys(Keys.RETURN)
	# send.clear()
	print(u'34. Некорректная дата очищена -              ОК')
except:
	print(u'34. Некорректная дата очищена -              ОШИБКА')

try:
	send = driver.find_element_by_class_name('date_rk')
	send.send_keys(u"11.03.2088")
	print(u'35. Корректная дата напечатана -             ОК')
except:
	print(u'35. Корректная дата напечатана -             ОШИБКА')

try:
	driver.find_element_by_css_selector('.tema_rk').click()
	print(u'36. Тема работы - активирован                ОК')
except:
	print(u'36. Тема работы - не активирован             ОШИБКА')

try:
	driver.find_element_by_css_selector('.date_rk.js--validator:not(.error)')
	print(u'37. Дата - Не_ерор найден!                   ОК')
except:
	print(u'37. Дата - Не_ерор не найден!                ОШИБКА')

try:	
	send = driver.find_element_by_class_name('phone_rk')
	send.send_keys(Keys.BACK_SPACE)
	print(u'38. Телефон одна цифра удалена -             ОК')
except:
	print(u'38. Телефон одна цифра удалена -             ОШИБКА')

try:
	driver.find_element_by_css_selector('.phone_rk.js--validator:not(.error)')
	print(u'39. Телефон - Не_ерор найден!                ОШИБКА')
except:
	print(u'39. Телефон - Не_ерор не найден!             ОК')

try:	
	send = driver.find_element_by_class_name('phone_rk')
	send.send_keys("7")
	print(u'40. Телефон номер напечатан -                ОК')
except:
	print(u'40. Телефон номер напечатан -                ОШИБКА')

try:
	driver.find_element_by_css_selector('.phone_rk.js--validator:not(.error)')
	print(u'41. Телефон - Не_ерор найден!                ОК')
except:
	print(u'41. Телефон - Не_ерор не найден!             ОШИБКА')

try:	
	send = driver.find_element_by_class_name('email_rk')
	send.send_keys(Keys.BACK_SPACE)
	print(u'42. Email одна буква удалена -               ОК')
except:
	print(u'42. Email одна буква удалена -               ОШИБКА')

try:
	driver.find_element_by_css_selector('.email_rk.js--validator:not(.error)')
	print(u'43. Email - Не_ерор найден!                  ОШИБКА')
except:
	print(u'43. Email - Не_ерор не найден!               ОК')

try:	
	send = driver.find_element_by_class_name('email_rk')
	send.send_keys("u")
	print(u'44. Email одна буква добавлена -             ОК')
except:
	print(u'44. Email одна буква добавлена -             ОШИБКА')

try:
	driver.find_element_by_css_selector('.email_rk.js--validator:not(.error)')
	print(u'45. Email - Не_ерор найден!                  ОК')
except:
	print(u'45. Email - Не_ерор не найден!               ОШИБКА')

try:
	driver.refresh()
	print(u'46. Обновление страницы -                    ОК')
except:
	print(u'46. Обновление страницы -                    ОШИБКА')

try:
	driver.find_element_by_class_name('order_rk').click()
	print(u'47. Открытие - Форма заказа -                ОК')
except:
	print(u'47. Открытие - Форма заказа -                ОШИБКА')

try:
	driver.find_element_by_class_name('tema_rk').click()
	print(u'48. Тема работы - активирован                ОК')
except:
	print(u'48. Тема работы - не активирован             ОШИБКА')

try:	
	send = driver.find_element_by_class_name('tema_rk')
	send.send_keys(Keys.ESCAPE)
	print(u'49. ESCAPE -                                 ОК')
except:
	print(u'49. ESCAPE -                                 ОШИБКА')

try:
	driver.find_element_by_class_name('order_rk').click()
	print(u'50. Открытие - Форма заказа -                ОК')
except:
	print(u'50. Открытие - Форма заказа -                ОШИБКА')

try:	
	send = driver.find_element_by_class_name('phone_rk')
	send.send_keys(Keys.ENTER)
	print(u'51. ENTER -                                  ОК')
except:
	print(u'51. ENTER -                                  ОШИБКА')

try:
	driver.find_element_by_css_selector('.rk_type_f.js--validator:not(.error)')
	print(u'52. Выберите тип - Не_ерор найден!           ОШИБКА')
except:
	print(u'52. Выберите тип - Не_ерор не найден!        ОК')

try:
	driver.find_element_by_css_selector('.tema_rk.js--validator:not(.error)')
	print(u'53. Тема работы - Не_ерор найден!            ОШИБКА')
except:
	print(u'53. Тема работы - Не_ерор не найден!         ОК')

try:
	driver.find_element_by_css_selector('.phone_rk.js--validator:not(.error)')
	print(u'54. Телефон - Не_ерор найден!                ОШИБКА')
except:
	print(u'54. Телефон - Не_ерор не найден!             ОК')

try:
	driver.find_element_by_css_selector('.email_rk.js--validator:not(.error)')
	print(u'55. Email - Не_ерор найден!                  ОШИБКА')
except:
	print(u'55. Email - Не_ерор не найден!               ОК')

try:
	driver.refresh()
	print(u'56. Обновление страницы -                    ОК')
except:
	print(u'56. Обновление страницы -                    ОШИБКА')

try:
	driver.find_element_by_class_name('order_rk').click()
	print(u'57. Открытие - Форма заказа -                ОК')
except:
	print(u'57. Открытие - Форма заказа -                ОШИБКА')

# Этап: Сначала фокус аут, потом отлавливаем эрор, потом посылаем текст. Потом отлавливаем отсутствие ошибки
# Ошибка должна исчезнуть после фокус аута по мере ввода текста
try:
	driver.find_element_by_css_selector('.tema_rk').click()
	print(u'58. Тема работы - активирован                ОК')
except:
	print(u'58. Тема работы - не активирован             ОШИБКА')

try:
	driver.find_element_by_css_selector('.phone_rk').click()
	print(u'59. Телефон - активирован                    ОК')
except:
	print(u'59. Телефон - не активирован                 ОШИБКА')

try:
	driver.find_element_by_css_selector('.tema_rk.js--validator:not(.error)')
	print(u'60. Тема работы - Не_ерор найден!            ОШИБКА')
except:
	print(u'60. Тема работы - Не_ерор не найден!         ОК')


try:
	send = driver.find_element_by_class_name('tema_rk')
	send.send_keys(u"Тест")
	print(u'61. Тема работы текст напечатан -            ОК')
except:
	print(u'61. Тема работы текст напечатан              ОШИБКА')


try:
	driver.find_element_by_css_selector('.tema_rk.js--validator:not(.error)')
	print(u'62. Тема работы - Не_ерор найден!            ОК')
except:
	print(u'62. Тема работы - Не_ерор не найден!         ОШИБКА')

try:
	driver.find_element_by_css_selector('.email_rk').click()
	print(u'63. Email - активирован                      ОК')
except:
	print(u'63. Email - не активирован                   ОШИБКА')

try:
	driver.find_element_by_css_selector('.phone_rk.js--validator:not(.error)')
	print(u'64. Телефон - Не_ерор найден!                ОШИБКА')
except:
	print(u'64. Телефон - Не_ерор не найден!             ОК')

try:	
	send = driver.find_element_by_class_name('phone_rk')
	send.send_keys("77777777777")
	print(u'65. Телефон номер напечатан -                ОК')
except:
	print(u'65. Телефон номер напечатан -                ОШИБКА')

try:
	driver.find_element_by_css_selector('.phone_rk.js--validator:not(.error)')
	print(u'66. Телефон - Не_ерор найден!                ОК')
except:
	print(u'66. Телефон - Не_ерор не найден!             ОШИБКА')

try:
	driver.find_element_by_css_selector('.tema_rk').click()
	print(u'67. Тема работы - активирован                ОК')
except:
	print(u'67. Тема работы - не активирован             ОШИБКА')

try:
	driver.find_element_by_css_selector('.email_rk.js--validator:not(.error)')
	print(u'68. Email - Не_ерор найден!                  ОШИБКА')
except:
	print(u'68. Email - Не_ерор не найден!               ОК')

try:
	send = driver.find_element_by_class_name('email_rk')
	send.send_keys("test@diplomtime.ru")
	print(u'69. Email напечатан -                        ОК')
except:
	print(u'69. Email напечатан -                        ОШИБКА')

try:
	driver.find_element_by_css_selector('.email_rk.js--validator:not(.error)')
	print(u'70. Email - Не_ерор найден!                  ОК')
except:
	print(u'70. Email - Не_ерор не найден!               ОШИБКА')

try:
	select = Select(driver.find_element_by_class_name('rk_type_f'))
	select.select_by_visible_text('Реферат')
	print(u'71. Тип работы выбран реферат                ОК')
except:
	print(u'71. Тип работы выбран реферат                ОШИБКА')

try:
	driver.find_element_by_class_name('send_rk').click()
	print(u'72. Кнопка узнать цену -                     ОК')
except:
	print(u'72. Кнопка узнать цену -                     ОШИБКА')

time.sleep(32)
try:
	driver.find_element_by_css_selector('.tag.center.mrgn_lx.mrgn_rx.js__quest--yes').click()
	print(u'73. Кнопка ДА -                              ОК')
except:
	print(u'73. Кнопка ДА -                              ОШИБКА')

try:
	driver.find_element_by_css_selector('.tag.center.mrgn_lx.mrgn_rx.close_rk').click()
	print(u'74. Кнопка продолжить -                      ОК')
except:
	print(u'74. Кнопка продолжить -                      ОШИБКА')


# time.sleep(3)
# driver.quit()















# try:
# 	send = driver.find_element_by_id('body')
# 	# send.send_keys(Keys.CONTROL + 'a') 
# 	send.send_keys(Keys.F5) 
# 	print(u'Ф5!    ОК')
# except:
# 	print(u'Ф5!    ОШИБКА')

