from utils.tabnews_utils import post_tabnews_article
import asyncio


async def main():
    print("Digite o Titulo:")
    titulo = input()
    print("Digite o Texto:")
    msg = input()
    await post_tabnews_article(titulo, msg)
    print('\nArtigo postado com sucesso no TabNews!')
    
    #precisa ser feito um sistema que vai receber a reposta 
    # do tabnews e verifica o status para saber se foi postado
    # ou não assim podendo mostrar no CMD


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())