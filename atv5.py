import cv2

# Carregar imagem
img = cv2.imread("justin bieber.png")

# Verificar se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem.")
else:
    # Criar o negativo da imagem
    negativo = 255 - img

    # Exibir as imagens
    cv2.imshow("Original", img)
    cv2.imshow("Negativo", negativo)

    # Esperar até pressionar uma tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()
