from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.datos import posts
from blog.validaciones import validar_posts
def mostrar_resultados(resultados):
    if not resultados:
        print("\nNo se encontraron publicaciones.")
        return
    for post in resultados:
        print(f"\nID: {post['id']}")
        print(f"Titulo: {post['titulo']}")
        print(f"Estado: {post['estado']}")
        print(f"Etiquetas: {', '.join(post['tags'])}")
def mostrar_menu():
    while True:
        print("\n===== BLOG DE CONSOLA =====")
        print("1. Listar publicaciones")
        print("2. Buscar por titulo")
        print("3. Filtrar por etiqueta")
        print("4. Validar publicaciones")
        print("5. Salir")
        opcion = input("Elegí una opcion: ").strip()
        if opcion == "1":
            listar_posts()
        elif opcion == "2":
            titulo = input("Escribi el titulo o una palabra: ").strip()
            resultados = buscar_por_titulo(titulo)
            mostrar_resultados(resultados)
        elif opcion == "3":
            tag = input("Escribi la etiqueta: ").strip()
            resultados = filtrar_por_tag(tag)
            mostrar_resultados(resultados)
        elif opcion == "4":
            print("\n--- VALIDACION DE PUBLICACIONES ---")
            for titulo, es_valido, mensaje in validar_posts(posts):
                estado = "VALIDO" if es_valido else "INVALIDO"
                print(f"{titulo}: {estado} - {mensaje}")
        elif opcion == "5":
            print("Gracias por usar el blog. ¡Hasta luego!")
            break
        else:
            print("Opcion incorrecta. Elegi un numero del 1 al 5.")