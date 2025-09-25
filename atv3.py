import cv2

# Carrega a imagem
img = cv2.imread("justin bieber.png")

# Verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem.")
else:
    # Reduz para metade do tamanho
    small = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    # Aumenta para o dobro do tamanho
    large = cv2.resize(img, (0, 0), fx=2, fy=2)

    # Exibe as imagens
    cv2.imshow("Original", img)
    cv2.imshow("Reduzida", small)
    cv2.imshow("Ampliada", large)

    # Espera por uma tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()
