import pygame
import random
import sys
import os
import requests
import time

# -------------------- Ir para a pasta do script --------------------
try:
    diretorio_atual = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(diretorio_atual)
except Exception:
    pass

# -------------------- Função util: baixar_arquivo --------------------
def baixar_arquivo(nome, url, pasta):
    try:
        if not os.path.exists(pasta):
            os.makedirs(pasta)
        caminho_local = os.path.join(pasta, nome)
        if os.path.exists(caminho_local):
            return caminho_local
        print(f"[download] Baixando {url}")
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        with open(caminho_local, "wb") as f:
            f.write(resp.content)
        return caminho_local
    except Exception as e:
        print(f"[baixar_arquivo] falha ao baixar {url}: {e}")
        return None

# -------------------- Inicialização --------------------
pygame.init()
clock = pygame.time.Clock()

# -------------------- Tela e cores --------------------
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Rpanng")

VERDE_ESCURO = (34, 139, 34)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
CINZA_CLARO = (200, 200, 200)
AMARELO_OURO = (255, 215, 0)
COR_CARTA = (40, 40, 60)
COR_BORDA_CARTA = (100, 100, 120)

# -------------------- URLs --------------------
URL_MAP = {
    "pann.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/pann.png",
    "pann_dano.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/pann_dano.png",
    "pann_meia_vida.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/pann_meia_vida.png",
    "pann_triste.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/pann_triste.png",
    "painel_status.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/painel_status.png",
    "o_sol.webp": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/o_sol.webp",
    "Sol.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/Sol.png",
    "menu.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/menu.png",
    "j1.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/j1.png",
    "carta_pann.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/carta_pann.png",
    "carta_michael.jpeg": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/carta_michael.jpeg",
    "botao_lutar.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/botao_lutar.png",
    "botao_fugir.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/botao_fugir.png",
    "Macaco.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/Macaco.png",
    "Lobo.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/Lobo.png",
    "Gato.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/Gato.png",
    "Slime.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/Slime.png",
    "michael.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/michael.png",
    "michael_dano.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/michael_dano.png",
    "michael_meia_vida.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/michael_meia_vida.png",
    "michael_triste.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/michael_triste.png",
    "tela_inicial.jpeg": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/tela_inicial.jpeg",
    "fundo_cartas.jpeg": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/fundo_cartas.png",
    "fundo_slime": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/fundo_slime.png",
    "botao_espada.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/botao_espada.png",
    "botao_magia.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/botao_magia.png",
    "botao_descansar.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/botao_descansar.png",
    "botao_voltar.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/botao_voltar.png",
    "fundo_lobo.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/fundo_lobo.png",
    "fundo_macaco.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/fundo_macaco.png",
    "fundo_gato.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/fundo_gato.png",
    "botao_beat_it.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/botao_beat_it.png",
    "botao_thriller.png": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/botao_thriller.png",
    "botao_earth_song.png": "https://github.com/Samuenpd/meu-jogo-imagens/blob/91daae905ca9786c1c128ace50563bf4486ec8d7/botao_earth_song.png",
}

URL_FONTES = {
    "OMORI_GAME2.ttf": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/OMORI_GAME2.ttf"
}

URL_MUSICAS = {
    "batalha.mp3": "https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/8943d874c3004064ac9e38c1578150a238f57cc5/Batalha.mp3"
}

# -------------------- Carregar imagem com cache local --------------------
def carregar_imagem(caminho, largura=None, altura=None, fallback_cor=(80, 80, 80), on_fail="surface"):
    try:
        if not caminho:
            raise FileNotFoundError("caminho vazio")

        # 1) Caminho local literal
        if os.path.exists(caminho):
            img = pygame.image.load(caminho).convert_alpha()
            if largura and altura:
                img = pygame.transform.scale(img, (largura, altura))
            return img

        # 2) Caminho local na pasta 'imagens'
        pasta = "imagens"
        if not os.path.exists(pasta):
            os.makedirs(pasta)
        nome_arquivo = os.path.basename(caminho)
        caminho_local = os.path.join(pasta, nome_arquivo)
        if os.path.exists(caminho_local):
            img = pygame.image.load(caminho_local).convert_alpha()
            if largura and altura:
                img = pygame.transform.scale(img, (largura, altura))
            return img

        # 3) Baixar
        if str(caminho).lower().startswith("http"):
            url = caminho
        elif caminho in URL_MAP:
            url = URL_MAP[caminho]
        else:
            url = f"https://raw.githubusercontent.com/Samuenpd/meu-jogo-imagens/main/{caminho}"

        try:
            print(f"[download] Baixando {url}")
            resp = requests.get(url, timeout=15)
            resp.raise_for_status()
            with open(caminho_local, "wb") as f:
                f.write(resp.content)
            img = pygame.image.load(caminho_local).convert_alpha()
            if largura and altura:
                img = pygame.transform.scale(img, (largura, altura))
            return img
        except Exception as e:
            print(f"[carregar_imagem] falha ao baixar {url}: {e}")
            if on_fail == "none":
                return None
            w = largura if largura else 50
            h = altura if altura else 50
            surf = pygame.Surface((w, h), pygame.SRCALPHA)
            surf.fill(fallback_cor)
            return surf

    except Exception as e:
        print(f"[carregar_imagem] erro: {e}")
        if on_fail == "none":
            return None
        w = largura if largura else 50
        h = altura if altura else 50
        surf = pygame.Surface((w, h), pygame.SRCALPHA)
        surf.fill(fallback_cor)
        return surf

# -------------------- Fontes --------------------
try:
    caminho_fonte = baixar_arquivo("OMORI_GAME2.ttf", URL_FONTES["OMORI_GAME2.ttf"], "fontes")
    if caminho_fonte and os.path.exists(caminho_fonte):
        fonte = pygame.font.Font(caminho_fonte, 36)
        fonte_pequena = pygame.font.Font(caminho_fonte, 24)
    else:
        fonte = pygame.font.Font(None, 36)
        fonte_pequena = pygame.font.Font(None, 28)
except Exception as e:
    print(f"[fonte] erro: {e}")
    fonte = pygame.font.Font(None, 36)
    fonte_pequena = pygame.font.Font(None, 28)

# -------------------- Música --------------------
try:
    pygame.mixer.init()
    caminho_musica = baixar_arquivo("batalha.mp3", URL_MUSICAS["batalha.mp3"], "musicas")
    if caminho_musica:
        pygame.mixer.music.load(caminho_musica)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
except Exception as e:
    print(f"[musica] erro: {e}")


# -------------------- Dados dos personagens --------------------
PERSONAGENS_JOGAVEIS = {
    "Pann": {
        "nome": "Pann",
        "imagem_normal": "pann.png",
        "imagem_dano": "pann_dano.png",
        "imagem_morto": "pann_triste.png",
        "imagem_hp_baixo": "pann_meia_vida.png",
        "vida": 250,
        "mana": 50,
        "dano_espada": 30,
        "dano_magia": 50,
        "imagem_carta": "carta_pann.png",
    },
    "Michael": {
        "nome": "Michael",
        "imagem_normal": "michael.png",
        "imagem_dano": "michael_dano.png",
        "imagem_morto": "michael_triste.png",
        "imagem_hp_baixo": "michael_meia_vida.png",
        "vida": 99,
        "mana": 99,
        "dano_espada": 999,
        "dano_magia": 999,
        "imagem_carta": "carta_michael.jpeg",
    }
}

# -------------------- Imagens globais (monstros, fundo, UI) --------------------
imagem_sol   = carregar_imagem('Sol.png',   400, 300, (255, 230, 0))
imagem_slime = carregar_imagem('Slime.png', 400, 300, (0, 200, 200))
imagem_lobo  = carregar_imagem('Lobo.png',  400, 300, (120, 120, 120))
imagem_gato  = carregar_imagem('Gato.png',  400, 300, (150, 150, 150))
imagem_macaco= carregar_imagem('Macaco.png',400, 300, (150, 100, 50))

fundo_sol = carregar_imagem('o_sol.webp', LARGURA_TELA, ALTURA_TELA, (0, 0, 0))
fundo_slime = carregar_imagem('fundo_slime.png', LARGURA_TELA, ALTURA_TELA, (0, 0, 0))
fundo_lobo = carregar_imagem('fundo_lobo.png', LARGURA_TELA, ALTURA_TELA, (0, 0, 0))
fundo_macaco = carregar_imagem('fundo_macaco.png', LARGURA_TELA, ALTURA_TELA, (0, 0, 0))
fundo_gato = carregar_imagem('fundo_gato.png', LARGURA_TELA, ALTURA_TELA, (0, 0, 0))

imagem_menu = carregar_imagem('menu.png', 50, 50, (100, 100, 100))
imagem_painel_fundo = carregar_imagem('painel_status.png', 155, 226, (50, 50, 50))
imagem_tela_inicial = carregar_imagem("tela_inicial.jpeg", LARGURA_TELA, ALTURA_TELA, (0, 0, 0))
imagem_tela_seleção = carregar_imagem('fundo_cartas.png', LARGURA_TELA, ALTURA_TELA, (0, 0, 0))

imagem_botao_lutar = carregar_imagem('botao_lutar.png', 336, 79, (180, 40, 40))
imagem_botao_fugir = carregar_imagem('botao_fugir.png', 336, 79, (40, 40, 180))
imagem_botao_espada = carregar_imagem('botao_espada.png', 183, 53, (40, 40, 180))
imagem_botao_magia = carregar_imagem('botao_magia.png', 183, 53, (40, 40, 180))
imagem_botao_descansar = carregar_imagem('botao_descansar.png', 183, 53, (40, 40, 180))
imagem_botao_voltar = carregar_imagem('botao_voltar.png', 183, 53, (40, 40, 180))


# -------------------- Estados e variáveis --------------------
estado_do_jogo = "menu_inicial"
jogador_atacou = False
tempo_ataque_jogador_fim = 0
menu_acao = "principal"
jogador = None
painel_jogador = None
monstro_atual = None
monstros_disponiveis = None

# -------------------- Classes --------------------
class Jogador:
    def __init__(self, nome, vida, mana, dano_espada, dano_magia,
                 imagem_normal, imagem_dano, imagem_morto, imagem_hp_baixo):
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.dano_espada = dano_espada
        self.dano_magia = dano_magia
        self.vida_max = vida
        self.mana_max = mana
        self.esta_danificado = False
        self.tempo_danificado_fim = 0
        self.imagem_normal   = carregar_imagem(imagem_normal,   150, 150, (0, 90, 200))
        self.imagem_dano     = carregar_imagem(imagem_dano,     150, 150, (255, 215, 0))
        self.imagem_morto    = carregar_imagem(imagem_morto,    150, 150, (200, 30, 30))
        self.imagem_hp_baixo = carregar_imagem(imagem_hp_baixo, 150, 150, (0, 200, 80))

    def esta_vivo(self):
        return self.vida > 0

class CartaPersonagem:
    def __init__(self, x, y, largura, altura, dados_personagem, imagem_carta_completa=None, imagem_personagem=None):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.dados_personagem = dados_personagem
        self.nome = dados_personagem.get("nome", "?")
        self.imagem_carta_completa = imagem_carta_completa
        self.imagem_personagem = imagem_personagem 

    def desenhar(self, tela):
        if self.imagem_carta_completa is not None:
            img_rect = self.imagem_carta_completa.get_rect(center=self.rect.center)
            tela.blit(self.imagem_carta_completa, img_rect)
        else:
            pygame.draw.rect(tela, COR_CARTA, self.rect, border_radius=10)
            pygame.draw.rect(tela, COR_BORDA_CARTA, self.rect, 3, border_radius=10)
            if self.imagem_personagem:
                img_rect = self.imagem_personagem.get_rect(center=(self.rect.centerx, self.rect.centery - 20))
                tela.blit(self.imagem_personagem, img_rect)
            texto_nome = fonte_pequena.render(self.nome, True, BRANCO)
            texto_rect = texto_nome.get_rect(center=(self.rect.centerx, self.rect.bottom - 22))
            tela.blit(texto_nome, texto_rect)

    def is_clicado(self, pos):
        return self.rect.collidepoint(pos)

class Monstro:
    def __init__(self, nome, vida, dano, imagem=None, background_img=None):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.imagem = imagem
        self.background_img = background_img
        self.x = LARGURA_TELA // 2
        self.y = ALTURA_TELA // 2
        self.vida_max = vida
        self.largura = 50
        self.altura = 50

    def esta_vivo(self):
        return self.vida > 0

    def desenhar(self):
        barra_vida_largura, barra_vida_altura = 100, 10
        if self.imagem:
            posicao_x = self.x - self.imagem.get_width() / 2
            posicao_y = self.y - self.imagem.get_height() / 2
            tela.blit(self.imagem, (posicao_x, posicao_y))
            barra_vida_x = self.x - barra_vida_largura / 2
            barra_vida_y = self.y - self.imagem.get_height() / 2 - 15
        else:
            pygame.draw.rect(tela, VERMELHO, (self.x, self.y, self.largura, self.altura))
            barra_vida_x = self.x - (barra_vida_largura - self.largura) / 2
            barra_vida_y = self.y - 15

        pygame.draw.rect(tela, BRANCO, (barra_vida_x, barra_vida_y, barra_vida_largura, barra_vida_altura))
        vida_atual_largura = (self.vida / self.vida_max) * barra_vida_largura
        if vida_atual_largura > 0:
            pygame.draw.rect(tela, VERDE, (barra_vida_x, barra_vida_y, int(vida_atual_largura), barra_vida_altura))

class Botao:
    def __init__(self, x, y, largura, altura, texto="", cor=None, cor_texto=None, imagem=None):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor = cor
        self.cor_texto = cor_texto
        self.imagem = imagem

    def desenhar(self, tela, debug=False):
        if self.imagem:
            imagem_rect = self.imagem.get_rect(center=self.rect.center)
            tela.blit(self.imagem, imagem_rect)
        elif self.cor:
            pygame.draw.rect(tela, self.cor or CINZA_CLARO, self.rect)
            if self.texto:
                texto_renderizado = fonte.render(self.texto, True, self.cor_texto or PRETO)
                texto_rect = texto_renderizado.get_rect(center=self.rect.center)
                tela.blit(texto_renderizado, texto_rect)
        else:
            if self.texto:
                texto_renderizado = fonte.render(self.texto, True, self.cor_texto or PRETO)
                texto_rect = texto_renderizado.get_rect(center=self.rect.center)
                tela.blit(texto_renderizado, texto_rect)

    def is_clicado(self, pos):
        return self.rect.collidepoint(pos)

class LogCombate:
    def __init__(self, x, y, largura, altura, fonte):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.fonte = fonte
        self.mensagens = []
        self.max_mensagens = 5
        self.caracteres_exibidos = 0
        self.tempo_ultimo_caractere = pygame.time.get_ticks()
        self.intervalo_caractere = 30

    def limpar(self):
        self.mensagens = []
        self.caracteres_exibidos = 0

    def quebrar_texto(self, texto):
        palavras = texto.split(' ')
        linhas_quebradas = []
        linha_atual = ''
        for palavra in palavras:
            teste_linha = (linha_atual + ' ' + palavra) if linha_atual else palavra
            if self.fonte.size(teste_linha)[0] <= self.rect.width - 20:
                linha_atual = teste_linha
            else:
                linhas_quebradas.append(linha_atual)
                linha_atual = palavra
        linhas_quebradas.append(linha_atual)
        return linhas_quebradas

    def adicionar_mensagem(self, mensagem):
        linhas = self.quebrar_texto(mensagem)
        for linha in linhas:
            self.mensagens.append(linha)
        while len(self.mensagens) > self.max_mensagens:
            self.mensagens.pop(0)
        self.caracteres_exibidos = 0
        self.tempo_ultimo_caractere = pygame.time.get_ticks()

    def atualizar(self):
        if self.mensagens:
            agora = pygame.time.get_ticks()
            if agora - self.tempo_ultimo_caractere > self.intervalo_caractere:
                if self.caracteres_exibidos < len(self.mensagens[-1]):
                    self.caracteres_exibidos += 1
                    self.tempo_ultimo_caractere = agora

    def desenhar(self, tela):
        pygame.draw.rect(tela, PRETO, self.rect)
        pygame.draw.rect(tela, BRANCO, self.rect, 2)
        y_offset = 10
        for i in range(len(self.mensagens) - 1):
            texto_renderizado = self.fonte.render(self.mensagens[i], True, BRANCO)
            tela.blit(texto_renderizado, (self.rect.x + 10, self.rect.y + y_offset))
            y_offset += 25
        if self.mensagens:
            texto_em_exibicao = self.mensagens[-1][:self.caracteres_exibidos]
            texto_renderizado = self.fonte.render(texto_em_exibicao, True, BRANCO)
            tela.blit(texto_renderizado, (self.rect.x + 10, self.rect.y + y_offset))

class PainelStatus:
    def __init__(self, x, y, nome, vida, mana, vida_max, mana_max, imagem_fundo):
        self.x = x
        self.y = y
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.vida_max = vida_max
        self.mana_max = mana_max
        self.imagem_fundo = imagem_fundo
        if self.imagem_fundo:
            self.largura, self.altura = self.imagem_fundo.get_size()
        else:
            self.largura, self.altura = 200, 200

    def desenhar(self, tela, fundo, imagem_atual):
        if self.imagem_fundo:
            tela.blit(self.imagem_fundo, (self.x, self.y))
        else:
            pygame.draw.rect(tela, (0, 0, 0), (self.x, self.y, self.largura, self.altura))
            pygame.draw.rect(tela, (255, 255, 255), (self.x, self.y, self.largura, self.altura), 3)

        tela.blit(imagem_atual, (self.x +5, self.y +12 ))

        hp_bar_x, hp_bar_y, hp_bar_width, hp_bar_height = self.x + 30, self.y + 173, 116, 19
        porcentagem_vida = max(0, self.vida / self.vida_max) if self.vida_max else 0
        cor_hp = (255, 0, 0)
        pygame.draw.rect(tela, (0, 0, 0), (hp_bar_x, hp_bar_y, hp_bar_width, hp_bar_height),border_radius=500)
        pygame.draw.rect(tela, cor_hp, (hp_bar_x, hp_bar_y, int(hp_bar_width * porcentagem_vida), hp_bar_height),border_radius=500)
        vida_txt = fonte_pequena.render(f"{self.vida}/{self.vida_max}", True, (255, 255, 255))
        tela.blit(vida_txt, vida_txt.get_rect(center=(hp_bar_x + hp_bar_width / 2, hp_bar_y + hp_bar_height / 2)))

        mp_bar_x, mp_bar_y, mp_bar_width, mp_bar_height = self.x + 30, self.y + 202, 116, 19
        porcentagem_mana = max(0, self.mana / self.mana_max) if self.mana_max else 0
        pygame.draw.rect(tela, (0, 0, 128), (mp_bar_x, mp_bar_y, mp_bar_width, mp_bar_height),border_radius=500)
        pygame.draw.rect(tela, (0, 128, 255), (mp_bar_x, mp_bar_y, int(mp_bar_width * porcentagem_mana), mp_bar_height),border_radius=500)
        mana_txt = fonte_pequena.render(f"{self.mana}/{self.mana_max}", True, (255, 255, 255))
        tela.blit(mana_txt, mana_txt.get_rect(center=(mp_bar_x + mp_bar_width / 2, mp_bar_y + mp_bar_height / 2)))

# -------------------- Mecânicas --------------------
def atacar(atacante, alvo, tipo_ataque="espada"):
    global jogador_atacou, tempo_ataque_jogador_fim
    jogador_atacou = True
    tempo_ataque_jogador_fim = pygame.time.get_ticks() + 1500
    if tipo_ataque == "espada":
        dado_ataque = random.randint(1, 20)
        if dado_ataque >= 17:
            dano = atacante.dano_espada * 2
            log.adicionar_mensagem(f'Deu {dano} de dano Crítico!')
        elif dado_ataque >= 10:
            dano = atacante.dano_espada
            log.adicionar_mensagem(f'Deu {dano} de dano!')
        else:
            dano = 0
            log.adicionar_mensagem('Ele desviou do ataque!')
        if dano > 0:
            alvo.vida -= dano
    elif tipo_ataque == "magia":
        custo_mana = 10
        if atacante.mana < custo_mana:
            log.adicionar_mensagem('Mana insuficiente!')
            jogador_atacou = False
            return
        atacante.mana -= custo_mana
        dado_ataque = random.randint(1, 20)
        if dado_ataque >= 12:
            dano = atacante.dano_magia
            log.adicionar_mensagem(f'Acertou a magia deu {dano} de dano!')
            alvo.vida -= dano
        else:
            log.adicionar_mensagem('Ele desviou da magia!')


def ataque_monstro(monstro, jogador):
    dado_ataque = random.randint(1, 20)
    if dado_ataque >= 11:
        dano = monstro.dano
        jogador.vida -= dano
        log.adicionar_mensagem(f'O {monstro.nome} te acertou! Recebeu {dano} de dano.')
        jogador.esta_danificado = True
        jogador.tempo_danificado_fim = pygame.time.get_ticks() + 500
    else:
        log.adicionar_mensagem('Se esquivou do ataque!')


def recuperar_mana(jogador):
    mana_recuperada = 15
    jogador.mana = min(jogador.mana + mana_recuperada, jogador.mana_max)
    log.adicionar_mensagem(f"Descansou e recuperou {mana_recuperada} de mana!")


def iniciar_batalha():
    monstros = [
        Monstro("Lobo Terrivel", random.randint(50, 480), random.randint(10, 50), imagem=imagem_lobo, background_img=fundo_lobo),
        Monstro("Gatesco", random.randint(50, 480), random.randint(10, 50), imagem=imagem_gato, background_img=fundo_gato),
        Monstro("O Sol", random.randint(50, 480), random.randint(10, 50), imagem=imagem_sol, background_img=fundo_sol),
        Monstro("Macaco No Abismo", random.randint(50, 480), random.randint(10, 50), imagem=imagem_macaco, background_img=fundo_macaco),
        Monstro("Slime", random.randint(50, 480), random.randint(10, 50), imagem=imagem_slime, background_img=fundo_slime),
    ]
    monstro = random.choice(monstros)
    log.limpar()
    log.adicionar_mensagem(f"Um monstro chamado {monstro.nome} apareceu!")
    return monstro, monstros

# -------------------- UI: instâncias --------------------
log = LogCombate(x=10, y=10, largura=500, altura=150, fonte=fonte)

if imagem_botao_lutar:
    botao_atacar = Botao(232, 381, 336, 79, imagem=imagem_botao_lutar)
else:
    botao_atacar = Botao(232, 381, 336, 50, "Lutar", VERMELHO, BRANCO)

if imagem_botao_fugir:
    botao_fugir = Botao(231, 466, 336, 79, imagem=imagem_botao_fugir)
else:
    botao_fugir = Botao(275, 550, 300, 50, "Fugir", AZUL, BRANCO)

botao_espada = Botao(120, 411, 336, 79, texto='', imagem=imagem_botao_espada)
botao_magia = Botao(340, 411, 336, 79, texto='', imagem=imagem_botao_magia)
botao_voltar = Botao(340, int(483.15), 336, 79, imagem=imagem_botao_voltar)
botao_descansar = Botao(int(120), int(483.15), 336, 79, texto='', imagem=imagem_botao_descansar)

botao_continuar = Botao(LARGURA_TELA//2-100, 400, 200, 50, "Voltar a Luta", VERDE, BRANCO)
botao_sair_derrota = Botao(LARGURA_TELA//2-100, 460, 200, 50, "Desistir", VERMELHO, BRANCO)

botao_continuar_batalha = Botao(LARGURA_TELA // 2 - 150, ALTURA_TELA // 2 - 60, 300, 50, "Continuar", VERDE, BRANCO)
botao_sair_menu = Botao(LARGURA_TELA // 2 - 150, ALTURA_TELA // 2 + 20, 300, 50, "Sair para o Menu", VERMELHO, BRANCO)

botao_pausa_superior = Botao(LARGURA_TELA - 60, 10, 50, 50, imagem=imagem_menu)

botao_iniciar = Botao(240, 310, 320, 70)
botao_sair_jogo = Botao(240, 405, 320, 70) 

# Cartas
cartas_personagens = []
largura_carta, altura_carta = 200, 300
num_cartas = len(PERSONAGENS_JOGAVEIS)
espacamento = 40
largura_total = (num_cartas * largura_carta) + ((num_cartas - 1) * espacamento)
offset_x = (LARGURA_TELA - largura_total) // 2

for i, (nome, dados) in enumerate(PERSONAGENS_JOGAVEIS.items()):
    pos_x = (i * (largura_carta + espacamento)) + offset_x
    pos_y = (ALTURA_TELA - altura_carta) // 2

    caminho_carta = dados.get("imagem_carta")
    imagem_carta_completa = carregar_imagem(caminho_carta, largura_carta, altura_carta, (40, 40, 60), on_fail="none")
    imagem_personagem_individual = carregar_imagem(dados.get("imagem_normal"), 150, 150, (0, 100, 200), on_fail="surface")

    carta = CartaPersonagem(
        x=pos_x,
        y=pos_y,
        largura=largura_carta,
        altura=altura_carta,
        dados_personagem=dados,
        imagem_carta_completa=imagem_carta_completa,
        imagem_personagem=imagem_personagem_individual,
    )
    cartas_personagens.append(carta)

# -------------------- Loop principal --------------------
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE and estado_do_jogo == "batalha":
            estado_do_jogo = "menu_pausa"

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if estado_do_jogo == "menu_inicial":
                tela.blit(imagem_tela_inicial, (0, 0))
                if botao_iniciar.is_clicado(pos):
                    estado_do_jogo = "selecao_personagem"
                elif botao_sair_jogo.is_clicado(pos):
                    rodando = False

            elif estado_do_jogo == "selecao_personagem":
                tela.blit(imagem_tela_seleção, (0, 0))
                for carta in cartas_personagens:
                    if carta.is_clicado(pos):
                        dados_escolhidos = carta.dados_personagem
                        jogador = Jogador(
                            nome=dados_escolhidos.get('nome', 'Herói'),
                            vida=dados_escolhidos.get('vida', 100),
                            mana=dados_escolhidos.get('mana', 30),
                            dano_espada=dados_escolhidos.get('dano_espada', 15),
                            dano_magia=dados_escolhidos.get('dano_magia', 20),
                            imagem_normal=dados_escolhidos.get('imagem_normal'),
                            imagem_dano=dados_escolhidos.get('imagem_dano'),
                            imagem_morto=dados_escolhidos.get('imagem_morto'),
                            imagem_hp_baixo=dados_escolhidos.get('imagem_hp_baixo')
                        )
                        painel_jogador = PainelStatus(
                            24,
                            324,
                            jogador.nome,
                            jogador.vida,
                            jogador.mana,
                            jogador.vida_max,
                            jogador.mana_max,
                            imagem_painel_fundo
                        )
                        if jogador.nome == "Michael":
                            imagem_botao_beat_it = carregar_imagem("botao_beat_it.png", 183, 53, (180, 40, 40))
                            imagem_botao_thriller = carregar_imagem("botao_thriller.png", 183, 53, (180, 40, 40))
                            imagem_botao_earth_song = carregar_imagem("botao_earth_song.png", 183, 53, (40, 180, 40))
                            botao_beat_it = Botao(120, 411, 336, 79, imagem=imagem_botao_beat_it)
                            botao_thriller = Botao(340, 411, 336, 79, imagem=imagem_botao_thriller)
                            botao_earth_song = Botao(int(120), int(483.15), 336, 79, imagem=imagem_botao_earth_song)
                            botoes_luta = [botao_beat_it, botao_thriller, botao_earth_song]
                        else:
                            botao_espada.texto = "Espada"
                            botao_magia.texto = "Magia"
                            botao_descansar.texto = "Descansar"
            
                        monstro_atual, monstros_disponiveis = iniciar_batalha()
                        estado_do_jogo = "batalha"
            elif estado_do_jogo == "batalha" and not jogador_atacou:
                if botao_pausa_superior.is_clicado(pos):
                    estado_do_jogo = "menu_pausa"
                else:
                    if menu_acao == "principal":
                        if botao_atacar.is_clicado(pos):
                            menu_acao = "ataque"
                        elif botao_fugir.is_clicado(pos):
                            estado_do_jogo = "transicao"
                            log.adicionar_mensagem("fugiu!")
                    elif menu_acao == "ataque":
                        if jogador.nome == "Michael":
                            if botao_beat_it.is_clicado(pos):
                                atacar(jogador, monstro_atual, "espada")
                            elif botao_thriller.is_clicado(pos):
                                atacar(jogador, monstro_atual, "magia")
                            elif botao_earth_song.is_clicado(pos):
                                recuperar_mana(jogador)
                                jogador_atacou = True
                                tempo_ataque_jogador_fim = pygame.time.get_ticks() + 1500
                            elif botao_voltar.is_clicado(pos):
                                menu_acao = 'principal'
                        else:
                            if botao_espada.is_clicado(pos):
                                atacar(jogador, monstro_atual, "espada")
                            elif botao_magia.is_clicado(pos):
                                atacar(jogador, monstro_atual, "magia")
                            elif botao_voltar.is_clicado(pos):
                                menu_acao = 'principal'
                            elif botao_descansar.is_clicado(pos):
                                recuperar_mana(jogador)
                                jogador_atacou = True
                                tempo_ataque_jogador_fim = pygame.time.get_ticks() + 1500

            elif estado_do_jogo == "derrota":
                if botao_continuar.is_clicado(pos):
                    estado_do_jogo = "selecao_personagem"
                elif botao_sair_derrota.is_clicado(pos):
                    rodando = False

            elif estado_do_jogo == "menu_pausa":
                if botao_continuar_batalha.is_clicado(pos):
                    estado_do_jogo = "batalha"
                elif botao_sair_menu.is_clicado(pos):
                    estado_do_jogo = "menu_inicial"

    # -------------------- Desenho de tela --------------------
    tela.fill(PRETO)

    if estado_do_jogo == "menu_inicial":
        tela.blit(imagem_tela_inicial, (0, 0))
        botao_iniciar.desenhar(tela)
        botao_sair_jogo.desenhar(tela)

    elif estado_do_jogo == "selecao_personagem":
        tela.blit(imagem_tela_seleção, (0, 0))
        texto_titulo = fonte.render("Escolha seu Personagem", True, BRANCO)
        tela.blit(texto_titulo, texto_titulo.get_rect(center=(LARGURA_TELA // 2, 100)))
        for carta in cartas_personagens:
            carta.desenhar(tela)

    elif estado_do_jogo in ["batalha", "menu_pausa"]:
        if monstro_atual and monstro_atual.background_img:
            tela.blit(monstro_atual.background_img, (0, 0))

        painel_jogador.vida = jogador.vida
        painel_jogador.mana = jogador.mana

        log.atualizar()

        if jogador_atacou and pygame.time.get_ticks() > tempo_ataque_jogador_fim:
            jogador_atacou = False
            if monstro_atual and monstro_atual.esta_vivo():
                ataque_monstro(monstro_atual, jogador)

        if jogador.esta_danificado and pygame.time.get_ticks() > jogador.tempo_danificado_fim:
            jogador.esta_danificado = False

        if not jogador.esta_vivo():
            estado_do_jogo = "derrota"
            log.limpar()
        elif monstro_atual and not monstro_atual.esta_vivo():
            estado_do_jogo = "transicao"

        if monstro_atual:
            monstro_atual.desenhar()
        log.desenhar(tela)

        imagem_painel = jogador.imagem_normal
        if jogador.esta_danificado:
            imagem_painel = jogador.imagem_dano
        elif jogador.vida <= jogador.vida_max * 0.5:
            imagem_painel = jogador.imagem_hp_baixo

        painel_jogador.desenhar(tela, fonte, imagem_painel)

        if imagem_menu:
            botao_pausa_superior.desenhar(tela)
        else:
            botao_pausa_superior_texto = Botao(LARGURA_TELA - 100, 10, 90, 40, "PAUSA", CINZA_CLARO, PRETO)
            botao_pausa_superior_texto.desenhar(tela)

        if menu_acao == "principal":
            botao_atacar.desenhar(tela)
            botao_fugir.desenhar(tela)
        elif menu_acao == "ataque":
            if jogador.nome == "Michael":
                for botao in botoes_luta:
                    botao.desenhar(tela)
                    botao_voltar.desenhar(tela)
            else:
                botao_espada.desenhar(tela)
                botao_magia.desenhar(tela)
                botao_voltar.desenhar(tela)
                botao_descansar.desenhar(tela)

        if estado_do_jogo == "menu_pausa":
            s = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
            s.fill((0, 0, 0, 150))
            tela.blit(s, (0, 0))

            texto_pausa = fonte.render("PAUSA", True, BRANCO)
            texto_pausa_rect = texto_pausa.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 - 120))
            tela.blit(texto_pausa, texto_pausa_rect)

            botao_continuar_batalha.desenhar(tela)
            botao_sair_menu.desenhar(tela)

    elif estado_do_jogo == "transicao":
        monstro_atual = random.choice(monstros_disponiveis)
        monstro_atual.vida = monstro_atual.vida_max
        log.adicionar_mensagem(f"Um novo monstro apareceu: {monstro_atual.nome}!")
        estado_do_jogo = "batalha"

    elif estado_do_jogo == "derrota":
        tela.fill(PRETO)
        texto_derrota = fonte.render("Eles venceram...", True, VERMELHO)
        texto_derrota_rect = texto_derrota.get_rect(center=(LARGURA_TELA // 2, 150))
        tela.blit(texto_derrota, texto_derrota_rect)

        imagem_morte_rect = jogador.imagem_morto.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2))
        tela.blit(jogador.imagem_morto, imagem_morte_rect)

        botao_continuar.desenhar(tela)
        botao_sair_derrota.desenhar(tela)

    pygame.display.flip()
    clock.tick(60)

sys.exit()
pygame.draw.rect
