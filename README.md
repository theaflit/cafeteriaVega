# Отчет об оптимизации 

## 1. Датасет
- Для обучения нейросети был использован датасет, содержащий изображения людей в столовой "Вега" вместе с разметкой в формате YOLO. Для просмотра нужно распаковать архив `DataSet.yoloV8.zip`

## 2. Код нейросети
- В папке "neyroVega" содержится код, реализующий нейронную сеть для распознавания людей на изображениях. Для этого использовалась архитектура YOLOv8. Код представлен в папке `neyroVega/main`.

## 3. Код Telegram бота
- В папке "TLbotVega" находится код Telegram бота, который использует нейросеть для распознавания людей через камеры, отправленных пользователями. Бот также предоставляет функциональность для запроса информации о количестве людей на видео, интенсивности потока Код бота представлен в файле `TLbotVega/main.py`.

## 4. Классификация
- Мы предлагаем классифицировать людей на студентов и преподавателей, для составления отчетов и статистики а также присвоить людям которые проходят и опережают не стояв в очереди отдельную категорию "overtakers", что сильно поможет оптимизации очереди. 

