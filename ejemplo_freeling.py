from Preprocesamiento.lematizador import lematizar

#cadena = '¡Pésimo! No gastes tu dinero ahí malas condiciones, deplorable. Definitivamente no gastes tu dinero ahí, mejor ve a gastarlo en dulces en la tienda de La catrina.'
cadena = 'La mejor vista de Guanajuato Es un mirador precioso y con la mejor vista de la ciudad de Guanajuato. El monumento es impresionante. Frente al monumento (por la parte de atrás del Pípila) hay una serie de locales en donde venden artesanías... si te gusta algo de ahí, cómpralo. A mí me pasó que vi algo y no lo compré pensando que lo vería más tarde en otro lado y no fue así. Te recomiendo que llegues hasta ahí en taxi, son MUY económicos, porque como está en un lugar muy alto, es muy cansado llegar caminando, aunque no está lejos del centro. PEROOOO... bájate caminando por los mini callejones. ¡Es algo precioso!Te lleva directamente por un lado del Teatro Juárez.'
cadena_lematizada = lematizar(cadena)

print (cadena_lematizada.lower())

