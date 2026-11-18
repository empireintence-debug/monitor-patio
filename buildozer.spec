
[app]

# Nome do aplicativo
title = Monitor de Pátio

# Identificação do pacote Android
package.name = monitorpatio
package.domain = org.monitor

# Pasta onde estão os arquivos do aplicativo
source.dir = .

# Arquivos que serão incluídos no APK
source.include_exts = py,png,jpg,jpeg,kv,atlas

# Versão do aplicativo
version = 1.0.0

# Bibliotecas necessárias
requirements = python3,kivy

# Orientação da tela
orientation = portrait

# Configurações Android
android.api = 33
android.minapi = 21
android.ndk = 25b

# Aceitar licenças do Android SDK
android.accept_sdk_license = True
