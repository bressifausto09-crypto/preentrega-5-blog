from blog.datos import posts
def listar_posts():
    """Muestra todas las publicaciones del blog."""
    if not posts:
        print("No hay publicaciones para mostrar.")
        return
    print("\n--- LISTA DE PUBLICACIONES ---")
    for post in posts:
        print(f"\nID: {post['id']}")
        print(f"Titulo: {post['titulo']}")
        print(f"Estado: {post['estado']}")
        print(f"Etiquetas: {', '.join(post['tags'])}")
def buscar_por_titulo(titulo):
    """Busca publicaciones por titulo, sin distinguir mayusculas."""
    resultados = []
    for post in posts:
        if titulo.lower() in post["titulo"].lower():
            resultados.append(post)
    return resultados
def filtrar_por_tag(tag):
    """Filtra publicaciones por etiqueta, sin distinguir mayusculas."""
    resultados = []
    for post in posts:
        if any(tag.lower() == etiqueta.lower() for etiqueta in post["tags"]):
            resultados.append(post)
    return resultados