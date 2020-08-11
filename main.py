from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class TestYandex:
	"""
	Тест яндекс
	"""
	url = 'https://yandex.ru/'
	
	def __init__(self):
		# Инициализируем драйвер и передаем url в качестве параметра
		self.driver = webdriver.Chrome()
		self.driver.get(self.url)
	
	def search_input_in_yandex(self):
		# Проверяем, присутствует ли искомый элемент на странице
		try:
			search_input = self.driver.find_element_by_xpath(
				"//input[@class='input__control input__input"
				" mini-suggest__input' and @aria-label='Запрос']")
			print('Строка поиска присутствует на странице!')
			search_input.send_keys('Тензор')
			# Проверяем, появилось ли окно предложений на странице
			try:
				# Ожидаем появления окна предложений поиска (PopUp появляется с задержкой ~2 секунды)
				Wait(self.driver, 2).until(
					ec.presence_of_element_located(
						(By.XPATH, "//div[@class='mini-suggest__popup mini-suggest__popup_svg_yes"
						           " mini-suggest__popup_theme_flat mini-suggest__popup_visible']")))
				print('Окно предложений присутствует на странице!')
				# Отправляем запрос
				self.driver.find_element_by_xpath("//button[@type='submit']").click()
			# Если, окно с предложениями поиска не найдено
			except Exception as e:
				print(f'''Окно с предложениями не найдено.
Ошибка: {e.__doc__}''')
		# Если поисковая строка не найдена
		except Exception as e:
			print(f'''Строка поиска не найдена.\n
Ошибка: {e.__doc__}''')
	
	def search_image_in_yandex(self):
		# Проверяем, присутствует ли ссылка на сервис "Картинки" на главной странице
		try:
			# Находим ссылку сервиса "Картинки" и кликаем по ней
			self.driver.find_element_by_xpath("//a[contains(@href, 'yandex.ru/images/')]").click()
			print('Сервис \"Картинки\" присутствует на странице!')
			# Получаем и проверяем ссылку на страницу сервиса "Картинки"
			try:
				self.driver.switch_to.window(self.driver.window_handles[1])
				# Если текущая страница соответствует ссылке на сервис "Картинки"
				if self.driver.current_url == 'https://yandex.ru/images/':
					# Открываем первое изображение
					self.driver.find_element_by_xpath(
						"//div[@class='cl-masonry__column cl-masonry__column_3'][1]/div[1]/div/a").click()
					print('Первая картинка открыта')
					# Сохраняем ссылку текущей картинки в переменную
					current_image = str(self.driver.current_url)
					# Находим и кликаем по кнопке навигации по картинкам (следующая)
					self.driver.find_element_by_xpath(
						"//div[@class='cl-viewer-navigate__item cl-viewer-navigate__item_right']").click()
					print('Кнопка следующее изображение нажата')
					# Находим кликаем по кнопке навигации по картинкам (предыдущая)
					self.driver.find_element_by_xpath(
						"//div[@class='cl-viewer-navigate__item cl-viewer-navigate__item_left']").click()
					# Сохраняем ссылку предыдущей картинки в переменную
					previous_image = str(self.driver.current_url)
					# Сравниваем сслыки на картинки
					assert current_image == previous_image
					print(f'Первое изображение {current_image}\n'
					      f'Возвращенное изображение {previous_image}')
			# Если не удалось перейти в сервис "Картинки"
			except Exception as e:
				print(f'''Перейти в сервис \"Картинки\" не удалось.\n
Ошибка: {e.__doc__}''')
		# Если сервис "Картинки" отсутствует на главной странице
		except Exception as e:
			print(f'''Сервис \"Картинки\" не найден.\n
Ошибка: {e.__doc__}''')


# Запускаем первую задачу в экземпляре класса
test = TestYandex()
test.search_input_in_yandex()

# Запускаем вторую задачу в экземпляре класса
test_2 = TestYandex()
test_2.search_image_in_yandex()
