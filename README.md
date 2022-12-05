# TabFast
Sistema que permite fazer postagem no TabNews.com.br atraves do CMD (prompt de comando).

![2022-12-05-14-36-35](https://user-images.githubusercontent.com/8114976/205706114-2d79c633-fd95-4afa-8a87-f46435bc3a3c.gif)

![2022-12-05-14-37-46](https://user-images.githubusercontent.com/8114976/205706135-93b08aa2-24ae-4d61-9cb2-2c5eb8e78e08.gif)

⚠️ **Nota importante**: Esse projeto ainda não está finalizado e ainda está em construção.

# Preparar para usar

Antes de tudo e preciso ter o `python` instalado e o modulo `aiohttp`
```
pip install aiohttp
```
**Em seguida no arquivo `config.py` deve adicionar as seguintes informações:**
```
TABNEWS_HOST = 'https://tabnews-8kgcqlch1-tabnews.vercel.app' # para testar basta deixar essa URL que e do Deploy Atual
                                                              # caso queira postar no TabNews mude para 'https://tabnews.com.br'
TABNEWS_EMAIL = '' # aqui vai seu email
TABNEWS_PASSWORD = '' # aqui vai sua senha
```

**Agora a parte mais aguardada...**

# Como rodar
Depois de preparar tudo basta ir no diretorio raiz, abrir o CMD (prompt de comando) NA PASTA DO PROJETO e escrever `python main.py` e apertar o enter

agora ele vai pedir o **TITULO** e a **MENSAGEM**. 

**PRONTO... você acaba de fazer sua primeira postagem :)**


# A SE FAZER
⚠️ Precisa ser feito um sistema que receba o `status` e printe na tela se a Postagem foi feito ou não,
no momento ele sempre vai retornar que foi postado...

⚠️(caso você usar o ambiente de homologação aguarde **10 minutos** para confirmar se foi feito a postagem)⚠️

# Creditos
[**Gustavosta**](https://github.com/Gustavosta/) - Quem fez o [**Tabulator**](https://github.com/Gustavosta/Tabulator) de onde eu retirei 99% do codigo.

[**Matrix_s0beit**](https://github.com/cybernerd007) - Fiz algumas alterações para ser possivel fazer postagens atraves do CMD (prompt de comando).
