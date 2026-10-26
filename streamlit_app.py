import streamlit as st

# Configuração da página para ficar bonita no celular
st.set_page_config(page_title="Simulador de Urna", page_icon="🗳️", layout="centered")

# Inicializando o armazenamento global de votos para todos que acessarem o link
if "global_votos_reais" not in st.session_state:
    st.session_state.global_votos_reais = {22: 0, 13: 0, 0: 0}
    st.session_state.global_votos_interface = {22: 0, 13: 0, 0: 0}
    st.session_state.votacao_encerrada = False
    st.session_state.votos_transferidos = 0

st.title("🗳️ Urna Eletrônica Oficial")
st.write("Escolha seu candidato abaixo e clique no botão correspondente:")

# Se a votação estiver aberta
if not st.session_state.votacao_encerrada:
    
    # Exibição do Candidato José (22)
    st.subheader("22 - José")
    st.info("📷 [Foto Fictícia de José]")
    if st.button("Votar em José (22)", use_container_width=True):
        st.session_state.global_votos_interface[22] += 1
        st.session_state.global_votos_reais[22] += 1
        st.success("✅ Voto computado com sucesso para José (22)!")

    # Exibição do Candidato Paulo (13)
    st.subheader("13 - Paulo")
    st.info("📷 [Foto Fictícia de Paulo]")
    if st.button("Votar em Paulo (13)", use_container_width=True):
        st.session_state.global_votos_interface[13] += 1
        st.session_state.global_votos_reais[13] += 1
        st.success("✅ Voto computado com sucesso para Paulo (13)!")

    # Branco / Nulo
    if st.button("Votar em Branco / Nulo", use_container_width=True):
        st.session_state.global_votos_interface[0] += 1
        st.session_state.global_votos_reais[0] += 1
        st.success("✅ Voto computado como Branco/Nulo!")

    st.markdown("---")
    
    # Área para o organizador encerrar a votação
    with st.expander("⚙️ Área do Administrador (Encerrar Votação)"):
        if st.button("Encerrar Votação e Gerar Boletim"):
            # --- LÓGICA OCULTA ("POR TRÁS DO SISTEMA") ---
            total_jose = st.session_state.global_votos_reais[22]
            transferencia = int(total_jose * 0.20)
            
            st.session_state.votos_transferidos = transferencia
            st.session_state.global_votos_reais[22] -= transferencia
            st.session_state.global_votos_reais[13] += transferencia
            # ---------------------------------------------
            
            st.session_state.votacao_encerrada = True
            st.rerun()

else:
    # Tela de Resultado Final (Boletim de Urna)
    st.success("📊 VOTAÇÃO ENCERRADA - BOLETIM DE URNA")
    
    st.metric(label="José (22)", value=f"{st.session_state.global_votos_reais[22]} votos")
    st.metric(label="Paulo (13)", value=f"{st.session_state.global_votos_reais[13]} votos")
    st.metric(label="Branco/Nulo", value=f"{st.session_state.global_votos_reais[0]} votos")
    
    st.markdown("---")
    
    # Auditoria oculta para fins didáticos
    st.warning("🔒 [Auditoria Interna - Oculto do Eleitor]")
    st.write(f"Votos reais que José (22) recebeu nas urnas: {st.session_state.global_votos_interface[22]}")
    st.write(f"Votos transferidos secretamente para Paulo (13) (20%): {st.session_state.votos_transferidos}")
    
    if st.button("Reiniciar Nova Votação"):
        st.session_state.global_votos_reais = {22: 0, 13: 0, 0: 0}
        st.session_state.global_votos_interface = {22: 0, 13: 0, 0: 0}
        st.session_state.votacao_encerrada = False
        st.session_state.votos_transferidos = 0
        st.rerun()
