from comunidadeimpressionadora import app,database
from comunidadeimpressionadora.models import Usuario

#with app.app_context():
#    database.create_all()
# so precisa rodar 1 vez para criar o banco de dados


#with app.app_context():
#    #usuario = Usuario(username='Lira', email='lira@gmail.com', senha='123456')
#    usuario2 = Usuario(username='Joao', email='joao@gmail.com', senha='123456')
#
#    #database.session.add(usuario)
#    database.session.add(usuario2)
#
#    database.session.commit()

# with app.app_context():
#    meus_usuarios = Usuario.query.all()
#    print(meus_usuarios)
#    for usuario in meus_usuarios:
#        print(usuario.username,usuario.email,usuario.senha)
#
#    usuario_teste = Usuario.query.filter_by(id=2).first()
#    print(usuario_teste.username)

#with app.app_context():
#    meu_post = Post(id_usuario=1, titulo='Primeiro post do Lira', corpo = 'Lira voando')
#    database.session.add(meu_post)
#    database.session.commit()

# with app.app_context():
#     post = Post.query.first()
#     print(post.autor.email)


with app.app_context():
#    database.drop_all()
    database.create_all()