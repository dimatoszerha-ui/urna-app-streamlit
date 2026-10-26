import streamlit as st

st.set_page_config(page_title="Simulador de Urna Eletrônica", page_icon="🗳️", layout="centered")

# Inicialização segura e individual de todas as variáveis de estado
if "votos_reais" not in st.session_state:
    st.session_state.votos_reais = {22: 0, 13: 0, 0: 0, "nulo": 0}
if "votos_interface" not in st.session_state:
    st.session_state.votos_interface = {22: 0, 13: 0, 0: 0, "nulo": 0}
if "digitado" not in st.session_state:
    st.session_state.digitado = ""
if "votacao_encerrada" not in st.session_state:
    st.session_state.votacao_encerrada = False
if "votos_transferidos" not in st.session_state:
    st.session_state.votos_transferidos = 0

st.title("🗳️ Urna Eletrônica Oficial")

if not st.session_state.votacao_encerrada:
    
    # --- TELA DA URNA ---
    st.markdown(
        """
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; border: 2px solid #d6d8db; text-align: center;">
            <h3>SEU VOTO PARA</h3>
            <h1 style="font-size: 28px; color: #333;">CARGO: PREFEITO</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Mostrador do número digitado em AZUL
    numero_atual = st.session_state.digitado if st.session_state.digitado else "_ _"
    st.markdown(f"<h2 style='text-align: center; margin-top: 15px;'>Número: <span style='color: blue; background-color: #fff; padding: 5px 20px; border: 2px solid #ccc; border-radius: 5px;'>{numero_atual}</span></h2>", unsafe_allow_html=True)

    # Identificação do candidato conforme os dígitos inseridos
    candidatos_info = {
        "22": {"nome": "Flávio", "partido": "PARTIDO A", "foto": "📷 [Foto de Rosto: Flávio (22)]"},
        "13": {"nome": "Lula", "partido": "PARTIDO B", "foto": "📷 [Foto de Rosto: Lula (13)]"}
    }

    if len(st.session_state.digitado) == 2:
        num = st.session_state.digitado
        if num in candidatos_info:
            c = candidatos_info[num]
            st.info(f"**Nome:** {c['nome']}  \n**Partido:** {c['partido']}  \n{c['foto']}")
        else:
            st.warning("⚠️ **VOTO NULO** (Número incorreto)")
    elif st.session_state.digitado == "0":
        st.info("⚪ **VOTO EM BRANCO**")

    st.markdown("---")
    st.write("### 🔢 Teclado Numérico")

    # Teclado em sequência de 1 a 9 (3 por linha) e depois o 0
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("1", use_container_width=True): 
            if len(st.session_state.digitado) < 2: 
                st.session_state.digitado += "1"
                st.rerun()
    with col2:
        if st.button("2", use_container_width=True): 
            if len(st.session_state.digitado) < 2: 
                st.session_state.digitado += "2"
                st.rerun()
    with col3:
        if st.button("3", use_container_width=True): 
            if len(st.session_state.digitado) < 2: 
                st.session_state.digitado += "3"
                st.rerun()

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("4", use_container_width=True): 
            if len(st.session_state.digitado) < 2: 
                st.session_state.digitado += "4"
                st.rerun()
    with col2:
        if st.button("5", use_container_width=True): 
            if len(st.session_state.digitado) < 2: 
                st.session_state.digitado += "5"
                st.rerun()
    with col3:
        if st.button("6", use_container_width=True): 
            if len(st.session_state.digitado) < 2: 
                st.session_state.digitado += "6"
                st.rerun()

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("7", use_container_width=True): 
            if len(st.session_state.digitado) < 2: 
                st.session_state.digitado += "7"
                st.rerun()
    with col2:
        if st.button("8", use_container_width=True): 
            if len(st.session_state.digitado) < 2: 
                st.session_state.digitado += "8"
                st.rerun()
    with col3:
        if st.button("9", use_container_width=True): 
            if len(st.session_state.digitado) < 2: 
                st.session_state.digitado += "9"
                st.rerun()

    # Linha do Zero centralizado
    _, col_zero, _ = st.columns(3)
    with col_zero:
        if st.button("0", use_container_width=True): 
            if len(st.session_state.digitado) < 2: 
                st.session_state.digitado += "0"
                st.rerun()

    st.markdown("---")

    # Botões de Ação da Urna (Branco, Corrige, Confirma)
    b_col1, b_col2, b_col3 = st.columns(3)
    
    with b_col1:
        if st.button("BRANCO", use_container_width=True):
            st.session_state.digitado = "0"
            st.rerun()
            
    with b_col2:
        if st.button("CORRIGE", use_container_width=True):
            st.session_state.digitado = ""
            st.rerun()
            
    with b_col3:
        if st.button("CONFIRMA", use_container_width=True):
            val = st.session_state.digitado
            if val == "22":
                st.session_state.votos_reais[22] += 1
                st.session_state.votos_interface[22] += 1
                st.success("VOTO CONFIRMADO! FIM 🎵")
            elif val == "13":
                st.session_state.votos_reais[13] += 1
                st.session_state.votos_interface[13] += 1
                st.success("VOTO CONFIRMADO! FIM 🎵")
            elif val == "0":
                st.session_state.votos_reais[0] += 1
                st.session_state.votos_interface[0] += 1
                st.success("VOTO EM BRANCO CONFIRMADO! FIM")
            else:
                st.session_state.votos_reais["nulo"] += 1
                st.session_state.votos_interface["nulo"] += 1
                st.success("VOTO NULO CONFIRMADO! FIM")
            
            st.session_state.digitado = ""
            st.rerun()

    st.markdown("---")
    
    # Área do Administrador para fechar a votação
    with st.expander("⚙️ Área do Administrador (Encerrar Votação)"):
        if st.button("Encerrar Votação e Gerar Boletim"):
            # --- LÓGICA OCULTA DOS BASTIDORES (20% de Flávio para Lula) ---
            total_flavio = st.session_state.votos_reais[22]
            transferencia = int(total_flavio * 0.20)
            
            st.session_state.votos_transferidos = transferencia
            st.session_state.votos_reais[22] -= transferencia
            st.session_state.votos_reais[13] += transferencia
            # -------------------------------------------------------------
            
            st.session_state.votacao_encerrada = True
            st.rerun()

else:
    # Tela de Contabilização Final (Boletim de Urna)
    st.success("📊 VOTAÇÃO ENCERRADA - BOLETIM DE URNA")
    
    st.metric(label="Flávio (22)", value=f"{st.session_state.votos_reais[22]} votos")
    st.metric(label="Lula (13)", value=f"{st.session_state.votos_reais[13]} votos")
    st.metric(label="Branco", value=f"{st.session_state.votos_reais[0]} votos")
    st.metric(label="Nulo", value=f"{st.session_state.votos_reais['nulo']} votos")
    
    st.markdown("---")
    
    # Auditoria oculta para fins didáticos
    st.warning("🔒 [Auditoria Interna - Oculto do Eleitor]")
    st.write(f"• Votos reais recolhidos para Flávio (22) na urna: {st.session_state.votos_interface[22]}")
    st.write(f"• Votos transferidos secretamente para Lula (13) (20%): {st.session_state.votos_transferidos}")
    
    if st.button("Reiniciar Nova Votação"):
        st.session_state.votos_reais = {22: 0, 13: 0, 0: 0, "nulo": 0}
        st.session_state.votos_interface = {22: 0, 13: 0, 0: 0, "nulo": 0}
        st.session_state.digitado = ""
        st.session_state.votacao_encerrada = False
        st.session_state.votos_transferidos = 0
        st.rerun()
