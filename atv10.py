import cv2
import numpy as np

# Abrir a webcam
cap = cv2.VideoCapture(0)

while True:
    # Capturar o frame da webcam
    ret, frame = cap.read()

    # Verificar se o frame foi capturado corretamente
    if not ret:
        break

    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Converter a imagem em escala de cinza de volta para BGR (para poder exibir lado a lado)
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Combinar as imagens lado a lado
    lado_a_lado = np.hstack((frame, gray_bgr))

    # Exibir as imagens combinadas
    cv2.imshow("Colorido e Cinza", lado_a_lado)

    # Fechar a janela pressionando 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura e fechar todas as janelas
cap.release()
cv2.destroyAllWindows()
