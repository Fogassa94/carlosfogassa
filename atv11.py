import cv2

# Abrir a webcam
cap = cv2.VideoCapture(0)

while True:
    # Capturar o frame da webcam
    ret, frame = cap.read()

    # Verificar se o frame foi capturado corretamente
    if not ret:
        break

    # Aplicar detecção de bordas com o Canny
    bordas = cv2.Canny(frame, 100, 200)

    # Exibir as bordas detectadas
    cv2.imshow("Bordas", bordas)

    # Fechar a janela pressionando 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura e fechar todas as janelas
cap.release()
cv2.destroyAllWindows()
