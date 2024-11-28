import cv2
import easyocr


def get_text(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Ошибка загрузки изображения.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('static/processed_image.jpg', gray)

    reader = easyocr.Reader(['ru'])

    result = reader.readtext(gray)

    if not result:
        print("Текст не распознан.")
        return

    extracted_text = ""
    for (bbox, text, prob) in result:
        extracted_text += text + "\n"

    return extracted_text


if __name__ == '__main__':
    image_path = 'static/snils2.jpg'
    text = get_text(image_path)
    print("Распознанный текст:")
    print(text)
