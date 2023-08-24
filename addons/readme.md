# Directorio de Módulos
Esta carpeta addons permite organizar un grupo de módulos, para que odoo reconozca estos módulos debes asegurarte de que la carpeta se encuentre enlazada con el contenedor, además de que odoo.cof tenga la ruta del directorio de addons.
Puedes tener más de un directorio de módulos. Por ejemplo, en BigOdoo, tenemos módulos genéricos para website, contabilidad y Ventas.
~~~
./addons-website
./addons-account
./addons-sale
~~~
De esta forma organizamos los módulos que vamos desarrollando.
Por otro lado, cuando se trata de personalizaciones particulares para nuevos clientes, entonces, creamos un nuevo repositorio, en la cuál subimos los módulos del cliente. y para que nuestro repositorio principal los localice los referenciamos a traveś de docker-compose.yaml.

~~~
-> directorio_empresa1
---> empresa1.bigodoo.com # Proyecto principal, se ejecuta docker desde aquí
-------- addons-contabilidad # Personalizaciones generales para contabilidad
-------- addons-website # Personalizaciones generales para website
-------- config
-------- docker-compose.yaml
-------- .env
---> addons_empresa1 # Personalizaciones particulares para la empresa
-------- custom_crm_empresa1    # Personalización de crm
-------- custom_mail_empresa1   # Personalización de mail
-------- custom_sale_empresa1   # Personalización de sale
~~~

