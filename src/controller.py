from flask import Blueprint, render_template, request, redirect, url_for, session


class Controller:
    def __init__(self, model):
        self.controller = Blueprint('controller', __name__, static_folder='view/static', template_folder='view/templates')
        self.model = model

        # Decorador home
        self.controller.add_url_rule('/', 'home', self.home, methods=['GET', 'POST'])

        # Decorador historico
        self.controller.add_url_rule('/historico', 'historico', self.historico, methods=['GET', 'POST'])

        # Decorador historico_usuario
        self.controller.add_url_rule('/historico/<usuario_id>', 'historico_usuario', self.historico_usuario, methods=['GET', 'POST'])

        # Decorador classificador
        self.controller.add_url_rule('/classificador', 'classificador', self.classificador, methods=['GET', 'POST'])

        # Decorador resultado (sem parâmetro na URL)
        self.controller.add_url_rule('/resultado', 'resultado', self.resultado, methods=['GET', 'POST'])


    def home(self):
        return render_template('home.html')
    
    def historico(self):
        lista = self.model.listar_usuarios()
        return render_template('historico.html', usuarios=lista)
    
    def historico_usuario(self, usuario_id):
        usuario = self.model.get_usuario(usuario_id)

        return render_template('historico_usuario.html', usuario=usuario)



    def classificador(self):
        if request.method == 'POST':
            nome = request.form.get('nome')
            peso = float(request.form.get('peso'))
            altura = float(request.form.get('altura'))
            flexibilidade = float(request.form.get('flexibilidade'))
            arremesso = float(request.form.get('arremesso'))
            s_horizontal = float(request.form.get('s_horizontal'))
            s_vertical = float(request.form.get('s_vertical'))


            posicao = self.model.classificar_posicao(peso, altura, flexibilidade, arremesso, s_horizontal, s_vertical)

            self.model.registrar_usuario(nome, peso, altura, flexibilidade, arremesso, s_horizontal, s_vertical, posicao)

            session['ultimo_usuario'] = {
                'nome': nome,
                'peso': peso,
                'altura': altura,
                'flexibilidade': flexibilidade,
                'arremesso': arremesso,
                's_horizontal': s_horizontal,
                's_vertical': s_vertical,
                'posicao': posicao
            }

            return redirect(url_for('controller.resultado'))


        return render_template('classificador.html')
    
    def resultado(self):
        ultimo_usuario = session.get('ultimo_usuario')

        if not ultimo_usuario:
            return redirect(url_for('controller.classificador'))
        
        session.pop('ultimo_usuario', None)

        return render_template('resultado.html', ultimo_usuario=ultimo_usuario)
        
    