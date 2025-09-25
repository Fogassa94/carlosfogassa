import cv2
import numpy as np

# Criar imagem em branco (500x500 pixels, 3 canais de cor)
img = np.zeros((500, 500, 3), dtype="uint8")

# Função para desenhar na imagem
def desenhar(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Desenhar um círculo verde na posição onde o mouse é clicado
        cv2.circle(img, (x, y), 20, (0, 255, 0), -1)

# Criar a janela e configurar o callback do mouse
cv2.namedWindow("Desenho")
cv2.setMouseCallback("Desenho", desenhar)

# Loop para mostrar a imagem e capturar as interações
while True:
    # Exibir a imagem
    cv2.imshow("Desenho", img)

    # Esperar até pressionar 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Fechar todas as janelas abertas
cv2.destroyAllWindows()
