from blog.datos import estados_post
def validar_post(post):
    """Comprueba que una publicacion tenga los datos necesarios."""
    campos_obligatorios = [
        "id",
        "titulo",
        "contenido",
        "autor",
        "tags",
        "estado"
    ]
    for campo in campos_obligatorios:
        if campo not in post:
            return False, f"Falta el campo obligatorio: {campo}"
    if not isinstance(post["id"], int):
        return False, "El ID debe ser un numero entero."
    if not isinstance(post["titulo"], str) or not post["titulo"].strip():
        return False, "El titulo no puede estar vacio."
    if not isinstance(post["contenido"], str) or not post["contenido"].strip():
        return False, "El contenido no puede estar vacio."
    if not isinstance(post["autor"], dict):
        return False, "El autor debe ser un diccionario."
    if not isinstance(post["tags"], list):
        return False, "Las etiquetas deben estar en una lista."
    if post["estado"] not in estados_post:
        return False, "El estado no es valido."
    return True, "Publicacion valida."
def validar_posts(posts):
    """Valida todas las publicaciones del blog."""
    resultados = []
    for post in posts:
        es_valido, mensaje = validar_post(post)
        resultados.append((post.get("titulo", "Sin titulo"), es_valido, mensaje))
    return resultados