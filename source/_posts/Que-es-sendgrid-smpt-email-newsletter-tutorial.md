---
title: ¿Qué es SendGrid? SMPT email newsletter tutorial
date: 2021-05-19 20:49:21
tags: [NewsLetter, SendGrid, SMPT]
categories: [Tutoriales]
toc: true
desc: Tal vez escuchaste el término SMTP antes, y te habrás preguntado que es. SMTP es un método comúnmente usado para manejar emails (correo electrónico).
---

Este tutorial es una traducción de un artículo original de [Nicholas Carrigan](https://www.freecodecamp.org/news/author/nhcarrigan/) y puedes encontrar el artículo en [FreeCodeCamp.org](https://www.freecodecamp.org/news/what-is-sendgrid-smpt-email-newsletter-tutorial/).

>💡***Anotación:*** A lo largo de este tutorial voy a usar palabras en ingles como email, emails, newsletter etc. Dejaré la traducción la primera vez que aparezcan con la intención de ir acostumbrándonos a estos nuevos términos que encontremos, te agradezco si tienes una forma mejor de hacerlo me lo dejes en los comentarios.

![img - https://www.freecodecamp.org/news/content/images/size/w2000/2021/05/pexels-rakicevic-nenad-1262304.jpg](https://www.freecodecamp.org/news/content/images/size/w2000/2021/05/pexels-rakicevic-nenad-1262304.jpg)


Tal vez escuchaste el término SMTP antes, y te habrás preguntado que es. SMTP es un método comúnmente usado para manejar emails (correo electrónico).

Hoy voy a explicarte que es SMTP, y como usar un proveedor de SMTP como SendGrid para enviar correos desde tu dirección de email.

## ¿Qué es SMTP?

SMTP (Simple Mail Transfer Protocol o Protocolo para Transferencia Simple de Correo), es el método a través del cual los servidores mandan emails (correos electrónicos). Cuando envías un correo electrónico a través de tu cuenta de Gmail, por ejemplo, tu cliente de email usa SMTP para enviar ese mensaje al servidor. El servidor también usa SMTP para enviarlo al servidor receptor.

Sin ahondar mucho en detalles técnicos, la forma más sencilla de pensar en SMTP es como un servidor de emails.

## ¿Qué es SendGrid?

SendGrid es un proveedor de servicios SMTP - de hecho, este es el servicio que usa freeCodeCamp para enviar el newsletter ([boletín informativo](https://es.wikipedia.org/wiki/Bolet%C3%ADn_informativo)) de Quincy's weekly.

Como muchos proveedores de SMTP, SendGrid ofrece el uso de servidores para enviar tus emails. Es una excelente opción para enviar gran cantidad de emails, y es una herramienta que debes tener en cuenta si mandas muchos emails que suponen una gran carga de  trabajo.

## Como crear una cuenta en SendGrid

El primer paso para usar los servicios de SendGrid es crear una cuenta. Dirígete a la página web de [SendGrid](https://sendgrid.com/) para registrarte. Ellos ofrecen múltiples precios, pero con el servicio gratuito será suficiente para este tutorial.

Sin embargo a medida que crezca tu lista de emails tal vez necesites características adicionales de suscripciones de pago.

Una vez estés registrado, deberías ver una página inicial parecida a esta.

![img - https://www.freecodecamp.org/news/content/images/size/w1000/2021/05/image-4.png](https://www.freecodecamp.org/news/content/images/size/w1000/2021/05/image-4.png)

## Como configurar tu dominio o email con SendGrid

Desde esta página, seleccionamos "Settings", y luego "Sender Authentication" del menú que se despliega. Las configuraciones de Sender Autenticaction (Autenticación de remitente) es donde le indicamos a SendGrid desde que cuentas de email permitiremos que se envíen emails.

Hay dos enfoques aquí - si tienes un dominio personal para los emails, puedes configurar este apartado en "Domain Authentication". Si usas una dirección de email personal, como una de Gmail, entonces tendrás que realizar las configuraciones en "Single Sender Authentication"

Elige la mejor opción para ti, sigue los pasos que teda SendGrid para configurar tu elección. Al terminar tendrás una vista similar a esta:

![img - https://www.freecodecamp.org/news/content/images/size/w1000/2021/05/image-5.png](https://www.freecodecamp.org/news/content/images/size/w1000/2021/05/image-5.png)

## Como puedes enviar emails vía SendGrid API

Actualmente para enviar emails es por medio de la API de SendGrid. Pero antes de usar la API, necesitas una API key (llave)

Desde tu página inicial, selecciona "Settings", y ahora "API Keys". Elije "Create API Key" y selecciona los permisos que quieras darle a esa key (yo le di todos los permisos solo para evitar problemas o errores).

Una vez tengas la key, guárdala en algún lugar seguro, ya que no podrás acceder otra vez a ella.

![img - https://www.freecodecamp.org/news/content/images/size/w1000/2021/05/image-6.png](https://www.freecodecamp.org/news/content/images/size/w1000/2021/05/image-6.png)

Ahora que tienes la API key, necesitas configurar el código para usar el `/mail/send` endpoint ([punto final][https://en.wikipedia.org/wiki/Web_API#Endpoints]). Puedes escribir el código de manera manual o usar uno de las librerías auxiliares, como el paquete de Node.js de SendGrid.

Cuando usas el paquete de Node.js, tienes un conjunto de valores para establecer en tus emails como los siguientes:

- `to`: La dirección que enviaras el email.
- `from`: La dirección de email desde la cual se enviara el email, esta debe cuadrar en tus configuraciones en "Sender Authentication"
- `subject`: El asunto de tu email.
- `text`: El contenido de tu email, si estás mandando un email de texto plano.
- `html`: El contenido de tu email, si estás mandando un email con formato HTML.

Las propiedades pueden cambiar si usas solo la API sin ayuda de una librería u otra librería, de cualquier manera dirígete a la documentación oficial para saber más.

## Como usar plantillas dinámicas en SendGrid

Como una opción alterativa, en lugar de enviar el contenido del email usando la API, puede usar una plantilla dinámica para generar el contenido.

Una plantilla dinámica te permite configurar el contenido para enviar emails, y ofrece la capacidad de cambiar campos específicos añadiendo una mayor funcionalidad.

Para crear una plantilla dinámica, desde la página inicial selecciona "Email API" y luego "Dynamic Templates". Luego has clic en "Create a Dinamic Template" - deberías ver tu plantilla aparecer.

Clic en ella, luego selecciona "Add Version" para abrir la selección de plantillas. Elige la plantilla en blanco, luego selecciona el tipo de editor que te gustaría usar (yo usare code editor).

![img - https://www.freecodecamp.org/news/content/images/size/w1000/2021/05/image-7.png](https://www.freecodecamp.org/news/content/images/size/w1000/2021/05/image-7.png)

Puedes escribir el contenido de tu email, o usar los placeholders (marcadores de posición) como estos `{{nombre}}` para los datos dinámicos. Estos placeholders recibirán valores mediante tu API cuando envíes un email.

Si quieres ver como tu plantilla va tomando forma debes ir a la pestaña de "Test Data" y añadir información de ejemplo para los placeholders.

## Como obtener Blocks/Bounces/Spams vía SendGrid API

Es importante rastrear los emails que no se pudieron entregar. SendGrid ofrece un conjunto de herramientas para ayudar a rastrear estos emails por ti, y puedes obtener esta información de tres maneras diferentes (o usando los endpoints API, si quieres analizar la información mediante programación).

- `Blocked` emails (correos electrónicos bloqueados) son emails que fueron rechazados por las políticas del proveedor de emails del receptor, como emails de universidades que no permiten trafico externo, o emails que no se resolvieron (no se encontró el servido de mail).

- `Bounced` emails (correos electrónicos rebotados) son emails que fueron recibidos por el servidor pero fueron devueltos. Esto puede pasar en casos donde el servidor de mail existe pero el usuario especificado no, o la bandeja de entrada esta llena.

- `Spam` emails (correo no deseado) son posiblemente los más importantes a monitorear, este se genera cuando el usuario revisa tu email y reporta ante su proveedor de email que tu email es spam. Estos impactan directamente tu reputación como remitente, es imperativo que no envíes emails a personas que marcaron tu email como spam.

## Otras preocupaciones 

Sobre tu reputación como remitente, SendGrid ofrece un nivel alto de métricas llamado "Sender Reputation". Estas métricas son una agregación de tu actividad en esta plataforma, y ayuda a tener una idea general de la forma en que los proveedores de email manejaran tus emails.

Una reputación baja resultará en que tus emails serán marcados como spam de manera automática, o incluso tu dirección de IP será bloqueada.

Si usas SendGrid de manera gratuita, usaras direcciones de IP compartidas. Esto significa que otros usuarios enviaran email mediante la misma IP, y estas acciones pueden impactar tu reputación de manera negativa.

Si tu intención es enviar grandes volúmenes de emails, te recomiendo que compres una dirección de IP dedicada para que te asegures de proteger tu reputación.

## Conclusión

Espero que este artículo te sea de ayuda y te sientas más cómodo usando SendGrid y el servicio que brinda. Deberías estar listo para empezar a mandar tus propios emails.

Si estás planeando iniciar un newsletter, el autor original escribió un artículo sobre como [crear un efectivo email newsletter](https://www.freecodecamp.org/news/how-to-create-an-email-newsletter-design-layout-send/) que te puede ayudar.

Esta fue una traducción realizada por [Jaime linares](https://www.linkedin.com/in/jaime-linares/). Espero que esta traducción te resulte de utilidad, tienes algo en lo que podría mejorar déjamelo saber en los comentarios tu opinión muy relevante para poder mejorar, gracias por leer este artículo.