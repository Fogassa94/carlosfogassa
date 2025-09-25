import cv2

# Carregar a imagem
img = cv2.imread("justin bieber.png")

# Verificar se a imagem foi carregada com sucesso
if img is None:
    print("Erro ao carregar a imagem.")
else:
    # Converter para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Exibir as imagens
    cv2.imshow("Colorida", img)
    cv2.imshow("Cinza", gray)

    # Esperar até que uma tecla seja pressionada
    cv2.waitKey(0)
    cv2.destroyAllWindows()
