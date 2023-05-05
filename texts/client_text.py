"""Message templates"""
from handlers.detect_anime import MIN_SIZE

WELCOME_TEXT = '''
Привет, выбери категорию
'''

WAITING_FOR_IMAGE = f'''
Отправь картинку размера как минимум {MIN_SIZE}x{MIN_SIZE}
'''

BAD_IMAGE_ERROR = '''
Изображение слишком маленькое, отправь другое изображение
'''

WAIT_FOR_RENDER = '''
Картинка обрабатывается...
'''

NOT_IMAGE_ERROR = '''
Это не картинка, отправь картинку
'''

GUESS_ANIME = '''
Вероятности:
'''