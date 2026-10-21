# Datos del autor del blog
perfil_autor = {
    "nombre": "Fausto",
    "bio": "Creador de contenido sobre programacion y tecnologia",
    "especialidad": "Python y desarrollo de software",
    "redes_sociales": ["fausto_dev", "fausto_python"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Python", "Django", "Web", "Backend"}

posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "Aprenderemos los fundamentos de Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Introduccion al desarrollo web",
        "contenido": "Conceptos basicos del desarrollo web.",
        "autor": perfil_autor,
        "tags": ["Python", "Web", "Backend"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "contenido": "Aprendiendo a organizar informacion.",
        "autor": perfil_autor,
        "tags": ["Python", "Diccionarios"],
        "estado": "archivado"
    }
]
