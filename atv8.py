import cv2

# Carregar imagem
img = cv2.imread("justin bieber.png")

# Verificar se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem.")
else:
    # Aplicar desfoque Gaussiano
    gauss = cv2.GaussianBlur(img, (7, 7), 0)

    # Aplicar desfoque da mediana
    median = cv2.medianBlur(img, 7)

    # Exibir as imagens
    cv2.imshow("Original", img)
    cv2.imshow("Gaussian", gauss)
    cv2.imshow("Median", median)

    # Esperar até pressionar uma tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()
