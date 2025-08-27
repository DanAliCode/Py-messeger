# Importando biblioteca
import streamlit as st
from unidecode import unidecode 
import time
from back_end import *

# Layouts ===================================================================

def login_page():
    st.header('🐍PyMesseger', divider=True)
    
    tab1, tab2 = st.tabs(['Entrar', 'Cadastrar'])
    
    with tab1.form(key='Login'):
        login_user = st.text_input('Digite seu nome de usuario')
        login_pass = st.text_input('Digite sua senha')
        if st.form_submit_button('Entrar'):
            user_login(login_user, login_pass)
        
    with tab2.form(key='Register'):
        register_user = st.text_input('Crie seu usuario')
        register_pass = st.text_input('Crie sua senha')
        if st.form_submit_button('Cadastrar'):
            register_new_user(register_user,register_pass)
        

def user_login(user,password):
    
    if authenticator_password(user, password):
        st.success('Login efetuado com sucesso')
        time.sleep(2)
        st.session_state['usuario_logado'] = unidecode(user.replace(" ", "_").upper())
        change_page('chat')
        st.rerun()    
    else:
        st.error('Erro ao efetuar o login')


def register_new_user(user,password):
    
    if save_new_user(user=user,password=password):
        st.success('Usuário cadastrado com sucesso')
        time.sleep(3)
        st.session_state['usuario_logado'] = user.upper()
        change_page('chat')
        st.rerun()
    else:
        st.error('Erro ao cadastrar o usuário')
        


def change_page(pagename):
    st.session_state['stay_page'] = pagename
    

# Criando o titulo da tela

def chat_page():
    st.header('🐍PyMesseger')
    st.divider()
    

    usuario_logado = st.session_state['usuario_logado']
    talking_to = st.session_state['talking_to']
    
    mensagens = read_messeger_storage(usuario_logado, talking_to)
    
    
    for mensagem in mensagens:
        nome_usuario = 'user' if mensagem['nome_usuario'] == usuario_logado else mensagem['nome_usuario']
        avatar = None if mensagem['nome_usuario'] == usuario_logado else '😄'
        chat = st.chat_message(nome_usuario, avatar=avatar)
        chat.markdown(mensagem['conteudo'])
        
    nova_mensagem = st.chat_input('Digite uma mensagem')
    
    if nova_mensagem:
        if nova_mensagem != st.session_state['last_send_messege']:
            
            st.session_state['last_send_messege'] = nova_mensagem
            usermessager = {'nome_usuario': usuario_logado,
                            'conteudo': nova_mensagem}
            
            chat = st.chat_message('user')
            chat.markdown(usermessager['conteudo'])
            mensagens.append(usermessager)
            messeger_storage(usuario_logado, talking_to, mensagens)
            

def init_messeger():
    if not 'stay_page' in st.session_state:
        change_page('login')
    if not 'usuario_logado' in st.session_state:
        st.session_state['usuario_logado'] = ''
    if not 'talking_to' in st.session_state:
        st.session_state['talking_to'] = ''
    if not 'last_send_messege' in st.session_state:
        st.session_state['last_send_messege'] = ''
        


def page_select_talk(element):
    
    if not st.session_state['talking_to'] == '':
        element.title(f"Conversando com :blue[{st.session_state['talking_to']}]")
        element.divider()
    
    users = user_list()
    users = [u for u in users if u != st.session_state['usuario_logado']]
    talking_to = element.selectbox('Selecione o usuario que deseja conversa',users)
    element.button('Iniciar Conversa', on_click=select_talk, args=(talking_to, ))
    
def select_talk(talking_to):
    
    st.session_state['talking_to'] = talking_to
    st.success(f'Iniciando conversa com {talking_to}')
    time.sleep(1)
    change_page('chat')
    

       
def main():
    
    init_messeger()
        
    if st.session_state['stay_page'] == 'login':
        login_page()
    elif st.session_state['stay_page'] == 'chat':
        if st.session_state['talking_to'] == '':
            containt = st.container()
            page_select_talk(containt)
        else:
            chat_page()
            containt = st.sidebar.container()
            page_select_talk(containt)
            time.sleep(1)
            st.rerun()

    
    
if __name__ == '__main__':
    main()