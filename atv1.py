import cv2

# Carregar imagem
img = cv2.imread("justin bieber.png")

# Verificar se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem")
else:
    # Exibir imagem em uma janela
    cv2.imshow("Minha Imagem", img)

    # Espera até pressionar uma tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()