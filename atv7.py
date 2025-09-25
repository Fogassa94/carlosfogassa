import cv2

# Carregar imagem
img = cv2.imread("justin bieber.png")

# Verificar se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem.")
else:
    # Rotação de 90 graus no sentido horário
    rot90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Rotação de 45 graus em torno do centro
    (h, w) = img.shape[:2]
    centro = (w // 2, h // 2)
    matriz = cv2.getRotationMatrix2D(centro, 45, 1.0)

    # Realiza a rotação
    rot45 = cv2.warpAffine(img, matriz, (w, h))

    # Exibir imagens
    cv2.imshow("Original", img)
    cv2.imshow("90 graus", rot90)
    cv2.imshow("45 graus", rot45)

    # Esperar até pressionar uma tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()
