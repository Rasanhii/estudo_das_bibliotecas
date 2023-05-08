import os


path = '/estudo_das_bibliotecas/designe.jpg'

if os.access('/estudo_das_bibliotecas/designe.jpg', os.R_OK):
    imagem = cv2.imread('/estudo_das_bibliotecas/designe.jpg')
    cv2.imshow('Imagem Original', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Não foi possível acessar o arquivo')