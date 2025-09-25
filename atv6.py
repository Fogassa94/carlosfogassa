import cv2

# Carregar a imagem
img = cv2.imread("justin bieber.png")

# Verificar se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem.")
else:
    # Selecionar a região de interesse (y1:y2, x1:x2)
    roi = img[50:200, 100:300]

    # Exibir a imagem original e o recorte
    cv2.imshow("Original", img)
    cv2.imshow("Recorte", roi)

    # Esperar até pressionar uma tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()
